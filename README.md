## Description:
2D Image data is taken as the initial state of a quantum mechanical [wavefunction](https://en.wikipedia.org/wiki/Wave_function) and evolved under the action of its own [self-influencing gravitational potential](https://en.wikipedia.org/wiki/Poisson%27s_equation). The probability density is plotted and saved as an animation. Modeling quantum systems with the Poisson potential has real-world applications in the study of ultralight ["fuzzy" dark matter](https://en.wikipedia.org/wiki/Fuzzy_cold_dark_matter). 

Half-steps in xy-space occur between full shifts in k-space in order to propagate the wavefunction through one full time step with minimal numerical error. Transformations between the spatial and momentum bases are facillitated by an FFT/iFFT of the wave function data.

```
python main.py
```

### Example Output:
<p align="center">
  <img src="https://github.com/rp-mullen/quantum-image-evolver/blob/main/output.gif"/>
</p>

