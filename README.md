# Approximation-of-pi

Two probabilistic approaches to compute the approximated value of Pi:


## Monte Carlo:

It is a straight forward technique: dots are projected to a designation of a circle inscribed in a square meaning that radius = half the square side length. Some of the dots are projected in the circle domain and the rest in the complement area.

If we calculated the ratio of the two areas we see that:


<p align="center">
  <img width="250" height="70" src="https://latex.codecogs.com/png.latex?%5Cbg_white%20%5Chuge%20%5Cfrac%7Barea%5C%3Bof%20%5C%3Bcircle%20%7D%20%7Barea%20%5C%3Bof%20%5C%3Bsquare%7D%20%3D%20%5Cfrac%7B4r%5E2%7D%7B%5Cpi%20r%5E2%7D">
</p>



that would be the same if we do this 

<p align="center">
  <img width="390" height="60" src="https://latex.codecogs.com/png.latex?%5Cbg_white%20%5CLARGE%20%5Cpi%20%3D%5Clim_%7Bx%5Cto%5Cinfty%7D%20%5Cfrac%7B%5C%23%20%5C%3Bof%20%5C%3Bdots%5C%3B%20within%20%5C%3Bcircle%7D%7Btotal%20%5C%3Bno.%5C%3B%20of%20%5C%3Bdots%28x%29%7D%20*%5C%3B4">
</p>


**The pygame simulation:**

<p align="center">
  <img width="450" height="450" src="https://user-images.githubusercontent.com/59314933/144127624-5dc805a0-520d-4d7b-9746-75dc96a3bd03.gif">
</p>


## Buffon Needles:

**The pygame simulation:**

<p align="center">
  <img width="450" height="250" src="https://user-images.githubusercontent.com/59314933/144129325-fe1e9d6c-6fea-46f7-876e-744295797fa7.gif">
</p>


