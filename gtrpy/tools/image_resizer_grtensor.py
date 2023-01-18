from PIL import Image


def resize_tensor_image(tensor_object, tensor_type=''):
    """
    Re-sizing the image of a tensor

    Args:
        tensor_object [str]: The name of the grtensor object (metric tensor, Riemann tensor, etc.)
        tensor_type   [str]: The type of the tensor. Given in terms of
                             'u': contravariant
                             'd': covariant
    """
    im = Image.open(r'logs/tensor.png')
    if tensor_object == 'Metric Tensor' and tensor_type == 'ud':
        size = (400, 400)

    elif tensor_object == 'Metric Tensor':
        size = (500, 500)

    elif tensor_object == 'Inverse Metric Tensor':
        size = (500, 500)

    elif tensor_object == 'Christoffel Symbol':
        size = (1200, 650)

    elif tensor_object == 'Riemann Tensor':
        size = (900, 450)

    elif tensor_object == 'Ricci Tensor':
        size = (500, 500)

    elif tensor_object == 'Ricci Scalar':
        size = (500, 500)

    elif tensor_object == 'Traceless Ricci Tensor':
        size = (500, 500)

    elif tensor_object == 'Weyl Tensor':
        size = (900, 450)

    elif tensor_object == 'Einstein Tensor':
        size = (500, 500)

    elif tensor_object == 'Kretschmann Scalar':
        size = (500, 500)
    im.thumbnail(size, Image.ANTIALIAS)
    out_dim = im.size
    out_name = r'logs/tensor.png'
    im.save(out_name, "PNG")
    im.close()


def resize_tensor_component_image():
    """
    Re-sizing the image of a tensor component
    """
    im = Image.open(r'logs/tensor_component.png')
    size = (200, 200)
    im.thumbnail(size, Image.ANTIALIAS)
    out_dim = im.size
    out_name = r'logs/tensor_component.png'
    im.save(out_name, "PNG")
    im.close()
