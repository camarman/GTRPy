################### PRODUCING EQUATIONS OF COVARIANT DERIVATIVE ###################


from sympy import latex

from Operations.cov_derv import *


def cd_scalar_field_eqn_producer(coord_sys, scalar_field, index_symbol):
    """
    Producing equations of covariant derivative for a scalar field.

    Args:
        coord_sys [list]: The coordinate system (cartesian, spherical, etc.).
        scalar_field [sympy.symbol]: Given scalar field.
        index_symbol [symbol]: The index of the coordinate system given as symbol (i.e. t, r, theta, phi).
    """
    index_int = coord_sys.index(index_symbol) 
    cd_component = latex(index_symbol)
    cd_eqn = latex(cd_scalar_field(coord_sys, scalar_field, index_int))
    return '$$\\nabla_{{{0}}}\phi = {1}$$'.format(cd_component, cd_eqn)


def cd_vector_field_eqn_producer(diag_comp, coord_sys, vector_field, vector_field_type, index_symbol):
    """
    Producing equations of covariant derivative for a vector field.

    Args:
        diag_comp [list]: Diagonal components of the metric tensor.
        coord_sys [list]: The coordinate system (cartesian, spherical, etc.).
        vector_field [list]: Given vector field.
        vector_field_type [str]: Type of the vector field. It should be given
        in terms of 'u': contravariant (upper-indices) and 'd': covariant (lower-indices).
        index_symbol [symbol]: The index of the coordinate system given as symbol (i.e. t, r, theta, phi).
    """
    if vector_field_type == 'u':
        index_int = coord_sys.index(index_symbol)
        cd_component = latex(index_symbol)
        cd_eqn = latex(cd_vector_field(diag_comp, coord_sys, vector_field, vector_field_type, index_int))
        return '$$\\nabla_{{{0}}}V^{{\\alpha}} = {1}$$'.format(cd_component, cd_eqn)
    
    elif vector_field_type == 'd':
        index_int = coord_sys.index(index_symbol)
        cd_component = latex(index_symbol)
        cd_eqn = latex(cd_vector_field(diag_comp, coord_sys, vector_field, vector_field_type, index_int))
        return '$$\\nabla_{{{0}}}V_{{\\alpha}} = {1}$$'.format(cd_component, cd_eqn)
    

def cd_tensor_field_eqn_producer(diag_comp, coord_sys, tensor_field, tensor_field_type, index_symbol):
    """
    Producing equations of covariant derivative for a tensor field.

    Args:
        diag_comp [list]: Diagonal components of the metric tensor.
        coord_sys [list]: The coordinate system (cartesian, spherical, etc.).
        tensor_field [list]: Given tensor field.
        tensor_field_type [str]: Type of the tensor field. It should be given
        in terms of 'u': contravariant (upper-indices) and 'd': covariant (lower-indices).
        index_symbol [symbol]: The index of the coordinate system given as symbol (i.e. t, r, theta, phi).
    """
    if tensor_field_type == 'uu':
        index_int = coord_sys.index(index_symbol)
        cd_component = latex(index_symbol)
        cd_eqn = latex(cd_tensor_field(diag_comp, coord_sys, tensor_field, tensor_field_type, index_int))
        return '$$\\nabla_{{{0}}}T^{{\\alpha\\beta}} = {1}$$'.format(cd_component, cd_eqn)
    
    elif tensor_field_type == 'ud':
        index_int = coord_sys.index(index_symbol)
        cd_component = latex(index_symbol)
        cd_eqn = latex(cd_tensor_field(diag_comp, coord_sys, tensor_field, tensor_field_type, index_int))
        return '$$\\nabla_{{{0}}}T^{{\\alpha}}_{{\\beta}} = {1}$$'.format(cd_component, cd_eqn)
    
    elif tensor_field_type == 'dd':
        index_int = coord_sys.index(index_symbol)
        cd_component = latex(index_symbol)
        cd_eqn = latex(cd_tensor_field(diag_comp, coord_sys, tensor_field, tensor_field_type, index_int))
        return '$$\\nabla_{{{0}}}T_{{\\alpha \\beta}} = {1}$$'.format(cd_component, cd_eqn)
        
############################################################################