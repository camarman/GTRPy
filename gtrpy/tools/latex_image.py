# Producing images of the equations in the LaTeX form
# to be used in the `gtrpy/res` directory

from PIL import Image
from sympy import preview


# equation in the LaTeX form
equation = r'$$\Sigma m_{{\nu}} = 0$$'

# storing the image
preview(equation, viewer='file', filename='masslessnu.png', euler=False,
        dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 600', '-bg', 'Transparent'])

# re-size the image if needed
im = Image.open('masslessnu.png')
size = (200, 200)
im.thumbnail(size, Image.ANTIALIAS)
out_dim = im.size
out_name = 'masslessnu.png'
im.save(out_name, "PNG")
im.close()
