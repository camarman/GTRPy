from PIL import Image


def resize_vry_image3d(field_object):
    """
    Re-sizing the image of the vector field, which we have varied the basis

    Args:
        field_object [str]: The name of the field object (vector or tensor)
    """
    if field_object == 'Type (1,0) Vector Field':
        im = Image.open(r'display3D/output images/vry_vector_field_10.png')
        size = (800, 600)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'display3D/output images/vry_vector_field_10.png'

    elif field_object == 'Type (0,1) Vector Field':
        im = Image.open(r'display3D/output images/vry_vector_field_01.png')
        size = (800, 600)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'display3D/output images/vry_vector_field_01.png'
    im.save(out_name, "PNG")
    im.close()


def resize_cd_image3d(field_object):
    """
    Re-sizing the image of covariant derivative for a given field object
    for the case of 3D

    Args:
        field_object [str]: The name of the field object (scalar, vector or tensor)
    """
    if field_object == 'Scalar Field':
        im = Image.open(r'display3D/output images/cd_scalar_field.png')
        size = (500, 500)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'display3D/output images/cd_scalar_field.png'

    elif field_object == 'Type (1,0) Vector Field':
        im = Image.open(r'display3D/output images/cd_vector_field_10.png')
        size = (800, 600)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'display3D/output images/cd_vector_field_10.png'

    elif field_object == 'Type (0,1) Vector Field':
        im = Image.open(r'display3D/output images/cd_vector_field_01.png')
        size = (800, 600)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'display3D/output images/cd_vector_field_01.png'

    elif field_object == 'Type (2,0) Tensor Field':
        im = Image.open(r'display3D/output images/cd_tensor_field_20.png')
        size = (1200, 650)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'display3D/output images/cd_tensor_field_20.png'

    elif field_object == 'Type (1,1) Tensor Field':
        im = Image.open(r'display3D/output images/cd_tensor_field_11.png')
        size = (1200, 650)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'display3D/output images/cd_tensor_field_11.png'

    elif field_object == 'Type (0,2) Tensor Field':
        im = Image.open(r'display3D/output images/cd_tensor_field_02.png')
        size = (1200, 650)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'display3D/output images/cd_tensor_field_02.png'
    im.save(out_name, "PNG")
    im.close()


def resize_ld_image3d(field_object):
    """
    Re-sizing the image of lie derivative for a given field object
    for the case of 3D

    Args:
        field_object [str]: The name of the field object (scalar, vector or tensor)
    """
    if field_object == 'Scalar Field':
        im = Image.open(r'display3D/output images/ld_scalar_field.png')
        size = (500, 500)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'display3D/output images/ld_scalar_field.png'

    elif field_object == 'Type (1,0) Vector Field':
        im = Image.open(r'display3D/output images/ld_vector_field_10.png')
        size = (800, 600)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'display3D/output images/ld_vector_field_10.png'

    elif field_object == 'Type (0,1) Vector Field':
        im = Image.open(r'display3D/output images/ld_vector_field_01.png')
        size = (800, 600)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'display3D/output images/ld_vector_field_01.png'

    elif field_object == 'Type (2,0) Tensor Field':
        im = Image.open(r'display3D/output images/ld_tensor_field_20.png')
        size = (1200, 650)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'display3D/output images/ld_tensor_field_20.png'

    elif field_object == 'Type (1,1) Tensor Field':
        im = Image.open(r'display3D/output images/ld_tensor_field_11.png')
        size = (1200, 650)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'display3D/output images/ld_tensor_field_11.png'

    elif field_object == 'Type (0,2) Tensor Field':
        im = Image.open(r'display3D/output images/ld_tensor_field_02.png')
        size = (1200, 650)
        im.thumbnail(size, Image.ANTIALIAS)
        out_dim = im.size
        out_name = r'display3D/output images/ld_tensor_field_02.png'
    im.save(out_name, "PNG")
    im.close()
