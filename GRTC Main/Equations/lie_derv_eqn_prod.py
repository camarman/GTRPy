################### PRODUCING EQUATIONS OF LIE DERIVATIVE ###################


from sympy import latex

from Operations.lie_derv import *


def ld_scalar_field_eqn_producer(coord_sys, X, scalar_field):
    """
    Producing equations of lie derivative of scalar field for a given vector field, X.

    Args:
        coord_sys [list]: The coordinate system (cartesian, spherical, etc.).
        X [list]: Given vector field.
        scalar_field [sympy.symbol]: Given scalar field.
    """
    ld_eqn = latex(ld_scalar_field(coord_sys, X, scalar_field))
    return '$$\mathcal{{L}}_X\phi = {0}$$'.format(ld_eqn)


def ld_vector_field_eqn_producer(coord_sys, X, vector_field, vector_field_type):
    """
    Producing equations of lie derivative of vector field for a given vector field, X.

    Args:
        coord_sys [list]: The coordinate system (cartesian, spherical, etc.).
        X [list]: Given vector field.
        vector_field [list]: Given vector field.
        vector_field_type [str]: Type of the vector field. It should be given
        in terms of 'u': contravariant (upper-indices) and 'd': covariant (lower-indices).
    """
    if vector_field_type == 'u':
        ld_eqn = latex(ld_vector_field(coord_sys, X, vector_field, vector_field_type))
        return '$$\mathcal{{L}}_XV^{{\\alpha}} = {0}$$'.format(ld_eqn)
    
    elif vector_field_type == 'd':
        ld_eqn = latex(ld_vector_field(coord_sys, X, vector_field, vector_field_type))
        return '$$\mathcal{{L}}_XV_{{\\alpha}} = {0}$$'.format(ld_eqn)
    
    
def ld_tensor_field_eqn_producer(coord_sys, X, tensor_field, tensor_field_type):
    """
    Producing equations of lie derivative of tensor field for a given vector field, X.

    Args:
        coord_sys [list]: The coordinate system (cartesian, spherical, etc.).
        X [list]: Given vector field.
        tensor_field [list]: Given tensor field.
        tensor_field_type [str]: Type of the tensor field. It should be given
        in terms of 'u': contravariant (upper-indices) and 'd': covariant (lower-indices).
    """
    if tensor_field_type == 'uu':
        ld_eqn = latex(ld_tensor_field(coord_sys, X, tensor_field, tensor_field_type))
        return '$$\mathcal{{L}}_XT^{{\\alpha\\beta}} = {0}$$'.format(ld_eqn)
    
    elif tensor_field_type == 'ud':
        ld_eqn = latex(ld_tensor_field(coord_sys, X, tensor_field, tensor_field_type))
        return '$$\mathcal{{L}}_XT^{{\\alpha}}_{{\\beta}} = {0}$$'.format(ld_eqn)
    
    elif tensor_field_type == 'dd':
        ld_eqn = latex(ld_tensor_field(coord_sys, X, tensor_field, tensor_field_type))
        return '$$\mathcal{{L}}_XT_{{\\alpha \\beta}}  = {0}$$'.format(ld_eqn)
        
############################################################################