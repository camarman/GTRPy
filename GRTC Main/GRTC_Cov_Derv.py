################### GRTC - COVARIANT DERIVATIVE ###################


from GRTC_Tensor import *


def cd_scalar_field(coord_sys, scalar_field, index):
    """
    The covariant derivative of a scalar field for a given index.

    Args:
        coord_sys [list]: The coordinate system (cartesian, spherical, etc.).
        scalar_field [sympy.symbol]: Given scalar field.
        index [int]: The index of the coordinate system given as an integer; (0-4).
    """
    return Simplify(diff(scalar_field, coord_sys[index]))


def cd_vector_field(diag_comp, coord_sys, vector_field, vector_field_type, index):
    """
    The covariant derivative of a vector field for a given type and index.

    Args:
        diag_comp [list]: Diagonal components of the metric tensor.
        coord_sys [list]: The coordinate system (cartesian, spherical, etc.).
        vector_field [list]: Given vector field.
        vector_field_type [str]: Type of the vector field. It should be given
        in terms of 'u': contravariant (upper-indices) and 'd': covariant (lower-indices).
        index [int]: The index of the coordinate system given as an integer; (0-4).
    """
    cs = ChristoffelSymbol(diag_comp, coord_sys)
    chris_symbol = cs.get_christoffelsymbol()
    covariant_tensor = []
    if vector_field_type == 'u':
        for a in range(4):
            V_partial = diff(vector_field[a], coord_sys[index])
            einsum = 0
            for b in range(4):
                einsum += chris_symbol[a, index, b]*vector_field[b]
            cov_V = V_partial + einsum
            covariant_tensor.append(cov_V)
            
    elif vector_field_type == 'd':
        for a in range(4):
            V_partial = diff(vector_field[a], coord_sys[index])
            einsum = 0
            for b in range(4):
                einsum += chris_symbol[b, index, a]*vector_field[b]
            cov_V = V_partial - einsum
            covariant_tensor.append(cov_V)
    return Simplify(Array(covariant_tensor))


def cd_tensor_field(diag_comp, coord_sys, tensor_field, tensor_field_type, index):
    """
    The covariant derivative of a tensor field for a given type and index.

    Args:
        diag_comp [list]: Diagonal components of the metric tensor.
        coord_sys [list]: The coordinate system (cartesian, spherical, etc.).
        tensor_field [list]: Given tensor field.
        tensor_field_type [str]: Type of the tensor field. It should be given
        in terms of 'u': contravariant (upper-indices) and 'd': covariant (lower-indices).
        index [int]: The index of the coordinate system given as an integer; (0-4).
    """
    cs = ChristoffelSymbol(diag_comp, coord_sys)
    chris_symbol = cs.get_christoffelsymbol()
    covariant_tensor = MutableDenseNDimArray(zeros((4,)*2))
    if tensor_field_type == 'uu':
        for a, b in product(range(4), repeat=2):
            T_partial = diff(tensor_field[a][b], coord_sys[index])
            einsum_1, einsum_2 = 0, 0
            for d in range(4):
                einsum_1 += chris_symbol[a, index, d]*tensor_field[d][b]
                einsum_2 += chris_symbol[b, index, d]*tensor_field[a][d]
            cov_T = T_partial + einsum_1 + einsum_2
            covariant_tensor[a, b] = cov_T
            
    elif tensor_field_type == 'ud':
        for a, b in product(range(4), repeat=2):
            T_partial = diff(tensor_field[a][b], coord_sys[index])
            einsum_1, einsum_2 = 0, 0
            for d in range(4):
                einsum_1 += chris_symbol[a, index, d]*tensor_field[d][b]
                einsum_2 += chris_symbol[d, index, b]*tensor_field[a][d]
            cov_T = T_partial + einsum_1 - einsum_2
            covariant_tensor[a, b] = cov_T
            
    elif tensor_field_type == 'dd':
        for a, b in product(range(4), repeat=2):
            T_partial = diff(tensor_field[a][b], coord_sys[index])
            einsum_1, einsum_2 = 0, 0
            for d in range(4):
                einsum_1 += chris_symbol[d, index, a]*tensor_field[d][b]
                einsum_2 += chris_symbol[d, index, b]*tensor_field[a][d]
            cov_T = T_partial - einsum_1 - einsum_2
            covariant_tensor[a, b] = cov_T
    return Simplify(covariant_tensor)

############################################################################