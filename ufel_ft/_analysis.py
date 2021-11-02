# -*- coding: utf-8 -*-

"""
Created on Mon Oct 12:20 2021

@author: paul
"""

import numpy as np

# Calculates the E feild as a function z by integrating A_out as a function of z_1 for each z point
def _calc_E( self ):
    from scipy.integrate import trapezoid
    return np.array( [ trapezoid( np.abs( self.A_out[:,i] )**2, self.z_1 ) for i in range( self.current_save_index )] )

