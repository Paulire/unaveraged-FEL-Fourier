# -*- coding: utf-8 -*-

"""
Created on Thu Sep 23 11:45:32 2021

Contains file for setting up the integration enviroment

@author: paul.ireland.2017@uni.strath.ac.uk
"""
import numpy as np
from _fel_io import _load
from sys import exit

def __init__( self, dz=None, dz_1=None, N=None, l_e=None, n_bar=None, rho=None, chi=None, l_bar=None, delta_bar=0, fname=None, continue_from_file=False, z_end_file = None ):
    # Load data from a file if specified, else set data from inputs
    if fname != None:
        _load( self, fname )

        # Check if the user wants to continue running from the end of the file
        if continue_from_file == True:
            self.continue_from_file = True 

            # Extends the existing z values to the new limit and saves the inital starting point
            try:
                z_end = self.z[-1]
                self.z = np.unique( np.append( self.z, np.linspace( self.z[-1], z_end_file[0], z_end_file[1] ) ) ) # Extended z array
                self.continue_from_file_z_value = np.where( self.z == z_end )[0][0] # Model starting point
            except:
                return Exception( "Make sure 'continue_from_file' is defined correctly" )

        return 0

    else:
        self.continue_from_file = False

    # z and z_1 ranges, inputs must be tupples (start, end, number)
    try:
        self.z = np.linspace( dz[0], dz[1], dz[2] )
        self.z_1 = np.linspace( dz_1[0], dz_1[1], dz_1[2] )
    except:
        raise TypeError( "Ensure 'dz' and 'dz_1' are both tuple")
        
    # Save the number of z and z_1 values
    self.N_z = dz[2]
    self.N_z1 = dz_1[2]
    
    # Number of particles N
    if type( N ) != int:
        raise TypeError( "'N' must be an int")
    elif N < 0:
        raise ValueError("'N' must be a positive value")
    self.N = N
    
    # l_e, electron beam length in z_1
    if type( l_e ) != float:
        try:
            self.l_e = float( l_e )
        except:
            raise TypeError( "'l_e' must be a float")
    elif l_e > self.z_1[-1]:
        raise ValueError("'l_e' must lie in the value bounds of z_1")
    else:
        self.l_e = l_e
        
    # The particles are placed between z_1[0] and l_e evenly then offset by a random number
    self.z_1_j = np.linspace( self.z_1[0], l_e, N, endpoint=True )

    # Number of electrons per unit z_1
    if type( n_bar ) != float:
        try:
            self.n_bar = float( n_bar )
        except:
            raise TypeError( "'n_bar' must be a float")
    else:
        self.n_bar = n_bar
    
    # Sets the free electron laser paramiter
    if type( rho ) != float:
        try:
            self.rho = float( rho )
        except:
            raise TypeError( "'rho' must be a float")
    else:
        self.rho = rho

    # Sets the undulator modual length
    if type( l_bar ) != float:
        try:
            self.l_bar = float( l_bar )
        except:
            raise TypeError( "'l_bar' must be a float" )
    else:
        self.l_bar = l_bar
    
    # Sets the chicane length
    if type( delta_bar ) != float:
        try:
            self.delta_bar = float( delta_bar )
        except:
            raise TypeError( "'delta_bar' must be a float" )
    else:
        self.delta_bar = delta_bar

    # Number of undulor modulas
    self.num_segmets = int( self.z[-1]/( self.l_bar + self.delta_bar  ) ) 

    # Chi is the charge weighting paramiter, needs improvement
    if chi == None:
        self.chi = np.zeros( N ) + 1

def set_initial_condition( self ):
    # Currently just sets it automatically
    self.A = np.zeros( self.N_z1 ) #+ 1e-8            # Field amplitude
    self.p_j = np.zeros( self.N )
