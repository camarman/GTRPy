# Two important functions that will be used to produce equations of the tensors and their components


from sympy import latex
from GRTC import *


def tensor_producer(diag_comp, coord_sys, xtensor_name, xtensor_type=''):
    """
    The function that will obtain inputs from the GUI in the GRTC_GUI.py file to produce
    tensor equation in the latex form

    Args:
        diag_comp [list]: Diagonal components of the metric tensor
        coord_sys [list]: The coordinate system (cartesian, spherical, etc.)
        xtensor_name [str]: The name of the desired tensor given as a string
        xtensor_type [str]: The type of the tensor. Given in terms of 'u': contravariant
        and 'd': covariant

    Returns:
        Tensor equation in the latex form
    """
    if xtensor_name == 'Metric Tensor':
        mt = MetricTensor(diag_comp, coord_sys)
        metric_tensor = mt.get_metrictensor()
        if xtensor_type == '':   # default type of the given tensor
            return '$$' + latex(metric_tensor) + '$$'
        else: # changing the type of the tensor and hence the equation as well
            return '$$' + latex(mt.vary_metrictensor_type(metric_tensor, xtensor_type)) + '$$'
    
    if xtensor_name == 'Inverse Metric Tensor':
        mt = MetricTensor(diag_comp, coord_sys)
        inverse_metric_tensor = mt.get_inverse()
        return '$$' + latex(inverse_metric_tensor) + '$$'
    
    if xtensor_name == 'Christoffel Symbol':
        cs = ChristoffelSymbol(diag_comp, coord_sys)
        chris_symbol = cs.get_christoffelsymbol()
        if xtensor_type == '':   # default type of the given tensor
            return '$$' + latex(chris_symbol) + '$$'
        else:
            return '$$' + latex(cs.vary_christoffelsymbol_type(chris_symbol, xtensor_type)) + '$$'
    
    if xtensor_name == 'Riemann Tensor':
        rt = RiemannTensor(diag_comp, coord_sys)
        riemann_tensor = rt.get_riemanntensor()
        if xtensor_type == '':   # default type of the given tensor
            return '$$' + latex(riemann_tensor) + '$$'
        else:
            return '$$' + latex(rt.vary_riemanntensor_type(riemann_tensor, xtensor_type)) + '$$'
    
    if xtensor_name == 'Ricci Tensor':
        rit = RicciTensor(diag_comp, coord_sys)
        ricci_tensor = rit.get_riccitensor()
        if xtensor_type == '':   # default type of the given tensor
             return '$$' + latex(ricci_tensor) + '$$'
        else:
            return '$$' + latex(rit.vary_riccitensor_type(ricci_tensor, xtensor_type)) + '$$'
    
    if xtensor_name == 'Ricci Scalar':
        rs = RicciScalar(diag_comp, coord_sys)
        ricci_scalar = rs.get_ricciscalar()
        return '$$R = ' + latex(ricci_scalar) + '$$'
    
    if xtensor_name == 'Traceless Ricci Tensor':
        trt = TracelessRicciTensor(diag_comp, coord_sys)
        traceless_ricci_tensor = trt.get_trclss_riccitensor()
        if xtensor_type == '':   # default type of the given tensor
            return '$$' + latex(traceless_ricci_tensor) + '$$'
        else:
            return '$$' + latex(trt.vary_trclss_riccitensor_type(traceless_ricci_tensor, xtensor_type)) + '$$'
    
    if xtensor_name == 'Weyl Tensor':
        wyl = WeylTensor(diag_comp, coord_sys)
        weyl_tensor = wyl.get_weyltensor()
        if xtensor_type == '':   # default type of the given tensor
            return '$$' + latex(weyl_tensor) + '$$'
        else:
            return '$$' + latex(wyl.vary_weyltensor_type(weyl_tensor, xtensor_type)) + '$$'
    
    if xtensor_name == 'Einstein Tensor':
        et = EinsteinTensor(diag_comp, coord_sys)
        einstein_tensor = et.get_einsteintensor()      
        if xtensor_type == '':   # default type of the given tensor
            return '$$' + latex(einstein_tensor) + '$$'
        else:
            return '$$' + latex(et.vary_einsteintensor_type(einstein_tensor, xtensor_type)) + '$$'
    
    if xtensor_name == 'Kretschmann Scalar':
        ks = KretschmannScalar(diag_comp, coord_sys)
        kret_scalar = ks.get_kretschmannscalar()
        return '$$K = ' + latex(kret_scalar) + '$$'
                 

