################### GRTC - TENSORS ###################


from IPython.display import display, Latex
from itertools import permutations, product
from sympy import Array, diff, latex, MutableDenseNDimArray, nsimplify, simplify
from numpy import diag, einsum, zeros, array


def permutation_finder(tensor_type):
    """
    Permuting tensor indices for a given tensor type

    Args:
        tensor_type [str]: The type of the tensor, written in terms of 'u' (contravariant) and 'd' (covariant)

    Returns:
        unique_permutations [set]: Unique permutations of the tensor indices

    Example: 
    >>> permutation_finder('udd')
    >>> {'dud', 'ddu','udd'}
    """
    permt_list = list(permutations(tensor_type))
    return set([''.join(i) for i in permt_list])


def Simplify(xtensor):
    """
    Simplifying the tensors via sympy s methods

    Args:
        xtensor [sympy.tensor]: Given tensor

    Returns:
        Simplified version of the tensor
    """
    try:
        return nsimplify(xtensor)
    except: # For some tensors the nsimplify method does not work properly
        return xtensor


def derivative_of_metric(coord_sys, xmetric_tensor, i, j, k):
    """
    Taking the partial derivative of a given metric tensor [g_jk] with respect to the 
    [i]'th component.

    Args:
        coord_sys [list]: The coordinate system (cartesian, spherical, etc.)
        xmetric_tensor [sympy.tensor]: Given metric tensor, g_jk
        i,j,k [int]: Coordinate indices that runs from 0 to ndim
    """
    return Simplify(diff(xmetric_tensor[j, k], coord_sys[i]))


def derivative_of_chris(coord_sys, xchris_symb, i, j, k, l):
    """
    Taking the partial derivative of a given Christoffel Symbol [G^j_kl] with respect to the 
    [i]'th component.

    Args:
        coord_sys [list]: The coordinate system (cartesian, spherical, etc.)
        xchris_symb [sympy.tensor]: Given Christoffel Symbol, G^j_kl
        i,j,k,l [int]: Coordinate indices that runs from 0 to ndim
    """
    return Simplify(diff(xchris_symb[j, k, l], coord_sys[i]))


class MetricTensor(object):
    def __init__(self, diag_comp, coord_sys):
        """
        Creating the Metric Tensor class

        Args:
            diag_comp [list]: Diagonal components of the metric tensor
            coord_sys [list]: The coordinate system (cartesian, spherical, etc.)
        
        Returns:
            self.diag_comp [np.ndarray]: Diagonal components of the metric tensor
            self.coord_sys [np.ndarray]: The coordinate system (cartesian, spherical, etc.)
            self.metric_type [str]: Type of the metric tensor. Default type is 'dd'
            self.metric_obj [sympy.tensor]: The metric tensor, g_jk
            self.inverse_metric_obj [sympy.tensor]: The inverse of the metric tensor, g^jk
            self.ndim [int]: Dimension of the space. It can be 3 or 4
    
        Raises:
            ValueError: If the dimension of the space is not 3 or 4
        """
        self.diag_comp = array(diag_comp)
        self.coord_sys = array(coord_sys)
        self.metric_type = 'dd'
        self.metric_obj = Simplify(diag(self.diag_comp))
        self.inverse_metric_obj = Simplify(diag(1/self.diag_comp))
        if len(diag_comp) == 3 or len(diag_comp) == 4:
            self.ndim = len(diag_comp)
        else:
            raise ValueError('The dimension of the space can only be 3 or 4')

    def get_metrictensor(self):
        """
        Returns the metric tensor with respect to the given diagonal components
        """
        return self.metric_obj

    def get_metrictensor_type(self):
        """
        Returns the type of the metric tensor 
        """
        return self.metric_type

    def get_inverse(self):
        """
        Returns the inverse of the metric tensor
        """
        return self.inverse_metric_obj
    
    def raise_index(self, xmetric_tensor):
        """
        Raising the index of the metric tensor

        Args:
            xmetric_tensor [sympy.tensor]: Given metric tensor 
        """
        return Array(einsum('jk,ki->ji', xmetric_tensor, self.inverse_metric_obj, optimize='optimal'))
    
    def vary_metrictensor_type(self, xmetric_tensor, new_type):
        """
        Varying the type of the metric tensor 

        Args:
            xmetric_tensor [sympy.tensor]: Given metric tensor
            new_type [str]: The new type of the metric tensor. It should be in terms of 
            'u': contravariant (upper-indices) and 'd': covariant (lower-indices)

        Raises:
            TypeError: If the type is given by wrong set of characters

        Returns:
            The new metric tensor for a given type
        """
        self.metric_type = new_type
        if new_type == 'dd':
            return self.metric_obj
        elif new_type in permutation_finder('ud'):
            return Simplify(self.raise_index(xmetric_tensor))
        elif new_type == 'uu':
            return Simplify(self.raise_index(self.raise_index(xmetric_tensor)))
        else:
            raise TypeError(
                'Please enter a valid tensor type in terms of "u": contravariant and "d": covariant with 2 indices')


