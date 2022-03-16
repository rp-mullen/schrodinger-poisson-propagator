## Description:
Image data is cast as an NxN numpy array and evolved as a wavefunction in a system where the image itself serves as its own self-influencing gravitational Poisson potential. Half-steps in xy-space occur between full shifts in k-space in order to propagate the wavefunction through one full time step. Transformations between the spatial and momentum bases are facillitated by an FFT/iFFT of the wave function data. 

```
python main.py
```

### Example Output:
<p align="center">
  <img src="https://github.com/rp-mullen/quantum-image-evolver/blob/main/output.gif"/>
</p>

