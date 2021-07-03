################### GUI - IMAGE RESIZER ###################


from PIL import Image
from sympy import preview


tensor2d = [
            'Metric Tensor', 'Inverse Metric Tensor', 'Ricci Tensor', 
            'Traceless Ricci Tensor', 'Einstein Tensor'
            ]

tensor4d = ['Riemann Tensor', 'Weyl Tensor']
scalars = ['Ricci Scalar', 'Kretschmann Scalar']


def re_size_tensor_image(tensor, tensor_type = ''):
    """
    Re-sizing the image of a tensor.

    Args:
        tensor [str]: The name of the tensor given as a string.
        tensor_type [str]: Type of the tensor. Given in terms of 'u': contravariant and 'd': covariant.
    """
    im = Image.open(r'Display\Output Images\tensor.png')
    if tensor == 'Metric Tensor' and tensor_type == 'ud': # for some reason this tensor looks bigger
        size = (400, 400)
    
    elif tensor in tensor2d:
        size = (500, 500)
    
    elif tensor == 'Christoffel Symbol':
        size = (1200, 650)
    
    elif tensor in tensor4d:
        size = (900, 450)
   
    elif tensor in scalars:
        size = (500, 500)
    im.thumbnail(size, Image.ANTIALIAS)
    out_dim = im.size
    out_name = r'Display\Output Images\tensor.png'
    im.save(out_name, "PNG")
    im.close()


def re_size_tensor_component_image():
    """
    Re-sizing the image of the tensor components.
    """
    im = Image.open(r'Display\Output Images\tensor_component.png')
    size = (200, 200)
    im.thumbnail(size, Image.ANTIALIAS)
    out_dim = im.size
    out_name = r'Display\Output Images\tensor_component.png'
    im.save(out_name, "PNG")
    im.close()


def re_size_cd_image(desired_cd_object):
    """
    Re-sizing the image of covariant derivative tensor.
    
    Args:
        desired_cd_object [str]: The type of the field (scalar, vector, tensorial) 
        choosen by the user.
    """
    if desired_cd_object == 'Scalar Field':
        im = Image.open(r'Display\Output Images\cd_scalar_field.png')
        size = (500, 500)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'Display\Output Images\cd_scalar_field.png'
    
    elif desired_cd_object == 'Type (1,0) Vector Field':
        im = Image.open(r'Display\Output Images\cd_vector_field_10.png')
        size = (800, 600)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'Display\Output Images\cd_vector_field_10.png'
    
    elif desired_cd_object == 'Type (0,1) Vector Field':
        im = Image.open(r'Display\Output Images\cd_vector_field_01.png')
        size = (800, 600)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'Display\Output Images\cd_vector_field_01.png'
    
    elif desired_cd_object == 'Type (2,0) Tensor Field':
        im = Image.open(r'Display\Output Images\cd_tensor_field_20.png')
        size = (1200, 650)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'Display\Output Images\cd_tensor_field_20.png'
    
    elif desired_cd_object == 'Type (1,1) Tensor Field':
        im = Image.open(r'Display\Output Images\cd_tensor_field_11.png')
        size = (1200, 650)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'Display\Output Images\cd_tensor_field_11.png'
    
    elif desired_cd_object == 'Type (0,2) Tensor Field':
        im = Image.open(r'Display\Output Images\cd_tensor_field_02.png')
        size = (1200, 650)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'Display\Output Images\cd_tensor_field_02.png'
    im.save(out_name, "PNG")
    im.close()


def re_size_ld_image(desired_ld_object):
    """
    Re-sizing the image of the lie derivative.
    
    Args:
        desired_ld_object [str]: The type of the field (scalar, vector, tensorial) 
        choosen by the user.
    """
    if desired_ld_object == 'Scalar Field':
        im = Image.open(r'Display\Output Images\ld_scalar_field.png')
        size = (500, 500)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'Display\Output Images\ld_scalar_field.png'
    
    elif desired_ld_object == 'Type (1,0) Vector Field':
        im = Image.open(r'Display\Output Images\ld_vector_field_10.png')
        size = (800, 600)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'Display\Output Images\ld_vector_field_10.png'
    
    elif desired_ld_object == 'Type (0,1) Vector Field':
        im = Image.open(r'Display\Output Images\ld_vector_field_01.png')
        size = (800, 600)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'Display\Output Images\ld_vector_field_01.png'
    
    elif desired_ld_object == 'Type (2,0) Tensor Field':
        im = Image.open(r'Display\Output Images\ld_tensor_field_20.png')
        size = (1200, 650)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'Display\Output Images\ld_tensor_field_20.png'
    
    elif desired_ld_object == 'Type (1,1) Tensor Field':
        im = Image.open(r'Display\Output Images\ld_tensor_field_11.png')
        size = (1200, 650)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'Display\Output Images\ld_tensor_field_11.png'
    
    elif desired_ld_object == 'Type (0,2) Tensor Field':
        im = Image.open(r'Display\Output Images\ld_tensor_field_02.png')
        size = (1200, 650)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'Display\Output Images\ld_tensor_field_02.png'
    im.save(out_name, "PNG")
    im.close()
    
############################################################################