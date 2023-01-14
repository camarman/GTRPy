from sympy import nsimplify, simplify


def Simplify(xobject):
    """
    Simplifies the given tensor or field via simplify and nsimplify functions

    Args:
        xobject: Given tensor or field object

    Returns:
        Simplified version of the object
    """
    try:   # if all components of the tensor (or field) are 0, nsimplify raises error
        return simplify(nsimplify(xobject))
    except:
        return xobject
