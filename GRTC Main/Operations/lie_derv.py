################### GRTC - LIE DERIVATIVE ###################


from Operations.GR_tensors import *


def ld_scalar_field(coord_sys, X, scalar_field):
    """
    The Lie Derivative of a scalar field with respect to a vector field, X.
    
    Args:
        coord_sys [list]: The coordinate system (cartesian, spherical, etc.).
        X [list]: Given vector field.
        scalar_field [sympy.symbol]: Given scalar field.
    """
    ndim = len(coord_sys)
    LX_phi = 0
    for c in range(ndim):
        LX_phi += X[c]*diff(scalar_field, coord_sys[c])
    return Simplify(LX_phi)
    
    
def ld_vector_field(coord_sys, X, vector_field, vector_field_type):
    """
    The Lie derivative of a vector field with respect to another vector field, X.

    Args:
        coord_sys [list]: The coordinate system (cartesian, spherical, etc.).
        X [list]: Given vector field.
        vector_field [list]: Given vector field.
        vector_field_type [str]: Type of the vector field. It should be given
        in terms of 'u': contravariant (upper-indices) and 'd': covariant (lower-indices).
    """
    ndim = len(coord_sys)
    LX_V = []
    if vector_field_type == 'u':
        for a in range(ndim):
            ld_V = 0
            for c in range(ndim):
                ld_V += X[c]*diff(vector_field[a], coord_sys[c]) - vector_field[c]*diff(X[a], coord_sys[c])
            LX_V.append(ld_V)
    
    elif vector_field_type == 'd':
        for a in range(ndim):
            ld_V = 0
            for c in range(ndim):
                ld_V += X[c]*diff(vector_field[a], coord_sys[c]) + vector_field[c]*diff(X[c], coord_sys[a])
            LX_V.append(ld_V)
    return Simplify(Array(LX_V))


def ld_tensor_field(coord_sys, X, tensor_field, tensor_field_type):
    """
    The Lie derivative of a tensor field with respect to another vector field, X.

    Args:
        coord_sys [list]: The coordinate system (cartesian, spherical, etc.).
        X [list]: Given vector field.
        tensor_field [list]: Given tensor field.
        tensor_field_type [str]: Type of the tensor field. It should be given
        in terms of 'u': contravariant (upper-indices) and 'd': covariant (lower-indices).
    """
    ndim = len(coord_sys)
    LX_T = MutableDenseNDimArray(zeros((ndim,)*2))
    if tensor_field_type == 'uu':
        for a, b in product(range(ndim), repeat=2):
            einsum = 0
            for c in range(ndim):
                S1 = X[c]*diff(tensor_field[a][b], coord_sys[c])
                S2 = tensor_field[c][b]*diff(X[a], coord_sys[c])
                S3 = tensor_field[a][c]*diff(X[b], coord_sys[c])
                einsum += S1 - S2 - S3
            LX_T[a,b] = einsum
            
    elif tensor_field_type == 'ud':
        for a, b in product(range(ndim), repeat=2):
            einsum = 0
            for c in range(ndim):
                S1 = X[c]*diff(tensor_field[a][b], coord_sys[c])
                S2 = tensor_field[c][b]*diff(X[a], coord_sys[c])
                S3 = tensor_field[a][c]*diff(X[c], coord_sys[b])
                einsum += S1 - S2 + S3
            LX_T[a,b] = einsum
            
    elif tensor_field_type == 'dd':
        for a, b in product(range(ndim), repeat=2):
            einsum = 0
            for c in range(ndim):
                S1 = X[c]*diff(tensor_field[a][b], coord_sys[c])
                S2 = tensor_field[c][b]*diff(X[c], coord_sys[a])
                S3 = tensor_field[a][c]*diff(X[c], coord_sys[b])
                einsum += S1 + S2 + S3
            LX_T[a,b] = einsum
    return Simplify(LX_T)
        
############################################################################