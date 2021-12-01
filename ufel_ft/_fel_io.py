# -*- coding: utf-8 -*-

"""
Created on Mon Oct 12:32 2021

@author: paul
"""

import json
from numpy import array as np_array

def _load( self, fname ):
    if fname == None or type( fname ) != str:
        raise TypeError( "'fname' must be a string" )

    # Try to open the file
    try:
        input_file = open( fname, 'r' )
    except:
        print("Could not load file")
        raise FileNotFoundError( str(fname) + "fname could not be found" )

    # Load the json input into a dictionary
    try:
        input_data = json.load( input_file )
        input_file.close()
    except:
        raise FileExistsError("fname is not a json")

    # Load the data to the relevent variables
    self.N_z = input_data['N_z']
    self.N_z1 = input_data['N_z1']
    self.current_save_index = input_data['current_save_index']
    self.N = input_data['N']
    self.l_e = input_data['l_e']
    self.beam_off_z1 = input_data['beam_off_z1']
    self.n_bar = input_data['n_bar']
    self.rho = input_data['rho']
    self.A = np_array( eval( input_data['A'] ) )
    self.p_j = np_array( eval( input_data['p_j'] ) )
    self.A_out_ft = np_array( eval( input_data['A_out_ft'] ) )
    self.A_out = np_array( eval( input_data['A_out'] ) )
    self.E_z = np_array( eval( input_data['E_z'] ) )
    self.chi = np_array( eval( input_data['chi'] ) )
    self.z = np_array( eval( input_data['z'] ) )
    self.z_1 = np_array( eval( input_data['z_1'] ) )
    self.z_1_j = np_array( eval( input_data['z_1_j'] ) )
    self.z_1_j_out = np_array( eval( input_data['z_1_j_out'] ) )
    self.p_j_out = np_array( eval( input_data['p_j_out'] ) )
    self.omega = np_array( eval( input_data['omega'] ) )
    self.spectral_power_z = np_array( eval( input_data['spectral_power_z'] ) )

    del( input_data )

    return 0

def _save( self, fname=None ):
    # Validate file
    if fname == None or type( fname ) != str:
        raise TypeError( "'fname' must be a string" )

    # Try to open the file
    try:
        data_file = open( fname, 'w' )
    except:
        raise FileNotFoundError( "could note save" )

    # Converts all the relevent data to a dictionary
    output_data = { 'N_z': self.N_z,
                    'N_z1': self.N_z1,
                    'current_save_index': self.current_save_index,
                    'N': self.N,
                    #'l_e': self.l_e,
                    #'beam_off_z1': self.beam_off_z1,
                    'n_bar': self.n_bar,
                    'rho': self.rho,
                    'A': str( self.A.tolist() ),
                    'p_j': str( self.p_j.tolist()),
                    'A_out_ft': str( self.A_out_ft.tolist() ),
                    'A_out': str( self.A_out.tolist() ), 
                    'z_1_j_out': str( self.z_1_j_out.tolist() ),
                    'p_j_out': str( self.p_j_out.tolist() ),
                    'E_z': str( self.E_z.tolist() ),
                    'chi': str( self.chi.tolist() ),
                    'z_1': str( self.z_1.tolist() ),
                    'z': str( self.z[:self.current_save_index+1].tolist() ),
                    'z_1_j': str( self.z_1_j.tolist() ),
                    'spectral_power_z': str( self.spectral_power_z.tolist() ),
                    'omega': str( self.omega.tolist() ) }

    # Puts the data into a json file
    json_data = json.dumps( output_data )
    data_file.write( json_data )
    data_file.close()

    del( output_data )
    del( json_data )

    return 0
