# Approximation-of-pi

Two probabilistic approaches to compute the approximated value of Pi:


## Monte Carlo:

It is a straight forward technique: dots are projected to a designation of a circle inscribed in a square meaning that radius = half the square side length. Some of the dots are projected in the circle domain and the rest in the complement area.

If we calculated the ratio of the two areas we see that:


<!---
<p align="center">
  <img width="220" height="60" src="https://latex.codecogs.com/png.latex?%5Cbg_white%20%5Chuge%20P%20%3D%5Cfrac%7Barea%20%5C%3Bof%20%5C%3Bcircle%7D%7Barea%20%5C%3Bof%20%5C%3Bsquare%7D%20%3D%5Cfrac%7B%5Cpi%20r%5E2%7D%7B4r%5E2%7D">
</p>
-->

$$P=\frac{area.of.circle}{area.of.square}=\frac{\pi r^2}{4r^2}$$


that would be the same if we do this 
<!---
<p align="center">
  <img width="390" height="60" src="https://latex.codecogs.com/png.latex?%5Cbg_white%20%5CLARGE%20%5Cpi%20%3D%5Clim_%7Bx%5Cto%5Cinfty%7D%20%5Cfrac%7B%5C%23%20%5C%3Bof%20%5C%3Bdots%5C%3B%20within%20%5C%3Bcircle%7D%7Btotal%20%5C%3Bno.%5C%3B%20of%20%5C%3Bdots%28x%29%7D%20*%5C%3B4">
</p>
-->

$$\pi = \lim_{n\to\infty} \frac{no.of. dots .in .circle}{total} \times 4$$
**The pygame simulation:**

<p align="center">
  <img  src="https://user-images.githubusercontent.com/59314933/144127624-5dc805a0-520d-4d7b-9746-75dc96a3bd03.gif">
</p>

**output:**

`pi = 3.1415929203539825 , error = 8.49136787674061e-06`
## Buffon Needles:


That one is a bit tricky. You have some sticks , needles, or whatever you want to call them and you drop them on spaced no. of lines then with some trig manipulation and calculus you will end up with the results in the photo. 

<p align="center">
  <img src="https://user-images.githubusercontent.com/59314933/144304242-84d25287-f2a9-4d9f-ae2d-4de836cc579d.jpg">
</p>

However, we are going to consider the first case where length of the needle is less than the spacing distance.
<!---
<p align="center">
  <img width="300" height="50" src="https://latex.codecogs.com/png.latex?%5Cbg_white%20%5CLARGE%20%5Cpi%20%3D%5Clim_%7Bx%5Cto%5Cinfty%7D%20%5Cfrac%7B2*L%7D%7BD%7D%20*%5Cfrac%7Btotal%20%5C%3B%28x%29%7D%7Bhits%7D">
</p>
-->
$$\pi = \lim_{n\to\infty} \frac{2L}{D}*\frac{total}{hits}$$


**The pygame simulation:**
<p align="center">
  <img src="https://user-images.githubusercontent.com/59314933/144129325-fe1e9d6c-6fea-46f7-876e-744295797fa7.gif">
</p>

**output:**

`pi =  3.141588785046729 , error =  0.00012313955024344762`
