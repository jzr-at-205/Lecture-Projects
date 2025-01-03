"""
Begin by creating a 2-dimensional array of integers of dimension m * n, 
called an iteration_arr.  Using an if statement - if(complex_arr[i][j] belongs to 
the Mandelbrot set), iteration_arr[i][j] = 0.  Otherwise, iteration_arr[i][j] = number of
iterations. 

"""
# import the libraries nessary for the program
from PIL import Image
from numpy import complex, array
import colorsys

# the width of the output image is set to 1024
WIDTH = 1024

# set a function to return a tuple of colors as rgb values
def rgb_conv(i):
    color = 255 * array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5))
    return tuple(color.astype(int))

# now a function defining Mandelbrot
def mandelbrot(x, y):
    c0 = complex(x, y)
    c = 0
    for i in range(1, 1000):
        if abs(c) > 2:
            return rgb_conv(i)
        c = c * c + c0
    return (0, 0, 0)

# following, create an image with the rgb values
img = Image.new('RGB', (WIDTH, int(WIDTH / 2)))
pixels = img.load()

for x in range(img.size[0]):
    print("%.2f %%" % (x / WIDTH * 100.0))
    for y in range(img.size[1]):
        pixels[x, y] = mandelbrot((x - (0.75 * WIDTH)) / (WIDTH / 4), (y - (WIDTH / 4)) / (WIDTH / 4))

def main():
    print("Hello World!")
    print("This is a Fractal Display")  
    img.show()


if __name__ == "__main__":
    main()