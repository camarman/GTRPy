# ========== PRODUCING EQUATIONS FOR SCALAR FIELDS ==========
from sympy import latex

from gtrpy.src.fields.scalarfield import ScalarField


def cd_scalarfield_ep(coord_sys, scalar_field, index_symbol):
    """
    Producing equations of covariant derivative for a scalar field

    Args:
        coord_sys    [list]        : The coordinate system given as a list (e.g., [t,x,y,z])
        scalar_field [sympy.symbol]: The scalar field, provided by the user
        index_symbol [sympy.symbol]: The index of the coordinate system given as a symbol (e.g., t, r, theta or phi)
    """
    sf = ScalarField(coord_sys, scalar_field)
    index_int = coord_sys.index(index_symbol)
    cd_component = latex(index_symbol)
    cd_eqn = latex(sf.cal_covariant_derivative(index_int))
    return '$$\\nabla_{{{0}}}\phi = {1}$$'.format(cd_component, cd_eqn)


def ld_scalarfield_ep(coord_sys, scalar_field, X):
    """
    Producing equations of Lie derivative of a scalar field with respect to a vector field, X

    Args:
        coord_sys    [list]        : The coordinate system given as a list (e.g., [t,x,y,z])
        scalar_field [sympy.symbol]: The scalar field, provided by the user
        X            [list]        : Given vector field that the Lie derivative is taken w.r.t
    """
    sf = ScalarField(coord_sys, scalar_field)
    ld_eqn = latex(sf.cal_lie_derivative(X))
    return '$$\mathcal{{L}}_X\phi = {0}$$'.format(ld_eqn)
