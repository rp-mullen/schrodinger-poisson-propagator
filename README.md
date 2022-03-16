## Description:
2D Image data is taken as the initial state of a wavefunction and evolved under the action of its own self-influencing gravitational potential (see Poisson(https://en.wikipedia.org/wiki/Poisson%27s_equation)). Half-steps in xy-space occur between full shifts in k-space in order to propagate the wavefunction through one full time step. Transformations between the spatial and momentum bases are facillitated by an FFT/iFFT of the wave function data. 

```
python main.py
```

### Example Output:
<p align="center">
  <img src="https://github.com/rp-mullen/quantum-image-evolver/blob/main/output.gif"/>
</p>