class ChristoffelSymbol(MetricTensor):
    def __init__(self, diag_comp, coord_sys):
        """
        Creating the Christoffel Symbol class

        Args:
            diag_comp [list]: Diagonal components of the metric tensor
            coord_sys [list]: The coordinate system (cartesian, spherical, etc.)

        Returns:
            self.chris_type [str]: Type of the Christoffel Symbol. Default type is 'udd'
            self.chris_obj [sympy.tensor]: The Christoffel Symbol, G^m_ij
        """
        MetricTensor.__init__(self, diag_comp, coord_sys)
        self.chris_type = 'udd'
        chris_sym = MutableDenseNDimArray(zeros((self.ndim,)*3))
        for m, i, j in product(range(self.ndim), repeat=3):
            einstein_sum = 0
            for k in range(self.ndim):
                I1 = derivative_of_metric(self.coord_sys, self.metric_obj, j, k, i)
                I2 = derivative_of_metric(self.coord_sys, self.metric_obj, i, k, j)
                I3 = derivative_of_metric(self.coord_sys, self.metric_obj, k, i, j)
                S = I1 + I2 - I3
                einstein_sum += 1/2 * self.inverse_metric_obj[m, k] * S
            chris_sym[m, i, j] = einstein_sum
        self.chris_obj = Simplify(chris_sym)


    def get_christoffelsymbol(self):
        """
        Returns the Christoffel Symbol with respect to the given diagonal components
        """
        return self.chris_obj


    def get_christoffelsymbol_type(self):
        """
        Returns the type of the Christoffel Symbol
        """
        return self.chris_type


    def lower_index(self, xchris_symbol):
        """
        Lowering the index of the Christoffel Symbol

        Args:
            xchris_symbol [sympy.tensor]: Given Christoffel Symbol
        """
        return Array(einsum('ijk,il->ljk', xchris_symbol, self.metric_obj, optimize='optimal'))


    def raise_index(self, xchris_symbol):
        """
        Raising the index of the Christoffel Symbol

        Args:
            xchris_symbol [sympy.tensor]: Given Christoffel Symbol
        """
        return Array(einsum('ikj,jm->imk', xchris_symbol, self.inverse_metric_obj, optimize='optimal'))


    def raise_index1(self, xchris_symbol):
        """
        Raising the second index of the Christoffel Symbol

        Args:
            xchris_symbol [sympy.tensor]: Given Christoffel Symbol
        """
        return Array(einsum('imk,kn->imn', xchris_symbol, self.inverse_metric_obj, optimize='optimal'))

    def vary_christoffelsymbol_type(self, xchris_symbol, new_type):
        """
        Varying the type of the Christoffel Symbol

        Args:
            xchris_symbol [sympy.tensor]: Given Christoffel Symbol
            new_type [str]: The new type of the Christoffel Symbol. It should be given 
            in terms of 'u': contravariant (upper-indices) and 'd': covariant (lower-indices)

        Raises:
            TypeError: If the type is given by wrong set of characters

        Returns:
            The new Christoffel Symbol for a given type
        """
        self.chris_type = new_type
        if new_type == 'ddd':
            return Simplify(self.lower_index(xchris_symbol))
        elif new_type in permutation_finder('udd'):
            return self.chris_obj
        elif new_type in permutation_finder('uud'):
            return Simplify(self.raise_index(xchris_symbol))
        elif new_type == 'uuu':
            return Simplify(self.raise_index1(self.raise_index(xchris_symbol)))
        else:
            raise TypeError('Please enter a valid tensor type in terms of "u": contravariant and "d": covariant with 3 indices')

    def nonzero_christoffelsymbol(self, xchris_symbol):
        """
        Printing the nonzero components of the given Christoffel Symbol
        
        Args:
            xchris_symbol [sympy.tensor]: Given Christoffel Symbol
            
        Returns:
            Non-zero components of the Christoffel Symbol
        """
        if self.chris_type == 'uuu':
            for i, j, k in product(range(self.ndim), repeat=3):
                if xchris_symbol[i, j, k] != 0:
                    display(Latex('$\\Gamma^{{{0} {1} {2}}} = {3}$'.format(latex(self.coord_sys[i]), latex(
                    self.coord_sys[j]), latex(self.coord_sys[k]), latex(xchris_symbol[i, j, k]))))
        elif self.chris_type in permutation_finder('udd'):
            for i, j, k in product(range(self.ndim), repeat=3):
                if xchris_symbol[i, j, k] != 0:
                    display(Latex('$\\Gamma^{{{0}}}{{}}_{{{1} {2}}} = {3}$'.format(latex(self.coord_sys[i]), latex(
                    self.coord_sys[j]), latex(self.coord_sys[k]), latex(xchris_symbol[i, j, k]))))
        elif self.chris_type in permutation_finder('uud'):
            for i, j, k in product(range(self.ndim), repeat=3):
                if xchris_symbol[i, j, k] != 0:
                    display(Latex('$\\Gamma^{{{0} {1}}}{{}}_{{{2}}} = {3}$'.format(latex(self.coord_sys[i]), latex(
                    self.coord_sys[j]), latex(self.coord_sys[k]), latex(xchris_symbol[i, j, k]))))
        elif self.chris_type == 'ddd':
            for i, j, k in product(range(self.ndim), repeat=3):
                if xchris_symbol[i, j, k] != 0:
                    display(Latex('$\\Gamma_{{{0} {1} {2}}} = {3}$'.format(latex(self.coord_sys[i]), latex(
                        self.coord_sys[j]), latex(self.coord_sys[k]), latex(xchris_symbol[i, j, k]))))
                    
                                                                
