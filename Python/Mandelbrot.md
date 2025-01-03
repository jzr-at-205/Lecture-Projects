# Mandelbrot Set plotted using Python
# Algorithm:

The following was provided by  [GeeksforGeeks](https://www.geeksforgeeks.org) :

```c = complexArray[i][j]
z = 0
bound-value = <some real number greater than 0>
iteration = 0
max-iterations = <some positive integer>
while(mod(z) < bound-value and iteration <= max-iterations){
    z := (z raised to power n) + c
    iteration += 1
}
if (iteration > max-iterations) :  iterationArray[i][j] = 0  [since c belongs to the multibrot set for n]
else : iterationArray[i][j] = iteration  [since c does not belong to the mandelbrot set for n]```

