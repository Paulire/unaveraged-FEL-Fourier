#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 11:11:34 2021

@author: paul
"""
import numpy as np
from scipy import interpolate
from matplotlib import pyplot as plt
from sys import exit
import time

def fel_eq( z, y, N,N_z_1, omega, chi, rho, n_bar, z_1, omega_prime, _1_2_rho, ifft_fact ):
    #time_val = []

    #start = time.time()
    A_hat = np.array( y[:N_z_1] + 1j*y[N_z_1:2*N_z_1] )
    #time_val.append( time.time() - #start )

    #start = time.time()
    # Conert A hat to real space
    A = np.fft.ifft( A_hat )*ifft_fact
    #time_val.append( time.time() - #start )

    #start = time.time()
    # Linear intepolation to fined A(z,z_1_j) values
    A_z_1_j = np.interp( y[2*N_z_1:2*N_z_1+N], z_1, A )
    #time_val.append( time.time() - #start )

    #B = 1/(2*rho)
    #omega_prime = omega+B

    #start = time.time()
    dAdz = np.sum( np.exp( -1j*np.outer(y[2*N_z_1:2*N_z_1+N], omega_prime )), axis=0)/n_bar - 1j*omega*A_hat
    #time_val.append( time.time() - #start )
    #start = time.time()
    dzdz = 2*rho*y[2*N_z_1 + N:2*(N_z_1 + N)] 
    #time_val.append( time.time() - #start )
    #start = time.time()
    dpdz = -2*(A_z_1_j*np.exp( 1j*y[2*N_z_1:2*N_z_1+N]*_1_2_rho )).real
    #time_val.append( time.time() - #start )

    #dzdz = [ 0 for i in range(N) ]
    #dpdz = [ 0 for i in range(N) ]

    #start = time.time()
    out = np.concatenate(( dAdz.real, dAdz.imag, dzdz, dpdz ))
    #time_val.append( time.time() - #start )

    #print( #time_val )
    #exit()

    return out
        