class RiemannTensor(ChristoffelSymbol):
    def __init__(self, diag_comp, coord_sys):
        """ 
        Creating the Riemann Tensor class

        Args:
            diag_comp [list]: Diagonal components of the metric tensor
            coord_sys [list]: The coordinate system (cartesian, spherical, etc.)

        Returns:
            self.riemann_type [str]: Type of the Riemann Tensor. Default type is 'uddd'
            self.riemann_obj [sympy.tensor]: The Riemann Tensor, R^l_ijk
        """
        ChristoffelSymbol.__init__(self, diag_comp, coord_sys)
        self.riemann_type = 'uddd'
        riemann_tensor = MutableDenseNDimArray(zeros((self.ndim,)*4))
        for l, i, j, k in product(range(self.ndim), repeat=4):
            Q1 = derivative_of_chris(self.coord_sys, self.chris_obj, j, l, i, k)
            Q2 = derivative_of_chris(self.coord_sys, self.chris_obj, i, l, j, k)
            einstein_sum = 0
            for p in range(self.ndim):
                I1 = self.chris_obj[p, i, k] * self.chris_obj[l, j, p]
                I2 = self.chris_obj[p, j, k] * self.chris_obj[l, i, p]
                einstein_sum += (I1 - I2)
            riemann_tensor[l, i, j, k] = Q1 - Q2 + einstein_sum
        self.riemann_obj = Simplify(riemann_tensor)

    def get_riemanntensor(self):
        """
        Returns the Riemann Tensor with respect to the given diagonal components
        """
        return self.riemann_obj

    def get_riemanntensor_type(self):
        """
        Returns the type of the Riemann Tensor
        """
        return self.riemann_type

    def lower_index(self, xriemann_tensor):
        """
        Lowering the index of the Riemann Tensor

        Args:
            xriemann_tensor [sympy.tensor]: Given Riemann Tensor
        """
        return Array(einsum('abcd,ak->kbcd', xriemann_tensor, self.metric_obj, optimize='optimal'))

    def raise_index(self, xriemann_tensor):
        """
        Raising the first index of the Riemann Tensor

        Args:
            xriemann_tensor [sympy.tensor]: Given Riemann Tensor
        """
        return Array(einsum('abcd,bk->akcd', xriemann_tensor, self.inverse_metric_obj, optimize='optimal'))

    def raise_index1(self, xriemann_tensor):
        """
        Raising the second index of the Riemann Tensor

        Args:
            xriemann_tensor [sympy.tensor]: Given Riemann Tensor
        """
        return Array(einsum('akcd,cl->akld', xriemann_tensor, self.inverse_metric_obj, optimize='optimal'))

    def raise_index2(self, xriemann_tensor):
        """
        Raising the third index of the Riemann Tensor

        Args:
            xriemann_tensor [sympy.tensor]: Given Riemann Tensor
        """
        return Array(einsum('akld,df->aklf', xriemann_tensor, self.inverse_metric_obj, optimize='optimal'))

    def vary_riemanntensor_type(self, xriemann_tensor, new_type):
        """
        Varying the type of the Riemann Tensor

        Args:
            xriemann_tensor [sympy.tensor]: Given Riemann Tensor
            new_type [str]: The new type of the Riemann Tensor. It should be given
            in terms of 'u': contravariant (upper-indices) and 'd': covariant (lower-indices)

        Raises:
            TypeError: If the type is given by wrong set of characters

        Returns:
            The new Riemann Tensor for a given type
        """
        self.riemann_type = new_type
        if new_type == 'dddd':
            return Simplify(self.lower_index(xriemann_tensor))
        elif new_type in permutation_finder('uddd'):
            return self.riemann_obj
        elif new_type in permutation_finder('uudd'):
            return Simplify(self.raise_index(xriemann_tensor))
        elif new_type in permutation_finder('uuud'):
            return Simplify(self.raise_index1(self.raise_index(xriemann_tensor)))
        elif new_type == 'uuuu':
            return Simplify(self.raise_index2(self.raise_index1(self.raise_index(xriemann_tensor))))
        else:
            raise TypeError('Please enter a valid tensor type in terms of "u": contravariant and "d": covariant with 4 indices')

    def nonzero_riemanntensor(self, xriemann_tensor):
        """
        Printing the nonzero components of the given Riemann Tensor
        
        Args:
            xriemann_tensor [sympy.tensor]: Given Riemann Tensor
        
        Returns:
            Non-zero components of the Riemann Tensor
        """
        if self.riemann_type  == 'uuuu':
            for i, j, k, l in product(range(self.ndim), repeat=4):
                if xriemann_tensor[i, j, k, l] != 0:
                    display(Latex('$R^{{{0} {1} {2} {3}}}= {4}$'.format(latex(self.coord_sys[i]), latex(
                    self.coord_sys[j]), latex(self.coord_sys[k]), latex(self.coord_sys[l]), latex(xriemann_tensor[i, j, k, l]))))
        elif self.riemann_type in permutation_finder('uuud'):
            for i, j, k, l in product(range(self.ndim), repeat=4):
                if xriemann_tensor[i, j, k, l] != 0:
                    display(Latex('$R^{{{0} {1} {2}}}{{}}_{{{3}}}= {4}$'.format(latex(self.coord_sys[i]), latex(
                    self.coord_sys[j]), latex(self.coord_sys[k]), latex(self.coord_sys[l]), latex(xriemann_tensor[i, j, k, l]))))
        elif self.riemann_type in permutation_finder('uudd'):
            for i, j, k, l in product(range(self.ndim), repeat=4):
                if xriemann_tensor[i, j, k, l] != 0:
                    display(Latex('$R^{{{0} {1}}}{{}}_{{{2} {3}}}= {4}$'.format(latex(self.coord_sys[i]), latex(
                        self.coord_sys[j]), latex(self.coord_sys[k]), latex(self.coord_sys[l]), latex(xriemann_tensor[i, j, k, l]))))
        elif self.riemann_type in permutation_finder('uddd'):
            for i, j, k, l in product(range(self.ndim), repeat=4):
                if xriemann_tensor[i, j, k, l] != 0:
                    display(Latex('$R^{{{0}}}{{}}_{{{1} {2} {3}}} = {4}$'.format(latex(self.coord_sys[i]), latex(
                    self.coord_sys[j]), latex(self.coord_sys[k]), latex(self.coord_sys[l]), latex(xriemann_tensor[i, j, k, l]))))
        elif self.riemann_type == 'dddd':
            for i, j, k, l in product(range(self.ndim), repeat=4):
                if xriemann_tensor[i, j, k, l] != 0:
                    display(Latex('$R_{{{0} {1} {2} {3}}} = {4}$'.format(latex(self.coord_sys[i]), latex(
                        self.coord_sys[j]), latex(self.coord_sys[k]), latex(self.coord_sys[l]), latex(xriemann_tensor[i, j, k, l]))))
                    

