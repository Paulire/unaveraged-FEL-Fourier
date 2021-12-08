# -*- coding: utf-8 -*-


import numpy as np
import matplotlib
from matplotlib import pyplot as plt

# Plots |A|^2 as a function of z_1 at the point z
def _plot_z1_A( self, z, fname, dpi ):
    #if type(z) != float xor type(z) != int:
    #    raise TypeError( "'z' must be a float or int" )

    # Sets z point index (finds the closes z)
    index = np.abs( self.z[:self.current_save_index+1] - z ).argmin()

    #plt.style.use( ['science', 'ieee'] )
    matplotlib.rcParams['font.family'] = 'serif'
    matplotlib.rcParams['mathtext.fontset'] = 'dejavuserif'
    matplotlib.rcParams['text.usetex'] = 'True'
    matplotlib.rcParams['text.latex.preamble'] = '\\usepackage{amsmath} \\usepackage{amssymb}'
    matplotlib.rcParams['axes.linewidth'] = '1.2'

    fig, axs = plt.subplots(  )
    axs.plot( self.z_1, np.abs(self.A_out[:,index])**2, '-k')
    axs.set_xlabel('$\\bar{z}_{1}$', fontsize=20)
    axs.set_ylabel('$|A|^2$', fontsize=20)
    axs.set_title('$\\bar{z}=' + str( round( self.z[index],2 ) ) + str('$'))
    axs.set_ylim( 0,np.max( 1.05*np.abs(self.A_out)**2 ) )
    axs.set_xlim( self.z_1[0], self.z_1[-1] )

    axs.tick_params( direction='in', axis='both', length=6, right=True, top=True, which="both", labelsize=18 )
    axs.ticklabel_format(axis='y', style='sci',scilimits=(-2,2))
    axs.tick_params(axis='x', pad=6)
    axs.tick_params(axis='y', pad=6)
    axs.yaxis.offsetText.set_fontsize(18)
    axs.minorticks_on()
    axs.tick_params( which='minor', length=3, direction='in'  )

    plt.tight_layout()

    if fname != None:
        plt.savefig(fname, 
                    dpi=dpi)
    else:
        plt.show()

    plt.close( fig )

def _plot_E_z( self, fname, dpi ):
    matplotlib.rcParams['font.family'] = 'serif'
    matplotlib.rcParams['mathtext.fontset'] = 'dejavuserif'
    matplotlib.rcParams['text.usetex'] = 'True'
    matplotlib.rcParams['text.latex.preamble'] = '\\usepackage{amsmath} \\usepackage{amssymb}'
    matplotlib.rcParams['axes.linewidth'] = '1.2'

    fig, axs = plt.subplots(  )
    axs.plot( self.z, self.E_z, '-k')
    axs.set_xlabel('$\\bar{z}$', fontsize=20)
    axs.set_ylabel('$E$', fontsize=20)
    axs.set_ylim( 0, 1.01*np.max( self.E_z ) )
    axs.set_xlim( self.z[0], self.z[-1] )

    axs.tick_params( direction='in', axis='both', length=6, right=True, top=True, which="both", labelsize=18 )
    axs.tick_params(axis='x', pad=6)
    axs.tick_params(axis='y', pad=6)
    axs.yaxis.offsetText.set_fontsize(18)
    axs.minorticks_on()
    axs.tick_params( which='minor', length=3, direction='in'  )

    plt.tight_layout()

    if fname != None:
        plt.savefig(fname, 
                    dpi=dpi)
    else:
        plt.show()

    plt.close( fig )

def _plot_power_z( self, fname, dpi ):
    matplotlib.rcParams['font.family'] = 'serif'
    matplotlib.rcParams['mathtext.fontset'] = 'dejavuserif'
    matplotlib.rcParams['text.usetex'] = 'True'
    matplotlib.rcParams['text.latex.preamble'] = '\\usepackage{amsmath} \\usepackage{amssymb}'
    matplotlib.rcParams['axes.linewidth'] = '1.2'

    fig, axs = plt.subplots( )
    axs.plot( self.z,self.spectral_power_z, '-k' )
    axs.set_ylim( 0, max( self.spectral_power_z ) )
    axs.set_xlim( self.z[0], self.z[-1] )
    axs.set_xlabel('$\\bar{z}$', fontsize=20)
    axs.set_ylabel('$P$', fontsize=20)

    axs.tick_params( direction='in', axis='both', length=6, right=True, top=True, which="both", labelsize=18 )
    axs.minorticks_on()
    axs.tick_params( which='minor', length=3, direction='in'  )

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

    matplotlib.rcParams['font.family'] = 'serif'
    matplotlib.rcParams['mathtext.fontset'] = 'dejavuserif'
    matplotlib.rcParams['text.usetex'] = 'True'
    matplotlib.rcParams['text.latex.preamble'] = '\\usepackage{amsmath} \\usepackage{amssymb}'
    matplotlib.rcParams['axes.linewidth'] = '1.2'
    
    fig, axs = plt.subplots(  )
    axs.plot( self.omega, np.abs( self.A_out_ft[:,index] )**2, '-k')
    axs.set_xlabel('$\\omega$', fontsize=20)
    #axs.set_ylabel('$|\\mathcal{F}(A)|^2$', fontsize=20)
    axs.set_ylabel('$|\\hat{A}|^2$', fontsize=20)

    axs.tick_params( direction='in', axis='both', length=6, right=True, top=True, which="both", labelsize=18 )
    axs.minorticks_on()
    axs.tick_params( which='minor', length=3, direction='in'  )

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
