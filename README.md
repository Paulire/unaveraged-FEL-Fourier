# uFEL-FT

This python modual solves the unavrage 1D free electron laser (FEL) equasions [1] using fourier analysis.

## Installing
A _pip_ and/or _deb_ file will be provided in the future.

## Usage

```class FEL_FT( dz, dz_1, N, l_e, n_bar, rho, chi, fname, continue_from_file, z_end_file )```
The init function for the FEL model
 * ```dz``` - tupple - Limits and number of z points (start, end, N)
 * ```dz_1``` - tupple - Limits and number of z_1 points (start, end, N)
 * ```N``` - int - Number of electrons
 * ```l_e``` - float - Length of electron pulse in ```z_1```
 * ```n_bar``` - float - N/l_e, will be defunct in the future
 * ```rho``` - float - Dimentionaless undulator paramiter
 * ```chi``` - array - Charge weighting parameter, if ```None``` then default all is 1
 * ```fname``` - string - Load a previuse file
 * ```continue_from_file``` - bool - contine from the end of the ```fname``` position if ```True```
 * ```z_end_file``` - tupple - Limits and number of z points (start, end, N) if ```continue_from_file``` is ```True```

```def run()```
Will solve the FEL equasions based off ```FEL_FT``` inputs

```def save( fname )```
Saves the output of the simulation.
 * ```fname``` - string - Save location (json)

```def plot_z1_A( z, fname, dpi )```
Plots |A|^2 as a function of z_1 for a given z position
 * ```z``` - float - Postion to plot
 * ```fname``` - float - Name of file to save, if not set then the plot is just displayed and not save
 * ```dpi``` - int - DPI for saved image

[1] - https://doi.org/10.1016/S0030-4018(99)00222-9 