class RicciTensor(RiemannTensor):
    def __init__(self, diag_comp, coord_sys):
        """ 
        Creating the Ricci Tensor class

        Args:
            diag_comp [list]: Diagonal components of the metric tensor
            coord_sys [list]: The coordinate system (cartesian, spherical, etc.)

        Returns:
            self.riccitensor_type [str]: Type of the Ricci Tensor. Default type is 'dd'
            self.riccitensor_obj [sympy.tensor]: The Ricci Tensor, R_ik            
        """
        RiemannTensor.__init__(self, diag_comp, coord_sys)
        self.riccitensor_type = 'dd'
        ricci_tensor = MutableDenseNDimArray(zeros((self.ndim,)*2))
        for i, k in product(range(self.ndim), repeat=2):
            einstein_sum = 0
            for j in range(self.ndim):
                einstein_sum += self.riemann_obj[j, i, j, k]
            ricci_tensor[i, k] = einstein_sum
        self.riccitensor_obj = Simplify(ricci_tensor)

    def get_riccitensor(self):
        """
        Returns the Ricci Tensor with respect to the given diagonal components
        """
        return self.riccitensor_obj

    def get_riccitensor_type(self):
        """
        Returns the type of the Ricci Tensor
        """
        return self.riccitensor_type

    def raise_index(self, xricci_tensor):
        """
        Raising the index of the Ricci Tensor

        Args:
            xricci_tensor [sympy.tensor]: Given Ricci Tensor  
        """
        return Array(einsum('ij,jk->ik', xricci_tensor, self.inverse_metric_obj, optimize='optimal'))

    def vary_riccitensor_type(self, xricci_tensor, new_type):
        """
        Varying the type of the Ricci Tensor

        Args:
            xricci_tensor [sympy.tensor]: Given Ricci Tensor
            new_type [str]: The new type of the Ricci Tensor. It should be given
            in terms of 'u': contravariant (upper-indices) and 'd': covariant (lower-indices)

        Raises:
            TypeError: If the type is given by wrong set of characters

        Returns:
            The new Ricci Tensor for a given type
        """
        self.riccitensor_type = new_type
        if new_type == 'dd':
            return self.riccitensor_obj
        elif new_type in permutation_finder('ud'):
            return Simplify(self.raise_index(xricci_tensor))
        elif new_type == 'uu':
            return Simplify(self.raise_index(self.raise_index(xricci_tensor)))
        else:
            raise TypeError(
                'Please enter a valid tensor type in terms of "u": contravariant and "d": covariant with 2 indices')


