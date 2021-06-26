################### GRTC GUI - PRODUCING EQUATIONS ###################


from GRTC_Tensor import *
from GRTC_Cov_Derv import *


################### PRODUCING EQUATIONS OF TENSORS ###################


def tensor_eqn_producer(diag_comp, coord_sys, tensor, tensor_type=''):
    """
    Producing equations of tensors for a given metric and tensor type.

    Args:
        diag_comp [list]: Diagonal components of the metric tensor.
        coord_sys [list]: The coordinate system (cartesian, spherical, etc.).
        tensor [str]: The name of the tensor given as a string.
        tensor_type [str]: The type of the tensor. Given in terms of 'u': contravariant
        and 'd': covariant.
    """
    if tensor == 'Metric Tensor':
        mt = MetricTensor(diag_comp, coord_sys)
        metric_tensor = mt.get_metrictensor()
        if tensor_type == '':   # default type of the given tensor
            return '$$' + latex(metric_tensor) + '$$'
        else:   # changing the type of the tensor and hence the equation as well
            return '$$' + latex(mt.vary_metrictensor_type(metric_tensor, tensor_type)) + '$$'
    
    elif tensor == 'Inverse Metric Tensor':
        mt = MetricTensor(diag_comp, coord_sys)
        inverse_metric_tensor = mt.get_inverse()
        return '$$' + latex(inverse_metric_tensor) + '$$'
    
    elif tensor == 'Christoffel Symbol':
        cs = ChristoffelSymbol(diag_comp, coord_sys)
        chris_symbol = cs.get_christoffelsymbol()
        if tensor_type == '':   # default type of the given tensor
            return '$$' + latex(chris_symbol) + '$$'
        else:   # changing the type of the tensor and hence the equation as well
            return '$$' + latex(cs.vary_christoffelsymbol_type(chris_symbol, tensor_type)) + '$$'
    
    elif tensor == 'Riemann Tensor':
        rt = RiemannTensor(diag_comp, coord_sys)
        riemann_tensor = rt.get_riemanntensor()
        if tensor_type == '':   # default type of the given tensor
            return '$$' + latex(riemann_tensor) + '$$'
        else:   # changing the type of the tensor and hence the equation as well
            return '$$' + latex(rt.vary_riemanntensor_type(riemann_tensor, tensor_type)) + '$$'
    
    elif tensor == 'Ricci Tensor':
        rit = RicciTensor(diag_comp, coord_sys)
        ricci_tensor = rit.get_riccitensor()
        if tensor_type == '':   # default type of the given tensor
             return '$$' + latex(ricci_tensor) + '$$'
        else:   # changing the type of the tensor and hence the equation as well
            return '$$' + latex(rit.vary_riccitensor_type(ricci_tensor, tensor_type)) + '$$'
    
    elif tensor == 'Ricci Scalar':
        rs = RicciScalar(diag_comp, coord_sys)
        ricci_scalar = rs.get_ricciscalar()
        return '$$R = ' + latex(ricci_scalar) + '$$'
    
    elif tensor == 'Traceless Ricci Tensor':
        trt = TracelessRicciTensor(diag_comp, coord_sys)
        traceless_ricci_tensor = trt.get_trclss_riccitensor()
        if tensor_type == '':   # default type of the given tensor
            return '$$' + latex(traceless_ricci_tensor) + '$$'
        else:   # changing the type of the tensor and hence the equation as well
            return '$$' + latex(trt.vary_trclss_riccitensor_type(traceless_ricci_tensor, tensor_type)) + '$$'
    
    elif tensor == 'Weyl Tensor':
        wyl = WeylTensor(diag_comp, coord_sys)
        weyl_tensor = wyl.get_weyltensor()
        if tensor_type == '':   # default type of the given tensor
            return '$$' + latex(weyl_tensor) + '$$'
        else:   # changing the type of the tensor and hence the equation as well
            return '$$' + latex(wyl.vary_weyltensor_type(weyl_tensor, tensor_type)) + '$$'
    
    elif tensor == 'Einstein Tensor':
        et = EinsteinTensor(diag_comp, coord_sys)
        einstein_tensor = et.get_einsteintensor()      
        if tensor_type == '':   # default type of the given tensor
            return '$$' + latex(einstein_tensor) + '$$'
        else:   # changing the type of the tensor and hence the equation as well
            return '$$' + latex(et.vary_einsteintensor_type(einstein_tensor, tensor_type)) + '$$'
    
    elif tensor == 'Kretschmann Scalar':
        ks = KretschmannScalar(diag_comp, coord_sys)
        kret_scalar = ks.get_kretschmannscalar()
        return '$$K = ' + latex(kret_scalar) + '$$'
     
                 
