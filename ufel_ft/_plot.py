# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt

# Plots |A|^2 as a function of z_1 at the point z
def _plot_z1_A( self, z, fname, dpi ):
    #if type(z) != float xor type(z) != int:
    #    raise TypeError( "'z' must be a float or int" )

    # Sets z point index (finds the closes z)
    index = np.abs( self.z[:self.current_save_index+1] - z ).argmin()

    plt.style.use( ['science', 'ieee'] )
    fig, axs = plt.subplots(  )
    axs.plot( self.z_1, np.abs(self.A_out[:,index])**2, '-k')
    #axs.plot( self.z_1_j_out[:,index], np.zeros( len( self.z_1_j_out[:,index] ) ), 'xr' )
    axs.set_xlabel('$\\bar{z}_{1}$', fontsize=20)
    axs.set_ylabel('$|A|^2$', fontsize=20)
    axs.set_title('$\\bar{z}=' + str( round( self.z[index],2 ) ) + str('$'))
    axs.set_ylim( 0,np.max( 1.1*np.abs(self.A_out)**2 ) )
    axs.set_xlim( self.z_1[0], self.z_1[-1] )
    plt.tight_layout()

    if fname != None:
        plt.savefig(fname, 
                    dpi=dpi)
    else:
        plt.show()

    plt.close( fig )

def _plot_E_z( self, fname, dpi ):
    fig, axs = plt.subplots(  )
    axs.plot( self.z, self.E_z, '-k')
    #axs.set_yscale( 'log' )
    axs.set_xlabel('$\\bar{z}$', fontsize=20)
    axs.set_ylabel('$E$', fontsize=20)
    plt.tight_layout()

    if fname != None:
        plt.savefig(fname, 
                    dpi=dpi)
    else:
        plt.show()

    plt.close( fig )

def _plot_fourier( self, z, fname, dpi ):
    # Sets z point index (finds the closes z)
    index = np.abs( self.z - z ).argmin()
    
    omega = np.fft.fftfreq( self.A_out_ft.shape[0], self.z_1[1] - self.z_1[0] )

    fig, axs = plt.subplots(  )
    axs.plot( omega[ :omega.shape[0]//2 ], np.abs( self.A_out_ft[:omega.shape[0]//2,index] )**2, '-k')
    axs.set_xlabel('$\\omega$', fontsize=20)
    axs.set_ylabel('$|\\mathcal{F}(A)|^2$', fontsize=20)
    plt.tight_layout()

    if fname != None:
        plt.savefig(fname, 
                    dpi=dpi)
    else:
        plt.show()

    plt.close( fig )

def _plot_pj_z1( self, z, fname, dpi ):
    # Sets z point index (finds the closes z)
    index = np.abs( self.z - z ).argmin()

    A = np.random.randint(0,799)

    fig, axs = plt.subplots( )
    #axs.plot( self.z_1_j_out[:,index], self.p_j_out[:,index], '.r' )
    axs.plot( self.z_1_j_out[A,:index+1], self.p_j_out[A,:index+1], '-r' )
    axs.plot( self.z_1_j_out[A,0], self.p_j_out[A,0], 'xr' )
    axs.plot( self.z_1_j_out[A,index], self.p_j_out[A,index], '.r' )
    axs.set_xlabel("$\\bar{z}_1$", fontsize=20 )
    axs.set_xlabel("$p$", fontsize=20 )
    plt.tight_layout()

    print( index )
    print( self.z_1_j_out[A,:index+1] )

    if fname != None:
        plt.savefig(fname, 
                    dpi=dpi)
    else:
        plt.show()

    plt.close( fig )