class RicciScalar(RicciTensor):
    def __init__(self, diag_comp, coord_sys):
        """ 
        Creating the Ricci Scalar class

        Args:
            diag_comp [list]: Diagonal components of the metric tensor
            coord_sys [list]: The coordinate system (cartesian, spherical, etc.)

        Returns:
            self.ricciscalar_obj [int/symbol]: The Ricci Scalar, R           
        """
        RicciTensor.__init__(self, diag_comp, coord_sys)
        ricci_scalar = 0
        for i, k in product(range(self.ndim), repeat=2):
            ricci_scalar += self.inverse_metric_obj[i,k] * self.riccitensor_obj[i, k]
        self.ricciscalar_obj = simplify(ricci_scalar)
        
    def get_ricciscalar(self):
        """
        Returns the Ricci Scalar with respect to the given diagonal components
        """
        return self.ricciscalar_obj


class WeylTensor(RicciScalar):
    def __init__(self, diag_comp, coord_sys):
        """
        Creating the Weyl Tensor class

        Args:
            diag_comp [list]: Diagonal components of the metric tensor
            coord_sys [list]: The coordinate system (cartesian, spherical, etc.)
            
        Returns:
            self.weyltensor_type [str]: Type of the Weyl Tensor. Default type is 'dddd'
            self.weyltensor_obj [sympy.tensor]: The Weyl Tensor, C_iklm
        """
        RicciScalar.__init__(self, diag_comp, coord_sys)
        self.weyltensor_type = 'dddd'
        weyl_tensor = MutableDenseNDimArray(zeros((self.ndim,)*4))
        riemanntensor_13 = self.get_riemanntensor()
        riemanntensor_04 = self.vary_riemanntensor_type(
            riemanntensor_13, 'dddd')
        for i, k, l, m in product(range(self.ndim), repeat=4):
            I_1 = (self.ndim-2)**(-1) * (self.riccitensor_obj[i, m]*self.metric_obj[k, l] - self.riccitensor_obj[i, l] *
                                         self.metric_obj[k, m] + self.riccitensor_obj[k, l]*self.metric_obj[i, m] - self.riccitensor_obj[k, m]*self.metric_obj[i, l])
            I_2 = ((self.ndim-1)*(self.ndim-2))**(-1) * self.ricciscalar_obj * \
                (self.metric_obj[i, l]*self.metric_obj[k, m] -
                 self.metric_obj[i, m]*self.metric_obj[k, l])
            weyl_tensor[i, k, l, m] = riemanntensor_04[i, k, l, m] + I_1 + I_2
        self.weyltensor_obj = Simplify(weyl_tensor)
            
    def get_weyltensor(self):
        """
        Returns the Weyl Tensor with respect to the given diagonal components
        """
        return self.weyltensor_obj

    def get_weyltensor_type(self):
        """
        Returns the type of the Weyl Tensor
        """
        return self.weyltensor_type

    def raise_index(self, xweyl_tensor):
        """
        Raising the first index of the Weyl Tensor

        Args:
            xweyl_tensor [sympy.tensor]: Given Weyl Tensor
        """
        return Array(einsum('iklm,ai->aklm', xweyl_tensor, self.inverse_metric_obj, optimize='optimal'))

    def raise_index1(self, xweyl_tensor):
        """
        Raising the second index of the Weyl Tensor

        Args:
            xweyl_tensor [sympy.tensor]: Given Weyl Tensor
        """
        return Array(einsum('aklm,bk->ablm', xweyl_tensor, self.inverse_metric_obj, optimize='optimal'))

    def raise_index2(self, xweyl_tensor):
        """
        Raising the third index of the Weyl Tensor

        Args:
            xweyl_tensor [sympy.tensor]: Given Weyl Tensor
        """
        return Array(einsum('ablm,cl->abcm', xweyl_tensor, self.inverse_metric_obj, optimize='optimal'))

    def raise_index3(self, xweyl_tensor):
        """
        Raising the fourth index of the Weyl Tensor

        Args:
            xweyl_tensor [sympy.tensor]: Given Weyl Tensor
        """
        return Array(einsum('abcm,md->abcd', xweyl_tensor, self.inverse_metric_obj, optimize='optimal'))

    def vary_weyltensor_type(self, xweyl_tensor, new_type):
        """
        Varying the type of the Weyl Tensor

        Args:
            xweyl_tensor [sympy.tensor]: Given Weyl Tensor
            new_type [str]: The new type of the Weyl Tensor. It should be given
            in terms of 'u': contravariant (upper-indices) and 'd': covariant (lower-indices)

        Raises:
            TypeError: If the type is given by wrong set of characters

        Returns:
            The new Weyl Tensor for a given type
        """
        self.weyltensor_type = new_type
        if new_type == 'dddd':
            return self.weyltensor_obj
        elif new_type in permutation_finder('uddd'):
            return Simplify(self.raise_index(xweyl_tensor))
        elif new_type in permutation_finder('uudd'):
            return Simplify(self.raise_index1(self.raise_index(xweyl_tensor)))
        elif new_type in permutation_finder('uuud'):
            return Simplify(self.raise_index2(self.raise_index1(self.raise_index(xweyl_tensor))))
        elif new_type == 'uuuu':
            return Simplify(self.raise_index3(self.raise_index2(self.raise_index1(self.raise_index(xweyl_tensor)))))
        else:
            raise TypeError(
                'Please enter a valid tensor type in terms of "u": contravariant and "d": covariant with 4 indices')
        
    def nonzero_weyltensor(self, xweyl_tensor):
        """
        Printing the nonzero components of the given Weyl Tensor
        
        Args:
            xweyl_tensor [sympy.tensor]: Given Weyl Tensor
        
        Returns:
            Non-zero components of the Weyl Tensor
        """
        if self.weyltensor_type == 'uuuu':
            for i, j, k, l in product(range(self.ndim), repeat=4):
                if xweyl_tensor[i, j, k, l] != 0:
                    display(Latex('$C^{{{0} {1} {2} {3}}}= {4}$'.format(latex(self.coord_sys[i]), latex(
                        self.coord_sys[j]), latex(self.coord_sys[k]), latex(self.coord_sys[l]), latex(xweyl_tensor[i, j, k, l]))))
        elif self.weyltensor_type in permutation_finder('uuud'):
            for i, j, k, l in product(range(self.ndim), repeat=4):
                if xweyl_tensor[i, j, k, l] != 0:
                    display(Latex('$C^{{{0} {1} {2}}}{{}}_{{{3}}}= {4}$'.format(latex(self.coord_sys[i]), latex(
                        self.coord_sys[j]), latex(self.coord_sys[k]), latex(self.coord_sys[l]), latex(xweyl_tensor[i, j, k, l]))))
        elif self.weyltensor_type in permutation_finder('uudd'):
            for i, j, k, l in product(range(self.ndim), repeat=4):
                if xweyl_tensor[i, j, k, l] != 0:
                    display(Latex('$C^{{{0} {1}}}{{}}_{{{2} {3}}}= {4}$'.format(latex(self.coord_sys[i]), latex(
                        self.coord_sys[j]), latex(self.coord_sys[k]), latex(self.coord_sys[l]), latex(xweyl_tensor[i, j, k, l]))))
        elif self.weyltensor_type in permutation_finder('uddd'):
            for i, j, k, l in product(range(self.ndim), repeat=4):
                if xweyl_tensor[i, j, k, l] != 0:
                    display(Latex('$C^{{{0}}}{{}}_{{{1} {2} {3}}} = {4}$'.format(latex(self.coord_sys[i]), latex(
                        self.coord_sys[j]), latex(self.coord_sys[k]), latex(self.coord_sys[l]), latex(xweyl_tensor[i, j, k, l]))))
        elif self.weyltensor_type == 'dddd':
            for i, j, k, l in product(range(self.ndim), repeat=4):
                if xweyl_tensor[i, j, k, l] != 0:
                    display(Latex('$C_{{{0} {1} {2} {3}}} = {4}$'.format(latex(self.coord_sys[i]), latex(
                        self.coord_sys[j]), latex(self.coord_sys[k]), latex(self.coord_sys[l]), latex(xweyl_tensor[i, j, k, l]))))


