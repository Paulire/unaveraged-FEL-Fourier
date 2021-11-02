# -*- coding: utf-8 -*-

"""
Created on Thu Sep 29 10:00 2021

Contains any functions required to run the integration system

@author: paul.ireland.2017@uni.strath.ac.uk
"""
import numpy as np
from scipy.integrate import solve_ivp
from matplotlib import pyplot as plt
from tqdm import tqdm
from sys import exit

import diff_eq
from _analysis import _calc_E

# This loads the OdeSolver step and init fucntion and saves the ones to be monkey edited as backups 
from scipy.integrate._ivp.rk import OdeSolver
_solve_ivp_init = OdeSolver.__init__
_solve_ivp_step = OdeSolver.step

# This is init monkey code for solve_ivp which adds the progress bar
def new_ivp_init( self, fun, t0, y0, tf, vectorized, **options ):
    # Create the progress bar
    self.pbar = tqdm( total=tf - t0, unit='ut', initial=0, ascii=True, desc='IVP', dynamic_ncols=True, unit_scale=True)
    self.last_t = t0

    # Call original init function for OdeSolver
    _solve_ivp_init( self, fun, t0, y0, tf, vectorized, **options )

# Updates the progress bar between steps
def new_ivp_step( self ):
    # Call the old OdeSolver stepping function
    _solve_ivp_step( self )

    # Updates the progress bar
    # update the bar
    tst = self.t - self.last_t
    self.pbar.update(tst)
    self.last_t = self.t

    # close the bar if the end is reached
    if self.t >= self.t_bound:
        self.pbar.close()

# Points OdeSovers functions to the new functions
OdeSolver.__init__ = new_ivp_init
OdeSolver.step = new_ivp_step