def tensor_component_producer(diag_comp, coord_sys, xtensor_name, component='', xtensor_type=''):
    """
    The function that will obtain inputs from the GUI in the GRTC_GUI.py file to produce
    equations of the tensor components in the latex form

    Args:
        diag_comp [list]: Diagonal components of the metric tensor
        coord_sys [list]: The coordinate system (cartesian, spherical, etc.)
        xtensor_name [str]: The name of the desired tensor given as a string
        component [str]: The desired component of the tensor
        xtensor_type [str]: Type of the tensor. Given in terms of 'u': contravariant
        and 'd': covariant

    Returns:
        Tensor component in the latex form
    """
    if xtensor_name == 'Metric Tensor':
        mt = MetricTensor(diag_comp, coord_sys)
        metric_tensor = mt.get_metrictensor()
        if component == '':   # default case 
            return '$$g_{{{0} {1}}} = {2}$$'.format(latex(coord_sys[0]), latex(coord_sys[0]), latex(metric_tensor[0][0]))
        else:
            new_metric_tensor = mt.vary_metrictensor_type(metric_tensor, xtensor_type)
            i = coord_sys.index(component[0])
            j = coord_sys.index(component[1])
            if xtensor_type == 'dd':
                return '$$g_{{{0} {1}}} = {2}$$'.format(latex(component[0]), latex(component[1]), latex(new_metric_tensor[i,j]))
            elif xtensor_type == 'ud':
                return '$$g^{{{0}}}_{{{1}}} = {2}$$'.format(latex(component[0]), latex(component[1]), latex(new_metric_tensor[i,j]))
            else:
                return '$$g^{{{0} {1}}} = {2}$$'.format(latex(component[0]), latex(component[1]), latex(new_metric_tensor[i,j]))
    
    if xtensor_name == 'Inverse Metric Tensor':
        mt = MetricTensor(diag_comp, coord_sys)
        inverse_metric_tensor = mt.get_inverse()
        if component == '':   # default case 
            return '$$g^{{{0} {1}}} = {2}$$'.format(latex(coord_sys[0]), latex(coord_sys[0]), latex(inverse_metric_tensor[0][0]))
        else:
            i = coord_sys.index(component[0])
            j = coord_sys.index(component[1])
            return '$$g^{{{0} {1}}} = {2}$$'.format(latex(component[0]), latex(component[1]), latex(inverse_metric_tensor[i,j]))

    if xtensor_name == 'Christoffel Symbol':
        cs = ChristoffelSymbol(diag_comp, coord_sys)
        chris_symbol = cs.get_christoffelsymbol()
        if component == '':   # default case 
            return '$$\\Gamma^{{{0}}}{{}}_{{{1} {2}}} = {3}$$'.format(latex(coord_sys[0]), latex(coord_sys[0]), latex(coord_sys[0]), latex(chris_symbol[0][0][0]))
        else:
            new_chris_symbol = cs.vary_christoffelsymbol_type(chris_symbol, xtensor_type)
            i = coord_sys.index(component[0])
            j = coord_sys.index(component[1])
            k = coord_sys.index(component[2])
            if xtensor_type == 'ddd':
                return '$$\\Gamma_{{{0} {1} {2}}} = {3}$$'.format(latex(component[0]), latex(component[1]), latex(component[2]), latex(new_chris_symbol[i,j,k]))
            elif xtensor_type == 'udd':
                return '$$\\Gamma^{{{0}}}{{}}_{{{1} {2}}} = {3}$$'.format(latex(component[0]), latex(component[1]), latex(component[2]), latex(new_chris_symbol[i,j,k]))
            elif xtensor_type == 'uud':
                return '$$\\Gamma^{{{0} {1}}}{{}}_{{{2}}} = {3}$$'.format(latex(component[0]), latex(component[1]), latex(component[2]), latex(new_chris_symbol[i,j,k]))
            else:
                return '$$\\Gamma^{{{0} {1} {2}}} = {3}$$'.format(latex(component[0]), latex(component[1]), latex(component[2]), latex(new_chris_symbol[i,j,k]))
    
    if xtensor_name == 'Riemann Tensor':
        rt = RiemannTensor(diag_comp, coord_sys)
        riemann_tensor = rt.get_riemanntensor()
        if component == '':   # default case 
             return '$$R^{{{0}}}{{}}_{{{1} {2} {3}}} = {4}$$'.format(latex(coord_sys[0]), latex(coord_sys[0]), latex(coord_sys[0]), latex(coord_sys[0]), latex(riemann_tensor[0][0][0][0]))
        else:
            new_riemann_tensor = rt.vary_riemanntensor_type(riemann_tensor, xtensor_type)
            i = coord_sys.index(component[0])
            j = coord_sys.index(component[1])
            k = coord_sys.index(component[2])
            l = coord_sys.index(component[3])
            if xtensor_type == 'dddd':
                return '$$R_{{{0} {1} {2} {3}}} = {4}$$'.format(latex(component[0]), latex(component[1]), latex(component[2]), latex(component[3]), latex(new_riemann_tensor[i,j,k,l]))
            elif xtensor_type == 'uddd':
                return '$$R^{{{0}}}{{}}_{{{1} {2} {3}}} = {4}$$'.format(latex(component[0]), latex(component[1]), latex(component[2]), latex(component[3]), latex(new_riemann_tensor[i,j,k,l]))
            elif xtensor_type == 'uudd':
                return '$$R^{{{0} {1}}}{{}}_{{{2} {3}}}= {4}$$'.format(latex(component[0]), latex(component[1]), latex(component[2]), latex(component[3]), latex(new_riemann_tensor[i,j,k,l]))
            elif xtensor_type == 'uuud':
                return '$$R^{{{0} {1} {2}}}{{}}_{{{3}}}= {4}$$'.format(latex(component[0]), latex(component[1]), latex(component[2]), latex(component[3]), latex(new_riemann_tensor[i,j,k,l]))
            else:
                return '$$R^{{{0} {1} {2} {3}}}= {4}$$'.format(latex(component[0]), latex(component[1]), latex(component[2]), latex(component[3]), latex(new_riemann_tensor[i,j,k,l]))
                
    if xtensor_name == 'Ricci Tensor':
        rit = RicciTensor(diag_comp, coord_sys)
        ricci_tensor = rit.get_riccitensor()
        if component == '':   # default case 
            return '$$R_{{{0} {1}}} = {2}$$'.format(latex(coord_sys[0]), latex(coord_sys[0]), latex(ricci_tensor[0][0]))
        else:
            new_ricci_tensor = rit.vary_riccitensor_type(ricci_tensor, xtensor_type)
            i = coord_sys.index(component[0])
            j = coord_sys.index(component[1])
            if xtensor_type == 'dd':
                return '$$R_{{{0} {1}}} = {2}$$'.format(latex(component[0]), latex(component[1]), latex(new_ricci_tensor[i,j]))
            elif xtensor_type == 'ud':
                return '$$R^{{{0}}}_{{{1}}} = {2}$$'.format(latex(component[0]), latex(component[1]), latex(new_ricci_tensor[i,j]))
            else:
                return '$$R^{{{0} {1}}} = {2}$$'.format(latex(component[0]), latex(component[1]), latex(new_ricci_tensor[i,j]))
    
    if xtensor_name == 'Traceless Ricci Tensor':
        trt = TracelessRicciTensor(diag_comp, coord_sys)
        traceless_ricci_tensor = trt.get_trclss_riccitensor()
        if component == '':   # default case
            return '$$Z_{{{0} {1}}} = {2}$$'.format(latex(coord_sys[0]), latex(coord_sys[0]), latex(traceless_ricci_tensor[0][0]))
        else:
            new_traceless_ricci_tensor = trt.vary_trclss_riccitensor_type(traceless_ricci_tensor, xtensor_type)
            i = coord_sys.index(component[0])
            j = coord_sys.index(component[1])
            if xtensor_type == 'dd':
                return '$$Z_{{{0} {1}}} = {2}$$'.format(latex(component[0]), latex(component[1]), latex(new_traceless_ricci_tensor[i,j]))
            elif xtensor_type == 'ud':
                return '$$Z^{{{0}}}_{{{1}}} = {2}$$'.format(latex(component[0]), latex(component[1]), latex(new_traceless_ricci_tensor[i,j]))
            else:
                return '$$Z^{{{0} {1}}} = {2}$$'.format(latex(component[0]), latex(component[1]), latex(new_traceless_ricci_tensor[i,j]))
                
    if xtensor_name == 'Einstein Tensor':
        et = EinsteinTensor(diag_comp, coord_sys)
        einstein_tensor = et.get_einsteintensor()
        if component == '':   # default case
            return '$$G_{{{0} {1}}} = {2}$$'.format(latex(coord_sys[0]), latex(coord_sys[0]), latex(einstein_tensor[0][0]))
        else:
            new_einstein_tensor = et.vary_einsteintensor_type(einstein_tensor, xtensor_type)
            i = coord_sys.index(component[0])
            j = coord_sys.index(component[1])
            if xtensor_type == 'dd':
                return '$$G_{{{0} {1}}} = {2}$$'.format(latex(component[0]), latex(component[1]), latex(new_einstein_tensor[i,j]))
            elif xtensor_type == 'ud':
                return '$$G^{{{0}}}_{{{1}}} = {2}$$'.format(latex(component[0]), latex(component[1]), latex(new_einstein_tensor[i,j]))
            else:
                return '$$G^{{{0} {1}}} = {2}$$'.format(latex(component[0]), latex(component[1]), latex(new_einstein_tensor[i,j]))
            
    if xtensor_name == 'Weyl Tensor':
        wyl = WeylTensor(diag_comp, coord_sys)
        weyl_tensor = wyl.get_weyltensor()
        if component == '':   # default case
            return '$$C_{{{0} {1} {2} {3}}} = {4}$$'.format(latex(coord_sys[0]), latex(coord_sys[0]), latex(coord_sys[0]), latex(coord_sys[0]), latex(weyl_tensor[0][0][0][0]))
        else:
            new_weyl_tensor = wyl.vary_weyltensor_type(weyl_tensor, xtensor_type)
            i = coord_sys.index(component[0])
            j = coord_sys.index(component[1])
            k = coord_sys.index(component[2])
            l = coord_sys.index(component[3])
            if xtensor_type == 'dddd':
                return '$$C_{{{0} {1} {2} {3}}} = {4}$$'.format(latex(component[0]), latex(component[1]), latex(component[2]), latex(component[3]), latex(new_weyl_tensor[i,j,k,l]))
            elif xtensor_type == 'uddd':
                return '$$C^{{{0}}}{{}}_{{{1} {2} {3}}} = {4}$$'.format(latex(component[0]), latex(component[1]), latex(component[2]), latex(component[3]), latex(new_weyl_tensor[i,j,k,l]))
            elif xtensor_type == 'uudd':
                return '$$C^{{{0} {1}}}{{}}_{{{2} {3}}}= {4}$$'.format(latex(component[0]), latex(component[1]), latex(component[2]), latex(component[3]), latex(new_weyl_tensor[i,j,k,l]))
            elif xtensor_type == 'uuud':
                return '$$C^{{{0} {1} {2}}}{{}}_{{{3}}}= {4}$$'.format(latex(component[0]), latex(component[1]), latex(component[2]), latex(component[3]), latex(new_weyl_tensor[i,j,k,l]))
            else:
                return '$$C^{{{0} {1} {2} {3}}}= {4}$$'.format(latex(component[0]), latex(component[1]), latex(component[2]), latex(component[3]), latex(new_weyl_tensor[i,j,k,l]))