class TracelessRicciTensor(RicciScalar):
    def __init__(self, diag_comp, coord_sys):
        """ 
        Creating the Traceless Ricci Tensor class

        Args:
            diag_comp [list]: Diagonal components of the metric tensor
            coord_sys [list]: The coordinate system (cartesian, spherical, etc.)
            
        Returns:
            self.trclss_riccitensor_type [str]: Type of the Traceless Ricci Tensor. Default type is 'dd'
            self.trclss_riccitensor_obj [sympy.tensor]: The Traceless Ricci Tensor, Z_ij
                        
        """
        RicciScalar.__init__(self, diag_comp, coord_sys)
        self.trclss_riccitensor_type = 'dd'
        trclss_ricci_tensor = MutableDenseNDimArray(zeros((self.ndim,)*2))
        for i, k in product(range(self.ndim), repeat=2):
            trclss_ricci_tensor[i, k] = self.riccitensor_obj[i, k] - \
                (1/self.ndim) * self.ricciscalar_obj * self.metric_obj[i, k]
        self.trclss_riccitensor_obj = Simplify(trclss_ricci_tensor)

    def get_trclss_riccitensor(self):
        """
        Returns the Traceless Ricci Tensor with respect to the given diagonal components
        """
        return self.trclss_riccitensor_obj

    def get_trclss_riccitensor_type(self):
        """
        Returns the type of the Traceless Ricci Tensor
        """
        return self.trclss_riccitensor_type

    def raise_index(self, xtrclss_riccitensor):
        """
        Raising the index of the Traceless Ricci Tensor

        Args:
            xtrclss_ricci_tensor [sympy.tensor]: Given Traceless Ricci Tensor  
        """
        return Array(einsum('ij,jk->ki', xtrclss_riccitensor, self.inverse_metric_obj, optimize='optimal'))

    def vary_trclss_riccitensor_type(self, xtrclss_riccitensor, new_type):
        """
        Varying the type of the Traceless Ricci Tensor

        Args:
            xtrclss_ricci_tensor [sympy.tensor]: Given Traceless Ricci Tensor
            new_type [str]: The new type of the Traceless Ricci Tensor. It should be given
            in terms of 'u': contravariant (upper-indices) and 'd': covariant (lower-indices)

        Raises:
            TypeError: If the type is given by wrong set of characters

        Returns:
            The new Traceless Ricci Tensor for a given type
        """
        self.trclss_riccitensor_type = new_type
        if new_type == 'dd':
            return self.trclss_riccitensor_obj
        elif new_type in permutation_finder('ud'):
            return Simplify(self.raise_index(xtrclss_riccitensor))
        elif new_type == 'uu':
            return Simplify(self.raise_index(self.raise_index(xtrclss_riccitensor)))
        else:
            raise TypeError(
                'Please enter a valid tensor type in terms of "u": contravariant and "d": covariant with 4 indices')


