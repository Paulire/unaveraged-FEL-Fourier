# -*- coding: utf-8 -*-

"""
Created on Mon Oct 12:20 2021

@author: paul
"""

import numpy as np

# Calculates the E feild as a function z by integrating A_out as a function of z_1 for each z point
def _calc_E( self ):
    from scipy.integrate import simpson
    return np.array( [ simpson( np.abs( self.A_out[:,i] )**2, self.z_1 ) for i in range( self.current_save_index + 1 )] )

# Calculates the spectral power as a function of z
def _calc_spectral_power( self ):
   from scipy.integrate import simpson
   return np.array( [ simpson( np.abs(self.A_out_ft[:,i])**2, self.z_1 ) for i in range( self.z.shape[0] ) ] )
