# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 09:29:17 2021

@author: paul
"""
import _setup
import _main
import _plot
import _fel_io

import numpy as np

class FEL_FT:
    # Set's up the user inputs into a usable manner
    def __init__( self, dz=None, dz_1=None, N=None, l_e=None, n_bar=None, rho=None, chi=None, l_bar=1, delta_bar=0, fname=None, continue_from_file=False, z_end_file = None ):
        # Declarer each verlible so that the user may see the when pressing tab in a code editor
        self.z = np.array( [0.0] )
        self.continue_from_file = bool( None )
        self.continue_from_file_z_value = int(0)
        self.z_1 = np.array( [0.0] )
        self.N_z = int(0)
        self.N_z1 = int(0)
        self.N = int(0)
        self.l_e = float(0)
        self.z_1_j = np.array( [0.0] )
        self.n_bar = float(0)
        self.rho = float(0)
        self.l_bar = float(0)
        self.delta_bar = float(0)
        self.chi = np.zeros(1)
        self.A = np.zeros( 1, dtype=complex ) #+ 1e-8            # Field amplitude
        self.p_j = np.zeros( 1 )

        # Settup the verlibles
        _setup.__init__( self, dz, dz_1, N, l_e, n_bar, rho, chi, l_bar, delta_bar, fname, continue_from_file, z_end_file )
    
    # Currently used to set the values of A and chi, should be moved to __init__
    def set_initial_condition( self ):
        _setup.set_initial_condition( self )
        
    # Preforms the fourier transform, the integration of the ODEs and the inverse fourer transform
    def run( self ):
        _main.run( self )

    # Plots |A|^2 as a function of z_1 at the point z
    def plot_z1_A( self, z, fname=None, dpi=300 ):
        _plot._plot_z1_A( self, z, fname, dpi )

    def plot_E_z( self, fname=None, dpi=300 ):
        _plot._plot_E_z( self, fname, dpi )

    def plot_fourier( self, z, fname=None, dpi=300 ):
        _plot._plot_fourier( self, z, fname, dpi )

    def plot_pj_z1( self, z, fname=None, dpi=300 ):
        _plot._plot_pj_z1( self, z, fname, dpi )

    def plot_power_z( self, fname=None, dpi=300 ):
        _plot._plot_power_z( self, fname, dpi )

    # Save the data as a json file
    def save( self, fname=None ):
        _fel_io._save( self, fname )
