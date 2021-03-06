## Description
2D Image data is plotted as the initial state of a quantum mechanical system, and  evolved under the influence of its own self-interacting [gravitational potential](https://en.wikipedia.org/wiki/Poisson%27s_equation) according to the [Schrodinger-Poisson Equation](https://en.wikipedia.org/wiki/Schr%C3%B6dinger%E2%80%93Newton_equation#:~:text=The%20Schr%C3%B6dinger%E2%80%93Newton%20equation%2C%20sometimes,function%20as%20a%20mass%20density%2C). The nonlinear self-interaction term present in this equation is a modification of standard quantum mechanics, and was originally proposed as an explanation for the self-gravitation of hypothetical boson stars, and later as an explanation for wavefunction collapse. Modeling quantum systems with the Schrodinger-Poisson equation finds real-world applications in the study of both [Bose-Einstein condensates](https://en.wikipedia.org/wiki/Bose%E2%80%93Einstein_condensate) and ["fuzzy" dark matter](https://en.wikipedia.org/wiki/Fuzzy_cold_dark_matter).

The main algorithm uses [Leapfrog Integration](https://en.wikipedia.org/wiki/Leapfrog_integration), a common technique for numerically solving second order differential equations. With this technique, evolutions occur in half-steps between the spatial and momentum representations of the wave function, in order to ensure that energy is conserved and the trajectory is calculated with limited numerical error. Transformations between representations are accomplished by a [Fast Fourier Transform (FFT)](https://en.wikipedia.org/wiki/Fast_Fourier_transform) of the image/wavefunction data. After the calculations are completed for the specified number of time steps, the probability density's evolution is plotted and saved as an animation.

The main script also runs with the ``-sq`` parameter, which allows the user to see what the image data looks like when evolved with the regular schrodinger equation in a zero-potential system devoid of any self-interaction terms.

## Dependencies
- numpy-1.22.3
- scikit-learn-1.0.2
- PIL-9.0.1
- matplotlib-3.5.1

## Usage
Place the image file in the same directory as the ``main.py`` script and run the following command:
```
python main.py <filename>
```
To produce the output of a regular square-well potential without the self interaction term, i.e. the solution to the canonical schrodinger equation, run the script with the ``-sq`` parameter:
```
python main.py -sq <filename>
```

### Example Output (Schrodinger-Poisson)
The probability density quickly coalesces around the regions of high amplitude due to the system's self-gravitation, while fringe components propagate outward. This system is, expectedly, far more dynamic than the typical square-well system.
<p align="center">
  <img src="https://github.com/rp-mullen/quantum-image-evolver/blob/main/output.gif"/>
</p>

### Example Output (Square Well)
Slow dispersion of clustered amplitudes and overlapping interference of the evolving probability density are the defining features of the gravitation-less square well system.
<p align="center">
  <img src="https://github.com/rp-mullen/schrodinger-poisson-evolver/blob/main/square_well_output.gif"/>
</p>
