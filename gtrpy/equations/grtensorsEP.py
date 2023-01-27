# ========== PRODUCING EQUATIONS FOR GTR-TENSORS ==========
from sympy import latex

from gtrpy.src.grtensors import *


def tensor_ep(metric_tensor, coord_sys, tensor_object, tensor_type=''):
    """
    Producing equations of tensors for a given metric and tensor type

    Args:
        metric_tensor [list]: The metric tensor, provided by the user
        coord_sys     [list]: The coordinate system given as a list (e.g., [t,x,y,z])
        tensor_object [str] : The name of the grtensor object (metric tensor, Riemann tensor, etc.)
        tensor_type   [str] : Type of the tensor.
                              It should be given in terms of:
                              'u': contravariant
                              'd': covariant
    """
    if tensor_object == 'Metric Tensor':
        mt = MetricTensor(metric_tensor, coord_sys)
        metric_tensor = mt.get_metrictensor()
        if tensor_type == '':   # default type of the given tensor
            return '$${}$$'.format(latex(metric_tensor))
        else:   # changing the type of the tensor and hence the equation as well
            return '$${}$$'.format(latex(mt.vary_metrictensor_type(tensor_type)))

    elif tensor_object == 'Inverse Metric Tensor':
        mt = MetricTensor(metric_tensor, coord_sys)
        inverse_metric_tensor = mt.get_inverse()
        return '$${}$$'.format(latex(inverse_metric_tensor))

    elif tensor_object == 'Christoffel Symbol':
        cs = ChristoffelSymbol(metric_tensor, coord_sys)
        chris_symbol = cs.get_christoffelsymbol()
        if tensor_type == '':   # default type of the given tensor
            return '$${}$$'.format(latex(chris_symbol))
        else:   # changing the type of the tensor and hence the equation as well
            return '$${}$$'.format(latex(cs.vary_christoffelsymbol_type(tensor_type)))

    elif tensor_object == 'Riemann Tensor':
        rt = RiemannTensor(metric_tensor, coord_sys)
        riemann_tensor = rt.get_riemanntensor()
        if tensor_type == '':   # default type of the given tensor
            return '$${}$$'.format(latex(riemann_tensor))
        else:   # changing the type of the tensor and hence the equation as well
            return '$${}$$'.format(latex(rt.vary_riemanntensor_type(tensor_type)))

    elif tensor_object == 'Ricci Tensor':
        rit = RicciTensor(metric_tensor, coord_sys)
        ricci_tensor = rit.get_riccitensor()
        if tensor_type == '':   # default type of the given tensor
            return '$${}$$'.format(latex(ricci_tensor))
        else:   # changing the type of the tensor and hence the equation as well
            return '$${}$$'.format(latex(rit.vary_riccitensor_type(tensor_type)))

    elif tensor_object == 'Ricci Scalar':
        rs = RicciScalar(metric_tensor, coord_sys)
        ricci_scalar = rs.get_ricciscalar()
        return '$$R = {}$$'.format(latex(ricci_scalar))

    elif tensor_object == 'Traceless Ricci Tensor':
        trt = TracelessRicciTensor(metric_tensor, coord_sys)
        traceless_ricci_tensor = trt.get_trclss_riccitensor()
        if tensor_type == '':   # default type of the given tensor
            return '$${}$$'.format(latex(traceless_ricci_tensor))
        else:   # changing the type of the tensor and hence the equation as well
            return '$${}$$'.format(latex(trt.vary_trclss_riccitensor_type(tensor_type)))

    elif tensor_object == 'Weyl Tensor':
        wyl = WeylTensor(metric_tensor, coord_sys)
        weyl_tensor = wyl.get_weyltensor()
        if tensor_type == '':   # default type of the given tensor
            return '$${}$$'.format(latex(weyl_tensor))
        else:   # changing the type of the tensor and hence the equation as well
            return '$${}$$'.format(latex(wyl.vary_weyltensor_type(tensor_type)))

    elif tensor_object == 'Einstein Tensor':
        et = EinsteinTensor(metric_tensor, coord_sys)
        einstein_tensor = et.get_einsteintensor()
        if tensor_type == '':   # default type of the given tensor
            return '$${}$$'.format(latex(einstein_tensor))
        else:   # changing the type of the tensor and hence the equation as well
            return '$${}$$'.format(latex(et.vary_einsteintensor_type(tensor_type)))

    elif tensor_object == 'Kretschmann Scalar':
        ks = KretschmannScalar(metric_tensor, coord_sys)
        kret_scalar = ks.get_kretschmannscalar()
        return '$$K = {}$$'.format(latex(kret_scalar))


