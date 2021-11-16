# uFEL-FT

This python modual solves the unavrage 1D free electron laser (FEL) equasions [1] using fourier analysis.

## Installing
A _pip_ and/or _deb_ file will be provided in the future.
### Pip
```
cd Downloads/
git clone https://github.com/Paulire/unaveraged-FEL-Fourier
cd unaveraged-FEL-Fourier
pip3 install .
```

To uninstall: ```pip3 uninstall ufel_ft```

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
Will solve the FEL equasions based off ```FEL_FT``` inputs. The model is solved in chunks of z, if ctrl+c is pressed during run, then the modual will store data up the model upto the last complete chunk.

```def save( fname )```
Saves the output of the simulation.
 * ```fname``` - string - Save location (json)

```def plot_z1_A( z, fname, dpi )```
Plots |A|^2 as a function of z_1 for a given z position
 * ```z``` - float - Postion to plot
 * ```fname``` - float - Name of file to save, if not set then the plot is just displayed and not save
 * ```dpi``` - int - DPI for saved image

## Example
```
import ufel_ft

fel = ufel.FEL_FT( dz=(0,1,150),
                   dz_1=(0,3,800),
                   N=800,
                   l_e=2,
                   n_bar=400,
                   rho=1e-2 )
                   
fel.run()

>>> Running z segment 0.0 --> 1.0 upto z=1.0
>>> IVP: 100%|###################################| 1.00/1.00 [01:40<00:00, 101s/ut]

fel_func.save( 'out.json' )
fel_func.plot_z1_A( 1, fname='out.pdf' )
```

![alt text](https://github.com/Paulire/unaveraged-FEL-Fourier/raw/main/img/out_1.png "Logo Title Text 1")

[1] - https://doi.org/10.1016/S0030-4018(99)00222-9 