################### PRODUCING EQUATIONS OF TENSOR COMPONENTS ###################


def tensor_component_eqn_producer(diag_comp, coord_sys, tensor, tensor_type='', component=''):
    """
    Producing equations of tensor components for a given metric, tensor type and component

    Args:
        diag_comp [list]: Diagonal components of the metric tensor.
        coord_sys [list]: The coordinate system (cartesian, spherical, etc.).
        tensor [str]: The name of the tensor given as a string.
        tensor_type [str]: Type of the tensor. Given in terms of 'u': contravariant
        and 'd': covariant.
        component [str]: The component of the tensor.
    """
    if tensor == 'Metric Tensor':
        mt = MetricTensor(diag_comp, coord_sys)
        metric_tensor = mt.get_metrictensor()
        if component == '':   # default case 
            return '$$g_{{{0} {1}}} = {2}$$'.format(latex(coord_sys[0]), latex(coord_sys[0]), latex(metric_tensor[0][0]))
        else:
            new_metric_tensor = mt.vary_metrictensor_type(metric_tensor, tensor_type)
            i = coord_sys.index(component[0])
            j = coord_sys.index(component[1])
            if tensor_type == 'dd':
                return '$$g_{{{0} {1}}} = {2}$$'.format(latex(component[0]), latex(component[1]), latex(new_metric_tensor[i,j]))
            elif tensor_type == 'ud':
                return '$$g^{{{0}}}_{{{1}}} = {2}$$'.format(latex(component[0]), latex(component[1]), latex(new_metric_tensor[i,j]))
            else:
                return '$$g^{{{0} {1}}} = {2}$$'.format(latex(component[0]), latex(component[1]), latex(new_metric_tensor[i,j]))
    
    elif tensor == 'Inverse Metric Tensor':
        mt = MetricTensor(diag_comp, coord_sys)
        inverse_metric_tensor = mt.get_inverse()
        if component == '':   # default case 
            return '$$g^{{{0} {1}}} = {2}$$'.format(latex(coord_sys[0]), latex(coord_sys[0]), latex(inverse_metric_tensor[0][0]))
        else:
            i = coord_sys.index(component[0])
            j = coord_sys.index(component[1])
            return '$$g^{{{0} {1}}} = {2}$$'.format(latex(component[0]), latex(component[1]), latex(inverse_metric_tensor[i,j]))

    elif tensor == 'Christoffel Symbol':
        cs = ChristoffelSymbol(diag_comp, coord_sys)
        chris_symbol = cs.get_christoffelsymbol()
        if component == '':   # default case 
            return '$$\\Gamma^{{{0}}}{{}}_{{{1} {2}}} = {3}$$'.format(latex(coord_sys[0]), latex(coord_sys[0]), latex(coord_sys[0]), latex(chris_symbol[0][0][0]))
        else:
            new_chris_symbol = cs.vary_christoffelsymbol_type(chris_symbol, tensor_type)
            i = coord_sys.index(component[0])
            j = coord_sys.index(component[1])
            k = coord_sys.index(component[2])
            if tensor_type == 'ddd':
                return '$$\\Gamma_{{{0} {1} {2}}} = {3}$$'.format(latex(component[0]), latex(component[1]), latex(component[2]), latex(new_chris_symbol[i,j,k]))
            elif tensor_type == 'udd':
                return '$$\\Gamma^{{{0}}}{{}}_{{{1} {2}}} = {3}$$'.format(latex(component[0]), latex(component[1]), latex(component[2]), latex(new_chris_symbol[i,j,k]))
            elif tensor_type == 'uud':
                return '$$\\Gamma^{{{0} {1}}}{{}}_{{{2}}} = {3}$$'.format(latex(component[0]), latex(component[1]), latex(component[2]), latex(new_chris_symbol[i,j,k]))
            else:
                return '$$\\Gamma^{{{0} {1} {2}}} = {3}$$'.format(latex(component[0]), latex(component[1]), latex(component[2]), latex(new_chris_symbol[i,j,k]))
    
    elif tensor == 'Riemann Tensor':
        rt = RiemannTensor(diag_comp, coord_sys)
        riemann_tensor = rt.get_riemanntensor()
        if component == '':   # default case 
             return '$$R^{{{0}}}{{}}_{{{1} {2} {3}}} = {4}$$'.format(latex(coord_sys[0]), latex(coord_sys[0]), latex(coord_sys[0]), latex(coord_sys[0]), latex(riemann_tensor[0][0][0][0]))
        else:
            new_riemann_tensor = rt.vary_riemanntensor_type(riemann_tensor, tensor_type)
            i = coord_sys.index(component[0])
            j = coord_sys.index(component[1])
            k = coord_sys.index(component[2])
            l = coord_sys.index(component[3])
            if tensor_type == 'dddd':
                return '$$R_{{{0} {1} {2} {3}}} = {4}$$'.format(latex(component[0]), latex(component[1]), latex(component[2]), latex(component[3]), latex(new_riemann_tensor[i,j,k,l]))
            elif tensor_type == 'uddd':
                return '$$R^{{{0}}}{{}}_{{{1} {2} {3}}} = {4}$$'.format(latex(component[0]), latex(component[1]), latex(component[2]), latex(component[3]), latex(new_riemann_tensor[i,j,k,l]))
            elif tensor_type == 'uudd':
                return '$$R^{{{0} {1}}}{{}}_{{{2} {3}}}= {4}$$'.format(latex(component[0]), latex(component[1]), latex(component[2]), latex(component[3]), latex(new_riemann_tensor[i,j,k,l]))
            elif tensor_type == 'uuud':
                return '$$R^{{{0} {1} {2}}}{{}}_{{{3}}}= {4}$$'.format(latex(component[0]), latex(component[1]), latex(component[2]), latex(component[3]), latex(new_riemann_tensor[i,j,k,l]))
            else:
                return '$$R^{{{0} {1} {2} {3}}}= {4}$$'.format(latex(component[0]), latex(component[1]), latex(component[2]), latex(component[3]), latex(new_riemann_tensor[i,j,k,l]))
                
    elif tensor == 'Ricci Tensor':
        rit = RicciTensor(diag_comp, coord_sys)
        ricci_tensor = rit.get_riccitensor()
        if component == '':   # default case 
            return '$$R_{{{0} {1}}} = {2}$$'.format(latex(coord_sys[0]), latex(coord_sys[0]), latex(ricci_tensor[0][0]))
        else:
            new_ricci_tensor = rit.vary_riccitensor_type(ricci_tensor, tensor_type)
            i = coord_sys.index(component[0])
            j = coord_sys.index(component[1])
            if tensor_type == 'dd':
                return '$$R_{{{0} {1}}} = {2}$$'.format(latex(component[0]), latex(component[1]), latex(new_ricci_tensor[i,j]))
            elif tensor_type == 'ud':
                return '$$R^{{{0}}}_{{{1}}} = {2}$$'.format(latex(component[0]), latex(component[1]), latex(new_ricci_tensor[i,j]))
            else:
                return '$$R^{{{0} {1}}} = {2}$$'.format(latex(component[0]), latex(component[1]), latex(new_ricci_tensor[i,j]))
    
    elif tensor== 'Traceless Ricci Tensor':
        trt = TracelessRicciTensor(diag_comp, coord_sys)
        traceless_ricci_tensor = trt.get_trclss_riccitensor()
        if component == '':   # default case
            return '$$Z_{{{0} {1}}} = {2}$$'.format(latex(coord_sys[0]), latex(coord_sys[0]), latex(traceless_ricci_tensor[0][0]))
        else:
            new_traceless_ricci_tensor = trt.vary_trclss_riccitensor_type(traceless_ricci_tensor, tensor_type)
            i = coord_sys.index(component[0])
            j = coord_sys.index(component[1])
            if tensor_type == 'dd':
                return '$$Z_{{{0} {1}}} = {2}$$'.format(latex(component[0]), latex(component[1]), latex(new_traceless_ricci_tensor[i,j]))
            elif tensor_type == 'ud':
                return '$$Z^{{{0}}}_{{{1}}} = {2}$$'.format(latex(component[0]), latex(component[1]), latex(new_traceless_ricci_tensor[i,j]))
            else:
                return '$$Z^{{{0} {1}}} = {2}$$'.format(latex(component[0]), latex(component[1]), latex(new_traceless_ricci_tensor[i,j]))
                
    elif tensor == 'Einstein Tensor':
        et = EinsteinTensor(diag_comp, coord_sys)
        einstein_tensor = et.get_einsteintensor()
        if component == '':   # default case
            return '$$G_{{{0} {1}}} = {2}$$'.format(latex(coord_sys[0]), latex(coord_sys[0]), latex(einstein_tensor[0][0]))
        else:
            new_einstein_tensor = et.vary_einsteintensor_type(einstein_tensor, tensor_type)
            i = coord_sys.index(component[0])
            j = coord_sys.index(component[1])
            if tensor_type == 'dd':
                return '$$G_{{{0} {1}}} = {2}$$'.format(latex(component[0]), latex(component[1]), latex(new_einstein_tensor[i,j]))
            elif tensor_type == 'ud':
                return '$$G^{{{0}}}_{{{1}}} = {2}$$'.format(latex(component[0]), latex(component[1]), latex(new_einstein_tensor[i,j]))
            else:
                return '$$G^{{{0} {1}}} = {2}$$'.format(latex(component[0]), latex(component[1]), latex(new_einstein_tensor[i,j]))
            
    elif tensor == 'Weyl Tensor':
        wyl = WeylTensor(diag_comp, coord_sys)
        weyl_tensor = wyl.get_weyltensor()
        if component == '':   # default case
            return '$$C_{{{0} {1} {2} {3}}} = {4}$$'.format(latex(coord_sys[0]), latex(coord_sys[0]), latex(coord_sys[0]), latex(coord_sys[0]), latex(weyl_tensor[0][0][0][0]))
        else:
            new_weyl_tensor = wyl.vary_weyltensor_type(weyl_tensor, tensor_type)
            i = coord_sys.index(component[0])
            j = coord_sys.index(component[1])
            k = coord_sys.index(component[2])
            l = coord_sys.index(component[3])
            if tensor_type == 'dddd':
                return '$$C_{{{0} {1} {2} {3}}} = {4}$$'.format(latex(component[0]), latex(component[1]), latex(component[2]), latex(component[3]), latex(new_weyl_tensor[i,j,k,l]))
            elif tensor_type == 'uddd':
                return '$$C^{{{0}}}{{}}_{{{1} {2} {3}}} = {4}$$'.format(latex(component[0]), latex(component[1]), latex(component[2]), latex(component[3]), latex(new_weyl_tensor[i,j,k,l]))
            elif tensor_type == 'uudd':
                return '$$C^{{{0} {1}}}{{}}_{{{2} {3}}}= {4}$$'.format(latex(component[0]), latex(component[1]), latex(component[2]), latex(component[3]), latex(new_weyl_tensor[i,j,k,l]))
            elif tensor_type == 'uuud':
                return '$$C^{{{0} {1} {2}}}{{}}_{{{3}}}= {4}$$'.format(latex(component[0]), latex(component[1]), latex(component[2]), latex(component[3]), latex(new_weyl_tensor[i,j,k,l]))
            else:
                return '$$C^{{{0} {1} {2} {3}}}= {4}$$'.format(latex(component[0]), latex(component[1]), latex(component[2]), latex(component[3]), latex(new_weyl_tensor[i,j,k,l]))
          

################### PRODUCING EQUATIONS OF COVARIANT DERIVATIVE ###################

 
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