class EinsteinTensor(RicciScalar):
    def __init__(self, diag_comp, coord_sys):
        """
        Creating the Einstein Tensor class

        Args:
            diag_comp [list]: Diagonal components of the metric tensor
            coord_sys [list]: The coordinate system (cartesian, spherical, etc.)
            
        Returns:
            self.einsteintensor_type [str]: Type of the Einstein Tensor. Default type is 'dd'
            self.einsteintensor_obj [sympy.tensor]: The Einstein Tensor, G_ij           
        """
        RicciScalar.__init__(self, diag_comp, coord_sys)
        self.einsteintensor_type = 'dd'
        einstein_tensor = MutableDenseNDimArray(zeros((self.ndim,)*2))
        for i, k in product(range(self.ndim), repeat=2):
            einstein_tensor[i, k] = self.riccitensor_obj[i, k] - \
                (1/2) * self.ricciscalar_obj * self.metric_obj[i, k]
        self.einsteintensor_obj = Simplify(einstein_tensor)

    def get_einsteintensor(self):
        """
        Returns the Einstein Tensor with respect to the given diagonal components
        """
        return self.einsteintensor_obj

    def get_einsteintensor_type(self):
        """
        Returns the type of the Einstein Tensor 
        """
        return self.einsteintensor_type

    def raise_index(self, xeinstein_tensor):
        """
        Raising the index of the Einstein Tensor

        Args:
            xeinstein_tensor [sympy.tensor]: Given Einstein Tensor  
        """
        return Array(einsum('ij,jk->ki', xeinstein_tensor, self.inverse_metric_obj, optimize='optimal'))

    def vary_einsteintensor_type(self, xeinstein_tensor, new_type):
        """
        Varying the type of the Einstein Tensor

        Args:
            xeinstein_tensor [sympy.tensor]: Given Einstein Tensor
            new_type [str]: The new type of the Einstein Tensor. It should be given
            in terms of 'u': contravariant (upper-indices) and 'd': covariant (lower-indices)

        Raises:
            TypeError: If the type is given by wrong set of characters

        Returns:
            The new Einstein Tensor for a given type
        """
        self.einsteintensor_type = new_type
        if new_type == 'dd':
            return self.einsteintensor_obj
        elif new_type in permutation_finder('ud'):
            return Simplify(self.raise_index(xeinstein_tensor))
        elif new_type == 'uu':
            return Simplify(self.raise_index(self.raise_index(xeinstein_tensor)))
        else:
            raise TypeError(
                'Please enter a valid tensor type in terms of "u": contravariant and "d": covariant with 4 indices')


class KretschmannScalar(RiemannTensor):
    def __init__(self, diag_comp, coord_sys):
        """
        Creating the Kretschmann Scalar class

        Args:
            diag_comp [list]: Diagonal components of the metric tensor
            coord_sys [list]: The coordinate system (cartesian, spherical, etc.)
            
        Returns:
            self.kretschmannscalar_obj [int/symbol]: The Kretschmann Scalar, K
        """
        RiemannTensor.__init__(self, diag_comp, coord_sys)
        riemanntensor_13 = self.get_riemanntensor()
        riemanntensor_04 = self.vary_riemanntensor_type(
            riemanntensor_13, 'dddd')
        riemanntensor_40 = self.vary_riemanntensor_type(
            riemanntensor_13, 'uuuu')
        kretschmann_scalar =  0
        for a, b, c, d in product(range(self.ndim), repeat=4):
            kretschmann_scalar += riemanntensor_04[a, b, c, d] * riemanntensor_40[a, b, c, d]
        self.kretschmannscalar_obj = simplify(kretschmann_scalar) 

    def get_kretschmannscalar(self):
        """
        Returns the KretschmannScalar with respect to the given diagonal components
        """
        return self.kretschmannscalar_obj

############################################################################
