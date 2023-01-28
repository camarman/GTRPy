# ========== PRODUCING EQUATIONS FOR TENSOR FIELDS ==========
from sympy import latex

from gtrpy.src.fields.tensorfield import TensorField


def vry_tensorfield20_ep(metric_tensor, coord_sys, tensor_field, new_type):
    """
    Varying the type of the tensor field from 'uu' to 'ud' or 'dd'

    Args:
        metric_tensor [list]: The metric tensor, provided by the user
        coord_sys     [list]: The coordinate system given as a list (e.g., [t,x,y,z])
        tensor_field  [list]: The tensor field, provided by the user
    """
    ndim = len(coord_sys)
    tf = TensorField(metric_tensor, coord_sys, tensor_field, 'uu')
    if ndim == 4:
        if new_type == 'ud':
            return '$$T^{{\\alpha}}_{{\\beta}}={0}$$'.format(latex(tf.vary_tensorfield_type('ud')))
        elif new_type == 'dd':
            return '$$T_{{\\alpha\\beta}}={0}$$'.format(latex(tf.vary_tensorfield_type('dd')))
    elif ndim == 3:
        if new_type == 'ud':
            return '$$T^{{a}}_{{b}}={0}$$'.format(latex(tf.vary_tensorfield_type('ud')))
        elif new_type == 'dd':
            return '$$T_{{ab}}={0}$$'.format(latex(tf.vary_tensorfield_type('dd')))


def cd_tensorfield20_ep(metric_tensor, coord_sys, tensor_field, index_symbol):
    """
    Producing equations of covariant derivative for type (2,0) tensor field

    Args:
        metric_tensor [list]        : The metric tensor, provided by the user
        coord_sys     [list]        : The coordinate system given as a list (e.g., [t,x,y,z])
        tensor_field  [list]        : The tensor field, provided by the user
        index_symbol  [sympy.symbol]: The index of the coordinate system given as a symbol (e.g., t, r, theta or phi)
    """
    ndim = len(coord_sys)
    tf = TensorField(metric_tensor, coord_sys, tensor_field, 'uu')
    index_int = coord_sys.index(index_symbol)
    cd_component = latex(index_symbol)
    cd_eqn = latex(tf.cal_covariant_derivative(index_int))
    if ndim == 4:
        return '$$\\nabla_{{{0}}}T^{{\\alpha\\beta}} = {1}$$'.format(cd_component, cd_eqn)
    elif ndim == 3:
        return '$$\\nabla_{{{0}}}T^{{ab}} = {1}$$'.format(cd_component, cd_eqn)


def ld_tensorfield20_ep(metric_tensor, coord_sys, tensor_field, X):
    """
    Producing equations of Lie derivative of type (2,0) tensor field with respect to vector field, X

    Args:
        metric_tensor [list]: The metric tensor, provided by the user
        coord_sys     [list]: The coordinate system given as a list (e.g., [t,x,y,z])
        tensor_field  [list]: The tensor field, provided by the user
        X             [list]: Given vector field that the Lie derivative is taken w.r.t
    """
    ndim = len(coord_sys)
    tf = TensorField(metric_tensor, coord_sys, tensor_field, 'uu')
    ld_eqn = latex(tf.cal_lie_derivative(X))
    if ndim == 4:
        return '$$\mathcal{{L}}_XT^{{\\alpha\\beta}} = {0}$$'.format(ld_eqn)
    elif ndim == 3:
        return '$$\mathcal{{L}}_XT^{{ab}} = {0}$$'.format(ld_eqn)


def vry_tensorfield11_ep(metric_tensor, coord_sys, tensor_field, new_type):
    """
    Varying the type of the tensor field from 'ud' to 'uu' or 'dd'

    Args:
        metric_tensor [list]: The metric tensor, provided by the user
        coord_sys     [list]: The coordinate system given as a list (e.g., [t,x,y,z])
        tensor_field  [list]: The tensor field, provided by the user
    """
    ndim = len(coord_sys)
    tf = TensorField(metric_tensor, coord_sys, tensor_field, 'ud')
    if ndim == 4:
        if new_type == 'uu':
            return '$$T^{{\\alpha\\beta}}={0}$$'.format(latex(tf.vary_tensorfield_type('uu')))
        elif new_type == 'dd':
            return '$$T_{{\\alpha\\beta}}={0}$$'.format(latex(tf.vary_tensorfield_type('dd')))
    elif ndim == 3:
        if new_type == 'uu':
            return '$$T^{{ab}}={0}$$'.format(latex(tf.vary_tensorfield_type('uu')))
        elif new_type == 'dd':
            return '$$T_{{ab}}={0}$$'.format(latex(tf.vary_tensorfield_type('dd')))


