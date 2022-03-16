## Description
2D Image data is taken as the initial state of a quantum mechanical system, and is evolved under the action of its own self-influencing [gravitational potential](https://en.wikipedia.org/wiki/Poisson%27s_equation). The probability density is plotted and saved as an animation. Modeling quantum systems with the Poisson potential has real-world applications in the study of both [Bose-Einstein condensates](https://en.wikipedia.org/wiki/Bose%E2%80%93Einstein_condensate) and ultralight ["fuzzy" dark matter](https://en.wikipedia.org/wiki/Fuzzy_cold_dark_matter). 

Further reading: [Schrödinger–Poisson Equation(https://en.wikipedia.org/wiki/Schr%C3%B6dinger%E2%80%93Newton_equation#:~:text=The%20Schr%C3%B6dinger%E2%80%93Newton%20equation%2C%20sometimes,function%20as%20a%20mass%20density%2C

Half-steps in xy-space occur between full shifts in k-space in order to propagate the wavefunction through one full time step with minimal numerical error. Transformations between the spatial and momentum bases are facillitated by an FFT/iFFT of the wave function data.


## Usage
Place the image file in the same directory as the script and run the following command:
```
python main.py <filename>
```

### Example Output:
<p align="center">
  <img src="https://github.com/rp-mullen/quantum-image-evolver/blob/main/output.gif"/>
</p>

