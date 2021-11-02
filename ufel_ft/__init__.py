# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 09:29:17 2021

@author: paul
"""
import _setup
import _main
import _plot
import _fel_io

class FEL_FT:
    # Set's up the user inputs into a usable manner
    def __init__( self, dz=None, dz_1=None, N=None, l_e=None, n_bar=None, rho=None, chi=None, fname=None, continue_from_file=False, z_end_file = None ):
        _setup.__init__( self, dz, dz_1, N, l_e, n_bar, rho, chi, fname, continue_from_file, z_end_file )
    
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

    # Save the data as a json file
    def save( self, fname=None ):
        _fel_io._save( self, fname )