def cd_tensorfield11_ep(metric_tensor, coord_sys, tensor_field, index_symbol):
    """
    Producing equations of covariant derivative for type (1,1) tensor field

    Args:
        metric_tensor [list]        : The metric tensor, provided by the user
        coord_sys     [list]        : The coordinate system given as a list (e.g., [t,x,y,z])
        tensor_field  [list]        : The tensor field, provided by the user
        index_symbol  [sympy.symbol]: The index of the coordinate system given as a symbol (e.g., t, r, theta or phi)
    """
    ndim = len(coord_sys)
    tf = TensorField(metric_tensor, coord_sys, tensor_field, 'ud')
    index_int = coord_sys.index(index_symbol)
    cd_component = latex(index_symbol)
    cd_eqn = latex(tf.cal_covariant_derivative(index_int))
    if ndim == 4:
        return '$$\\nabla_{{{0}}}T^{{\\alpha}}_{{\\beta}} = {1}$$'.format(cd_component, cd_eqn)
    elif ndim == 3:
        return '$$\\nabla_{{{0}}}T^{{a}}_{{b}} = {1}$$'.format(cd_component, cd_eqn)


def ld_tensorfield11_ep(metric_tensor, coord_sys, tensor_field, X):
    """
    Producing equations of Lie derivative of type (1,1) tensor field with respect to vector field, X

    Args:
        metric_tensor [list]: The metric tensor, provided by the user
        coord_sys     [list]: The coordinate system given as a list (e.g., [t,x,y,z])
        tensor_field  [list]: The tensor field, provided by the user
        X             [list]: Given vector field that the Lie derivative is taken w.r.t
    """
    ndim = len(coord_sys)
    tf = TensorField(metric_tensor, coord_sys, tensor_field, 'ud')
    ld_eqn = latex(tf.cal_lie_derivative(X))
    if ndim == 4:
        return '$$\mathcal{{L}}_XT^{{\\alpha}}_{{\\beta}} = {0}$$'.format(ld_eqn)
    elif ndim == 3:
        return '$$\mathcal{{L}}_XT^{{a}}_{{b}} = {0}$$'.format(ld_eqn)


def vry_tensorfield02_ep(metric_tensor, coord_sys, tensor_field, new_type):
    """
    Varying the type of the tensor field from 'dd' to 'ud' or 'uu'

    Args:
        metric_tensor [list]: The metric tensor, provided by the user
        coord_sys     [list]: The coordinate system given as a list (e.g., [t,x,y,z])
        tensor_field  [list]: The tensor field, provided by the user
    """
    ndim = len(coord_sys)
    tf = TensorField(metric_tensor, coord_sys, tensor_field, 'dd')
    if ndim == 4:
        if new_type == 'ud':
            return '$$T^{{\\alpha}}_{{\\beta}}={0}$$'.format(latex(tf.vary_tensorfield_type('ud')))
        elif new_type == 'uu':
            return '$$T^{{\\alpha\\beta}}={0}$$'.format(latex(tf.vary_tensorfield_type('uu')))
    elif ndim == 3:
        if new_type == 'ud':
            return '$$T^{{a}}_{{b}}={0}$$'.format(latex(tf.vary_tensorfield_type('ud')))
        elif new_type == 'uu':
            return '$$T^{{ab}}={0}$$'.format(latex(tf.vary_tensorfield_type('uu')))


def cd_tensorfield02_ep(metric_tensor, coord_sys, tensor_field, index_symbol):
    """
    Producing equations of covariant derivative for type (0,2) tensor field

    Args:
        metric_tensor [list]        : The metric tensor, provided by the user
        coord_sys     [list]        : The coordinate system given as a list (e.g., [t,x,y,z])
        tensor_field  [list]        : The tensor field, provided by the user
        index_symbol  [sympy.symbol]: The index of the coordinate system given as a symbol (e.g., t, r, theta or phi)
    """
    ndim = len(coord_sys)
    tf = TensorField(metric_tensor, coord_sys, tensor_field, 'dd')
    index_int = coord_sys.index(index_symbol)
    cd_component = latex(index_symbol)
    cd_eqn = latex(tf.cal_covariant_derivative(index_int))
    if ndim == 4:
        return '$$\\nabla_{{{0}}}T_{{\\alpha \\beta}} = {1}$$'.format(cd_component, cd_eqn)
    elif ndim == 3:
        return '$$\\nabla_{{{0}}}T_{{ab}} = {1}$$'.format(cd_component, cd_eqn)


def ld_tensorfield02_ep(metric_tensor, coord_sys, tensor_field, X):
    """
    Producing equations of Lie derivative of type (0,2) tensor field with respect to vector field, X

    Args:
        metric_tensor [list]: The metric tensor, provided by the user
        coord_sys     [list]: The coordinate system given as a list (e.g., [t,x,y,z])
        tensor_field  [list]: The tensor field, provided by the user
        X             [list]: Given vector field that the Lie derivative is taken w.r.t
    """
    ndim = len(coord_sys)
    tf = TensorField(metric_tensor, coord_sys, tensor_field, 'dd')
    ld_eqn = latex(tf.cal_lie_derivative(X))
    if ndim == 4:
        return '$$\mathcal{{L}}_XT_{{\\alpha \\beta}} = {0}$$'.format(ld_eqn)
    elif ndim == 3:
        return '$$\mathcal{{L}}_XT_{{ab}} = {0}$$'.format(ld_eqn)