# ========== PRODUCING EQUATIONS OF TENSOR COMPONENTS ==========


def tensor_component_ep(metric_tensor, coord_sys, tensor_object, tensor_type='', component=''):
    """
    Producing equations of tensor components for a given metric, tensor type and component

    Args:
        metric_tensor     [list]: The metric tensor, provided by the user
        coord_sys         [list]: The coordinate system given as a list (e.g., [t,x,y,z])
        tensor_object     [str] : The name of the grtensor object (metric tensor, Riemann tensor, etc.)
        component [sympy.symbol]: The component of the tensor (e.g., g_{tt})
        tensor_type       [str] : Type of the tensor.
                                  It should be given in terms of:
                                  'u': contravariant
                                  'd': covariant
    """
    ndim = len(coord_sys)
    if tensor_object == 'Metric Tensor':
        mt = MetricTensor(metric_tensor, coord_sys)
        metric_tensor = mt.get_metrictensor()
        if component == '':   # default case
            return '$$^{{({0})}}g_{{{1} {2}}} = {3}$$'.format(ndim, latex(coord_sys[0]), latex(coord_sys[0]), latex(metric_tensor[0][0]))
        else:
            new_metric_tensor = mt.vary_metrictensor_type(tensor_type)
            i = coord_sys.index(component[0])
            j = coord_sys.index(component[1])
            if tensor_type == 'dd':
                return '$$^{{({0})}}g_{{{1} {2}}} = {3}$$'.format(ndim, latex(component[0]), latex(component[1]), latex(new_metric_tensor[i, j]))
            elif tensor_type == 'ud':
                return '$$^{{({0})}}g^{{{1}}}_{{{2}}} = {3}$$'.format(ndim, latex(component[0]), latex(component[1]), latex(new_metric_tensor[i, j]))
            else:
                return '$$^{{({0})}}g^{{{1} {2}}} = {3}$$'.format(ndim, latex(component[0]), latex(component[1]), latex(new_metric_tensor[i, j]))

    elif tensor_object == 'Inverse Metric Tensor':
        mt = MetricTensor(metric_tensor, coord_sys)
        inverse_metric_tensor = mt.get_inverse()
        if component == '':   # default case
            return '$$^{{({0})}}g^{{{1} {2}}} = {3}$$'.format(ndim, latex(coord_sys[0]), latex(coord_sys[0]), latex(inverse_metric_tensor[0][0]))
        else:
            i = coord_sys.index(component[0])
            j = coord_sys.index(component[1])
            return '$$^{{({0})}}g^{{{1} {2}}} = {3}$$'.format(ndim, latex(component[0]), latex(component[1]), latex(inverse_metric_tensor[i, j]))

    elif tensor_object == 'Christoffel Symbol':
        cs = ChristoffelSymbol(metric_tensor, coord_sys)
        chris_symbol = cs.get_christoffelsymbol()
        if component == '':   # default case
            return '$$^{{({0})}}\\Gamma^{{{1}}}{{}}_{{{2} {3}}} = {4}$$'.format(ndim, latex(coord_sys[0]), latex(coord_sys[0]), latex(coord_sys[0]), latex(chris_symbol[0][0][0]))
        else:
            new_chris_symbol = cs.vary_christoffelsymbol_type(tensor_type)
            i = coord_sys.index(component[0])
            j = coord_sys.index(component[1])
            k = coord_sys.index(component[2])
            if tensor_type == 'ddd':
                return '$$^{{({0})}}\\Gamma_{{{1} {2} {3}}} = {4}$$'.format(ndim, latex(component[0]), latex(component[1]), latex(component[2]), latex(new_chris_symbol[i, j, k]))
            elif tensor_type == 'udd':
                return '$$^{{({0})}}\\Gamma^{{{1}}}{{}}_{{{2} {3}}} = {4}$$'.format(ndim, latex(component[0]), latex(component[1]), latex(component[2]), latex(new_chris_symbol[i, j, k]))
            elif tensor_type == 'uud':
                return '$$^{{({0})}}\\Gamma^{{{1} {2}}}{{}}_{{{3}}} = {4}$$'.format(ndim, latex(component[0]), latex(component[1]), latex(component[2]), latex(new_chris_symbol[i, j, k]))
            else:
                return '$$^{{({0})}}\\Gamma^{{{1} {2} {3}}} = {4}$$'.format(ndim, latex(component[0]), latex(component[1]), latex(component[2]), latex(new_chris_symbol[i, j, k]))

    elif tensor_object == 'Riemann Tensor':
        rt = RiemannTensor(metric_tensor, coord_sys)
        riemann_tensor = rt.get_riemanntensor()
        if component == '':   # default case
            return '$$^{{({0})}}R^{{{1}}}{{}}_{{{2} {3} {4}}} = {5}$$'.format(ndim, latex(coord_sys[0]), latex(coord_sys[0]), latex(coord_sys[0]), latex(coord_sys[0]), latex(riemann_tensor[0][0][0][0]))
        else:
            new_riemann_tensor = rt.vary_riemanntensor_type(tensor_type)
            i = coord_sys.index(component[0])
            j = coord_sys.index(component[1])
            k = coord_sys.index(component[2])
            l = coord_sys.index(component[3])
            if tensor_type == 'dddd':
                return '$$^{{({0})}}R_{{{1} {2} {3} {4}}} = {5}$$'.format(ndim, latex(component[0]), latex(component[1]), latex(component[2]), latex(component[3]), latex(new_riemann_tensor[i, j, k, l]))
            elif tensor_type == 'uddd':
                return '$$^{{({0})}}R^{{{1}}}{{}}_{{{2} {3} {4}}} = {5}$$'.format(ndim, latex(component[0]), latex(component[1]), latex(component[2]), latex(component[3]), latex(new_riemann_tensor[i, j, k, l]))
            elif tensor_type == 'uudd':
                return '$$^{{({0})}}R^{{{1} {2}}}{{}}_{{{3} {4}}} = {5}$$'.format(ndim, latex(component[0]), latex(component[1]), latex(component[2]), latex(component[3]), latex(new_riemann_tensor[i, j, k, l]))
            elif tensor_type == 'uuud':
                return '$$^{{({0})}}R^{{{1} {2} {3}}}{{}}_{{{4}}} = {5}$$'.format(ndim, latex(component[0]), latex(component[1]), latex(component[2]), latex(component[3]), latex(new_riemann_tensor[i, j, k, l]))
            else:
                return '$$^{{({0})}}R^{{{1} {2} {3} {4}}} = {5}$$'.format(ndim, latex(component[0]), latex(component[1]), latex(component[2]), latex(component[3]), latex(new_riemann_tensor[i, j, k, l]))

    elif tensor_object == 'Ricci Tensor':
        rit = RicciTensor(metric_tensor, coord_sys)
        ricci_tensor = rit.get_riccitensor()
        if component == '':   # default case
            return '$$^{{({0})}}R_{{{1} {2}}} = {3}$$'.format(ndim, latex(coord_sys[0]), latex(coord_sys[0]), latex(ricci_tensor[0][0]))
        else:
            new_ricci_tensor = rit.vary_riccitensor_type(tensor_type)
            i = coord_sys.index(component[0])
            j = coord_sys.index(component[1])
            if tensor_type == 'dd':
                return '$$^{{({0})}}R_{{{1} {2}}} = {3}$$'.format(ndim, latex(component[0]), latex(component[1]), latex(new_ricci_tensor[i, j]))
            elif tensor_type == 'ud':
                return '$$^{{({0})}}R^{{{1}}}_{{{2}}} = {3}$$'.format(ndim, latex(component[0]), latex(component[1]), latex(new_ricci_tensor[i, j]))
            else:
                return '$$^{{({0})}}R^{{{1} {2}}} = {3}$$'.format(ndim, latex(component[0]), latex(component[1]), latex(new_ricci_tensor[i, j]))

    elif tensor_object == 'Traceless Ricci Tensor':
        trt = TracelessRicciTensor(metric_tensor, coord_sys)
        traceless_ricci_tensor = trt.get_trclss_riccitensor()
        if component == '':   # default case
            return '$$^{{({0})}}Z_{{{1} {2}}} = {3}$$'.format(ndim, latex(coord_sys[0]), latex(coord_sys[0]), latex(traceless_ricci_tensor[0][0]))
        else:
            new_traceless_ricci_tensor = trt.vary_trclss_riccitensor_type(tensor_type)
            i = coord_sys.index(component[0])
            j = coord_sys.index(component[1])
            if tensor_type == 'dd':
                return '$$^{{({0})}}Z_{{{1} {2}}} = {3}$$'.format(ndim, latex(component[0]), latex(component[1]), latex(new_traceless_ricci_tensor[i, j]))
            elif tensor_type == 'ud':
                return '$$^{{({0})}}Z^{{{1}}}_{{{2}}} = {3}$$'.format(ndim, latex(component[0]), latex(component[1]), latex(new_traceless_ricci_tensor[i, j]))
            else:
                return '$$^{{({0})}}Z^{{{1} {2}}} = {3}$$'.format(ndim, latex(component[0]), latex(component[1]), latex(new_traceless_ricci_tensor[i, j]))

    elif tensor_object == 'Einstein Tensor':
        et = EinsteinTensor(metric_tensor, coord_sys)
        einstein_tensor = et.get_einsteintensor()
        if component == '':   # default case
            return '$$^{{({0})}}G_{{{1} {2}}} = {3}$$'.format(ndim, latex(coord_sys[0]), latex(coord_sys[0]), latex(einstein_tensor[0][0]))
        else:
            new_einstein_tensor = et.vary_einsteintensor_type(tensor_type)
            i = coord_sys.index(component[0])
            j = coord_sys.index(component[1])
            if tensor_type == 'dd':
                return '$$^{{({0})}}G_{{{1} {2}}} = {3}$$'.format(ndim, latex(component[0]), latex(component[1]), latex(new_einstein_tensor[i, j]))
            elif tensor_type == 'ud':
                return '$$^{{({0})}}G^{{{1}}}_{{{2}}} = {3}$$'.format(ndim, latex(component[0]), latex(component[1]), latex(new_einstein_tensor[i, j]))
            else:
                return '$$^{{({0})}}G^{{{1} {2}}} = {3}$$'.format(ndim, latex(component[0]), latex(component[1]), latex(new_einstein_tensor[i, j]))

    elif tensor_object == 'Weyl Tensor':
        wyl = WeylTensor(metric_tensor, coord_sys)
        weyl_tensor = wyl.get_weyltensor()
        if component == '':   # default case
            return '$$^{{({0})}}C_{{{1} {2} {3} {4}}} = {5}$$'.format(ndim, latex(coord_sys[0]), latex(coord_sys[0]), latex(coord_sys[0]), latex(coord_sys[0]), latex(weyl_tensor[0][0][0][0]))
        else:
            new_weyl_tensor = wyl.vary_weyltensor_type(tensor_type)
            i = coord_sys.index(component[0])
            j = coord_sys.index(component[1])
            k = coord_sys.index(component[2])
            l = coord_sys.index(component[3])
            if tensor_type == 'dddd':
                return '$$^{{({0})}}C_{{{1} {2} {3} {4}}} = {5}$$'.format(ndim, latex(component[0]), latex(component[1]), latex(component[2]), latex(component[3]), latex(new_weyl_tensor[i, j, k, l]))
            elif tensor_type == 'uddd':
                return '$$^{{({0})}}C^{{{1}}}{{}}_{{{2} {3} {4}}} = {5}$$'.format(ndim, latex(component[0]), latex(component[1]), latex(component[2]), latex(component[3]), latex(new_weyl_tensor[i, j, k, l]))
            elif tensor_type == 'uudd':
                return '$$^{{({0})}}C^{{{1} {2}}}{{}}_{{{3} {4}}} = {5}$$'.format(ndim, latex(component[0]), latex(component[1]), latex(component[2]), latex(component[3]), latex(new_weyl_tensor[i, j, k, l]))
            elif tensor_type == 'uuud':
                return '$$^{{({0})}}C^{{{1} {2} {3}}}{{}}_{{{4}}} = {5}$$'.format(ndim, latex(component[0]), latex(component[1]), latex(component[2]), latex(component[3]), latex(new_weyl_tensor[i, j, k, l]))
            else:
                return '$$^{{({0})}}C^{{{1} {2} {3} {4}}} = {5}$$'.format(ndim, latex(component[0]), latex(component[1]), latex(component[2]), latex(component[3]), latex(new_weyl_tensor[i, j, k, l]))
