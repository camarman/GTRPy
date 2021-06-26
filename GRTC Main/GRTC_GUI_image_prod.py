################### GRTC GUI - PRODUCING IMAGES ###################


from PIL import Image
from sympy import preview


tensor2d = ['Metric Tensor', 'Inverse Metric Tensor', 'Ricci Tensor', 'Traceless Ricci Tensor', 'Einstein Tensor']
tensor4d = ['Riemann Tensor', 'Weyl Tensor']
scalars = ['Ricci Scalar', 'Kretschmann Scalar']


def re_size_tensor(tensor, tensor_type = ''):
    """
    Re-sizing the image of a tensor.

    Args:
        tensor [str]: The name of the tensor given as a string.
        tensor_type [str]: Type of the tensor. Given in terms of 'u': contravariant and 'd': covariant.
    """
    im = Image.open(r'GUI Tensor Images\tensor.png')
    if tensor == 'Metric Tensor' and tensor_type == 'ud': # for some reason this tensor looks bigger
        size = (300, 300)
    elif tensor in tensor2d:
        size = (500, 500)
    elif tensor == 'Christoffel Symbol':
        size = (1200, 600)
    elif tensor in tensor4d:
        size = (600, 600)
    elif tensor in scalars:
        size = (500, 500)
    im.thumbnail(size, Image.ANTIALIAS)
    out_dim = im.size
    out_name = r'GUI Tensor Images\tensor.png'
    im.save(out_name, "PNG")
    im.close()


def re_size_tensor_component():
    """
    Re-sizing the image of the tensor components.
    """
    im = Image.open(r'GUI Tensor Images\tensor_component.png')
    size = (200, 200)
    im.thumbnail(size, Image.ANTIALIAS)
    out_dim = im.size
    out_name = r'GUI Tensor Images\tensor_component.png'
    im.save(out_name, "PNG")
    im.close()


def re_size_cd(desired_cd_object):
    """
    Re-sizing the image of covariant derivative tensor.
    
    Args:
        desired_cd_object [str]: The type of the field (scalar, vector, tensorial) choosen by the user.
    """
    if desired_cd_object == 'Scalar Field':
        im = Image.open(r'GUI Tensor Images\cd_scalar_field.png')
        size = (500, 500)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'GUI Tensor Images\cd_scalar_field.png'
    elif desired_cd_object == 'Type (1,0) Vector Field':
        im = Image.open(r'GUI Tensor Images\cd_vector_field_10.png')
        size = (600, 600)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'GUI Tensor Images\cd_vector_field_10.png'
    elif desired_cd_object == 'Type (0,1) Vector Field':
        im = Image.open(r'GUI Tensor Images\cd_vector_field_01.png')
        size = (600, 600)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'GUI Tensor Images\cd_vector_field_01.png'
    elif desired_cd_object == 'Type (2,0) Tensor Field':
        im = Image.open(r'GUI Tensor Images\cd_tensor_field_20.png')
        size = (700, 700)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'GUI Tensor Images\cd_tensor_field_20.png'
    elif desired_cd_object == 'Type (1,1) Tensor Field':
        im = Image.open(r'GUI Tensor Images\cd_tensor_field_11.png')
        size = (700, 700)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'GUI Tensor Images\cd_tensor_field_11.png'
    elif desired_cd_object == 'Type (0,2) Tensor Field':
        im = Image.open(r'GUI Tensor Images\cd_tensor_field_02.png')
        size = (700, 700)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'GUI Tensor Images\cd_tensor_field_02.png'
    im.save(out_name, "PNG")
    im.close()


def produce_image_tensor(tensor_equation, tensor_component_equation, desired_tensor, desired_tensor_type=''):
    """
    Producing the images and re-sizing them after the user chooses another tensor or tensor component.

    Args:
        tensor_equation [str]: The latex form of the tensor.
        tensor_component_equation [str]: The latex form of the component of a given tensor.
        desired_tensor [str]: Tensor chosen by the user
        desired_tensor_type [str, optional]: The type of the desired tensor.
    """
    if desired_tensor_type == '':
        preview(tensor_equation, viewer='file', filename=r'GUI Tensor Images\tensor.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
        preview(tensor_component_equation, viewer='file', filename=r'GUI Tensor Images\tensor_component.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
        re_size_tensor(desired_tensor)
        re_size_tensor_component()
    else:
        preview(tensor_equation, viewer='file', filename=r'GUI Tensor Images\tensor.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
        preview(tensor_component_equation, viewer='file', filename=r'GUI Tensor Images\tensor_component.png', euler=False,
                dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
        re_size_tensor(desired_tensor, desired_tensor_type)
        re_size_tensor_component()

############################################################################
