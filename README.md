## Description
2D Image data is plotted as the initial state of a quantum mechanical system, and is evolved under the influence of its own self-interacting [gravitational potential](https://en.wikipedia.org/wiki/Poisson%27s_equation). The nonlinear self-interaction term present in the Schrodinger-Poisson equation is a modification of standard quantum mechanics and was originally proposed as an explanation for the self-gravitation of hypothetical boson stars, and later as an explanation for wavefunction collapse. Modeling quantum systems with the Schrodinger-Poisson equation finds real-world applications in the study of both [Bose-Einstein condensates](https://en.wikipedia.org/wiki/Bose%E2%80%93Einstein_condensate) and ["fuzzy" dark matter](https://en.wikipedia.org/wiki/Fuzzy_cold_dark_matter). 

Further Reading: [Schrödinger–Poisson Equation](https://en.wikipedia.org/wiki/Schr%C3%B6dinger%E2%80%93Newton_equation#:~:text=The%20Schr%C3%B6dinger%E2%80%93Newton%20equation%2C%20sometimes,function%20as%20a%20mass%20density%2C)

Half-steps in xy-space occur in a leapfrog fashion between full shifts in k-space in order to propagate the wavefunction through one full time step with minimal numerical error. Transformations between the spatial and momentum bases are facillitated by an FFT/iFFT of the wave function data. The probability density is plotted and saved as an animation.

This repo also contains the ``square_well.py`` script, which allows the user to see what the image data looks like when evolved with the regular schrodinger equation in a zero-potential system devoid of any self-interaction terms. 

## Dependencies
- numpy
- scikit-learn
- Pillow

## Usage
Place the image file in the same directory as the ``main.py`` script and run the following command:
```
python main.py <filename>
```
To produce the output of a "normal" square-well potential without the self interaction term, i.e. the solution to the canonical schrodinger equation, run:
```
python square_well.py <filename>
```

### Example Output:
<p align="center">
  <img src="https://github.com/rp-mullen/quantum-image-evolver/blob/main/output.gif"/>
</p>