def run( self ):
    # If the input file wan't to be extended then set up the code to continue the model from the last point
    if self.continue_from_file == True:
        indexes = [ self.continue_from_file_z_value ] # Starting index

        # Find check if the next highest whole number is in z
        if np.ceil( self.z[indexes[0]] + 1e-12 ) < self.z[-1]:
            indexes.append(
                           np.abs( self.z - np.ceil( self.z[indexes[0]] ) ).argmin()
                          )

        # Now check if the next whole number z is to be modelled
        # If so, then this will increase the array of index boundrays
        # upto the maximum whole number
        if np.ceil( self.z[indexes[-1]] ) + 1 < self.z[-1]:
            # The differenace between whole numbered z represented by there index
            diff_index = ( np.abs( self.z - np.ceil( self.z[indexes[-1]] + 1 )).argmin() -
                           np.abs( self.z - np.ceil( self.z[indexes[-1]] ) ).argmin() )
            offset = indexes[-1] + diff_index   # Start point for new model offset
            new_indexes = [ offset + i*diff_index for i in range( 0,
                                                                  (self.z.shape[0]-offset)//diff_index + 1) ]

            indexes = np.concatenate( ( indexes, new_indexes ) )
            indexes = indexes.tolist()

        # If the final z value is not a whole number, then the final index
        # point for z is added to the list of indexes
        if indexes[-1] != self.z.shape[0] - 1: 
            indexes.append( self.z.shape[0] - 1 )

        indexes = np.array( indexes, dtype=int ).tolist()


        A = False
        if A == True:
            print( self.A_out.shape )
            print( self.z.shape )
            print( self.z[self.A_out.shape[1]-1] )
            print( '-----' )
            print( indexes )
            print( '-----' )
            [ print( self.z[i] ) for i in indexes ]
            exit()

        self.omega = 2*np.pi*np.fft.fftfreq( self.N_z1, (self.z_1[1] - self.z_1[0] )) # Del plzz
        self.A_hat = self.A_out_ft[:,-1]*(self.z_1[1] - self.z_1[0])
        self.z_1_j = self.z_1_j_out[:,-1]
        self.p_j = self.p_j_out[:,-1]
    
    # Else, set up a new model
    else:
        # These will be used to store the output data, being None implies that the simulation must start from z=0
        # If it is not None then the simulation will continue as normal
        self.A_out_ft = None
        self.z_1_j_out = None
        self.p_j_out = None

        # Preform the fourier transformation on the initial conditions
        # and on z_1
        self.omega = 2*np.pi*np.fft.fftfreq( self.N_z1, (self.z_1[1] - self.z_1[0] ))
        self.A_hat = np.fft.fft( self.A )*(self.z_1[1] - self.z_1[0])

        # This will split the runs into sizes of \delta z=1 and run each individually
        # This will allow early termination of the model and will still save the data
        first_index = int( 1//( self.z[1]-self.z[0] ) )
        indexes = [ i*first_index for i in range( self.z.shape[0]//first_index + 1 ) ]
        if indexes[-1] != self.z.shape[0] - 1: 
            indexes.append( self.z.shape[0] - 1 )


    # solve_ivp does not accept complex number by default
    A_hat_prime = np.concatenate( ( self.A_hat.real, self.A_hat.imag ) )
    
    # solve_ivp's inital conditons must be a continus array
    #input_data = A_hat_prime.tolist() + self.z_1_j.tolist() + self.p_j.tolist()
    input_data = np.concatenate(( A_hat_prime, self.z_1_j, self.p_j ))

    self.current_save_index = indexes[0]

    # Omega is altered to be
    _1_2_rho = 1/(2*self.rho)
    omega_prime = self.omega + _1_2_rho

    # 'out' is the output of the fourier tranformed ODE
    for i in range( len( indexes ) - 1 ):
        # If ctrl+c pressed, then the model will terminate and the data upto the latest run chunk will save
        try:
            print( "Running z segment " + str( round( self.z[indexes[i]], 2 ) ) + ' --> ' + str( round( self.z[indexes[i+1]], 2 ) ) + ' for upto z=' + str( round( self.z[-1] ) ) )
            
            # Use last run data to get this runs IC
            input_data = out.y[:,-1] if i != 0 else input_data

            # Run the model
            out = solve_ivp(diff_eq.fel_eq,
                            #[ self.z[0], self.z[-1] ],
                            [ self.z[ indexes[i]], self.z[ indexes[i+1] ] ],
                            input_data, method='LSODA',
                            #t_eval=self.z,
                            t_eval=self.z[ indexes[i]:indexes[i+1] + 1 ] if i != len( indexes ) - 2 else self.z[ indexes[i]: ],
                            args=(self.N, self.N_z1,self.omega, self.chi, self.rho, self.n_bar, self.z_1, omega_prime, _1_2_rho, 1/(self.z_1[1] - self.z_1[0]) ),
                            atol=1e-5 )
                            #rtol=1e-2 )

            # Stores the data from the last run in relevent output data sets
            if type( self.A_out_ft ) == type( None ):
                self.A_out_ft = out.y[:self.N_z1,:] + out.y[self.N_z1:self.N_z1*2,:]*1j
                self.z_1_j_out = out.y[self.N_z1*2:self.N_z1*2+self.N]
                self.p_j_out = out.y[ self.N_z1*2+self.N: ]
            else:
                self.A_out_ft = np.hstack( [ self.A_out_ft, out.y[:self.N_z1,:] + out.y[self.N_z1:self.N_z1*2,:]*1j ] )
                self.z_1_j_out =  np.hstack( [ self.z_1_j_out, out.y[self.N_z1*2:self.N_z1*2+self.N] ] )
                self.p_j_out = np.hstack( [ self.p_j_out, out.y[ self.N_z1*2+self.N: ] ] )

            self.current_save_index = indexes[i+1]

        except KeyboardInterrupt: 
            break

    if self.current_save_index == 0:
        print("\nThe simulation did not run for long enough to record any data - killed")
        exit()
    
    # Get the FT data
    #self.A_out_ft = out.y[:self.N_z1,:] + out.y[self.N_z1:self.N_z1*2,:]*1j
    
    # Convert FT data into wave data
    self.A_out = np.zeros( (self.N_z1,self.current_save_index+1), dtype=np.complex128 )
    for i in range( self.current_save_index + 1 ):
        self.A_out[:,i] = np.fft.ifft( self.A_out_ft[:,i] )/(self.z_1[1] - self.z_1[0])

    # Calculate the E field as a function of z
    self.E_z = _calc_E( self )

    # Get the remaining output data (z_1_j & p_j)
    #self.z_1_j_out = out.y[self.N_z1*2:self.N_z1*2+self.N]
    #self.p_j_out = out.y[ self.N_z1*2+self.N: ]

    return 0 
