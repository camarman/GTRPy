# Some important functions for image processing


from PIL import Image
from sympy import preview


# Classifying some of the tensors that will be used with the tensor types
tensor2d = ['Metric Tensor', 'Ricci Tensor', 'Traceless Ricci Tensor', 'Einstein Tensor']
scalars = ['Ricci Scalar', 'Kretschmann Scalar']


def re_size(xtensor_name, xtensor_type = ''):
    """
    Re-sizing the image of a tensor

    Args:
        xtensor_name [str]: The name of the desired tensor given as a string
        xtensor_type [str]: Type of the tensor. Given in terms of 'u': contravariant and 'd': covariant
    """
    im = Image.open('tensor.png')
    if xtensor_name == 'Metric Tensor' and xtensor_type == 'ud': # for some reason this tensor looks bigger
        size = (300, 300)
    elif xtensor_name in tensor2d or xtensor_name == 'Inverse Metric Tensor':
        size = (500, 500)
    elif xtensor_name == 'Christoffel Symbol':
        size = (1200, 600)
    elif xtensor_name == 'Riemann Tensor' or xtensor_name == 'Weyl Tensor':
        size = (600, 600)
    elif xtensor_name in scalars:
        size = (500, 500)
    im.thumbnail(size, Image.ANTIALIAS)
    out_dim = im.size
    out_name = 'tensor.png'
    im.save(out_name, "PNG")
    im.close()


def re_size_component():
    """
    Re-sizing the image of the tensor components
    """
    im = Image.open('tensor_component.png')
    size = (200, 200)
    im.thumbnail(size, Image.ANTIALIAS)
    out_dim = im.size
    out_name = 'tensor_component.png'
    im.save(out_name, "PNG")
    im.close()


def produce_image(tensor_equation, tensor_component_equation, desired_tensor, desired_tensor_type='' ):
    """
    Producing the Images and re-sizing them after the user chooses another tensor or tensor component

    Args:
        tensor_equation [str]: The latex form of the tensor
        tensor_component_equation [str]: The latex form of the component of a given tensor
        desired_tensor [str]: [description]
        desired_tensor_type [str, optional]: Type of the tensor. Defaults to ''.
    """
    if desired_tensor_type == '':
        preview(tensor_equation, viewer='file', filename='tensor.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 600', '-bg', 'Transparent'])
        preview(tensor_component_equation, viewer='file', filename='tensor_component.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 600', '-bg', 'Transparent'])
        re_size(desired_tensor)
        re_size_component()
    else:
        preview(tensor_equation, viewer='file', filename='tensor.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 600', '-bg', 'Transparent'])
        preview(tensor_component_equation, viewer='file', filename='tensor_component.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 600', '-bg', 'Transparent'])
        re_size(desired_tensor, desired_tensor_type)
        re_size_component()
    
