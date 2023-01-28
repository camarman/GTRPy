# ========== PRODUCING EQUATIONS FOR VECTOR FIELDS ==========
from sympy import latex

from gtrpy.src.fields.vectorfield import VectorField


def vry_vectorfield10_ep(metric_tensor, coord_sys, vector_field):
    """
    Varying the type of the vector field from 'u' (contravariant) to 'd' (covariant)

    Args:
        metric_tensor [list]: The metric tensor, provided by the user
        coord_sys     [list]: The coordinate system given as a list (e.g., [t,x,y,z])
        vector_field  [list]: The vector field, provided by the user
    """
    ndim = len(coord_sys)
    vf = VectorField(metric_tensor, coord_sys, vector_field, 'u')
    if ndim == 4:
        return '$$V_{{\\alpha}}={0}$$'.format(latex(vf.vary_vectorfield_type()))
    elif ndim == 3:
        return '$$V_{{a}}={0}$$'.format(latex(vf.vary_vectorfield_type()))


def cd_vectorfield10_ep(metric_tensor, coord_sys, vector_field, index_symbol):
    """
    Producing equations of covariant derivative for type (1,0) vector field

    Args:
        metric_tensor [list]        : The metric tensor, provided by the user
        coord_sys     [list]        : The coordinate system given as a list (e.g., [t,x,y,z])
        vector_field  [list]        : The vector field, provided by the user
        index_symbol  [sympy.symbol]: The index of the coordinate system given as a symbol (e.g., t, r, theta or phi)
    """
    ndim = len(coord_sys)
    vf = VectorField(metric_tensor, coord_sys, vector_field, 'u')
    index_int = coord_sys.index(index_symbol)
    cd_component = latex(index_symbol)
    cd_eqn = latex(vf.cal_covariant_derivative(index_int))
    if ndim == 4:
        return '$$\\nabla_{{{0}}}V^{{\\alpha}} = {1}$$'.format(cd_component, cd_eqn)
    elif ndim == 3:
        return '$$\\nabla_{{{0}}}V^{{a}} = {1}$$'.format(cd_component, cd_eqn)


def ld_vectorfield10_ep(metric_tensor, coord_sys, vector_field, X):
    """
    Producing equations of Lie derivative of type (1,0) vector field with respect to
    another vector field, X

    Args:
        metric_tensor [list]: The metric tensor, provided by the user
        coord_sys     [list]: The coordinate system given as a list (e.g., [t,x,y,z])
        vector_field  [list]: The vector field, provided by the user
        X             [list]: Given vector field that the Lie derivative is taken w.r.t
    """
    ndim = len(coord_sys)
    vf = VectorField(metric_tensor, coord_sys, vector_field, 'u')
    ld_eqn = latex(vf.cal_lie_derivative(X))
    if ndim == 4:
        return '$$\mathcal{{L}}_XV^{{\\alpha}} = {0}$$'.format(ld_eqn)
    elif ndim == 3:
        return '$$\mathcal{{L}}_XV^{{a}} = {0}$$'.format(ld_eqn)


def killingfield10_ep(metric_tensor, coord_sys, vector_field):
    """
    Producing equation of a Killing field for type (1,0) vector field

    Args:
        metric_tensor [list]: The metric tensor, provided by the user
        coord_sys     [list]: The coordinate system given as a list (e.g., [t,x,y,z])
        vector_field  [list]: The vector field, provided by the user
    """
    vf = VectorField(metric_tensor, coord_sys, vector_field, 'u')
    if vf.isKillingField(vector_field) == True:
        return '$$V^{{\\alpha}}={0}~\\text{{is a Killing field}}$$'.format(latex(vector_field))
    else:
        return '$$V^{{\\alpha}}={0}~\\text{{is not a Killing field}}$$'.format(latex(vector_field))


def vry_vectorfield01_ep(metric_tensor, coord_sys, vector_field):
    """
    Varying the type of the vector field from 'd' (covariant) to 'u' (contravariant)

    Args:
        metric_tensor [list]: The metric tensor, provided by the user
        coord_sys     [list]: The coordinate system given as a list (e.g., [t,x,y,z])
        vector_field  [list]: The vector field, provided by the user
    """
    ndim = len(coord_sys)
    vf = VectorField(metric_tensor, coord_sys, vector_field, 'd')
    if ndim == 4:
        return '$$V^{{\\alpha}}={0}$$'.format(latex(vf.vary_vectorfield_type()))
    elif ndim == 3:
        return '$$V^{{a}}={0}$$'.format(latex(vf.vary_vectorfield_type()))


def cd_vectorfield01_ep(metric_tensor, coord_sys, vector_field, index_symbol):
    """
    Producing equations of covariant derivative for type (0,1) vector field

    Args:
        metric_tensor [list]        : The metric tensor, provided by the user
        coord_sys     [list]        : The coordinate system given as a list (e.g., [t,x,y,z])
        vector_field  [list]        : The vector field, provided by the user
        index_symbol  [sympy.symbol]: The index of the coordinate system given as a symbol (e.g., t, r, theta or phi)
    """
    ndim = len(coord_sys)
    vf = VectorField(metric_tensor, coord_sys, vector_field, 'd')
    index_int = coord_sys.index(index_symbol)
    cd_component = latex(index_symbol)
    cd_eqn = latex(vf.cal_covariant_derivative(index_int))
    if ndim == 4:
        return '$$\\nabla_{{{0}}}V_{{\\alpha}} = {1}$$'.format(cd_component, cd_eqn)
    elif ndim == 3:
        return '$$\\nabla_{{{0}}}V_{{a}} = {1}$$'.format(cd_component, cd_eqn)


def ld_vectorfield01_ep(metric_tensor, coord_sys, vector_field, X):
    """
    Producing equations of Lie derivative of type (0,1) vector field with respect to
    another vector field, X

    Args:
        metric_tensor [list]: The metric tensor, provided by the user
        coord_sys     [list]: The coordinate system given as a list (e.g., [t,x,y,z])
        vector_field  [list]: The vector field, provided by the user
        X             [list]: Given vector field that the Lie derivative is taken w.r.t
    """
    ndim = len(coord_sys)
    vf = VectorField(metric_tensor, coord_sys, vector_field, 'd')
    ld_eqn = latex(vf.cal_lie_derivative(X))
    if ndim == 4:
        return '$$\mathcal{{L}}_XV_{{\\alpha}} = {0}$$'.format(ld_eqn)
    elif ndim == 3:
        return '$$\mathcal{{L}}_XV_{{a}} = {0}$$'.format(ld_eqn)


def killingfield01_ep(metric_tensor, coord_sys, vector_field):
    """
    Producing equation of a Killing field for type (0,1) vector field

    Args:
        metric_tensor [list]: The metric tensor, provided by the user
        coord_sys     [list]: The coordinate system given as a list (e.g., [t,x,y,z])
        vector_field  [list]: The vector field, provided by the user
    """
    vf = VectorField(metric_tensor, coord_sys, vector_field, 'd')
    # since the Lie derivative in the Killing vector equation only takes upper indices
    vector_field_raised = vf.vary_vectorfield_type()
    if vf.isKillingField(vector_field_raised) == True:
        return '$$V_{{\\alpha}}={0}~\\text{{is a Killing field}}$$'.format(latex(vector_field))
    else:
        return '$$V_{{\\alpha}}={0}~\\text{{is not a Killing field}}$$'.format(latex(vector_field))
