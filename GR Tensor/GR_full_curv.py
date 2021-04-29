from IPython.display import Latex, display
from sympy import *
from numpy import zeros, sign
from itertools import product, permutations


def permutation_finder(tensor_type):
    """
    Permuting tensor indices for a given tensor type.
    
    Args:
        tensor_type [string]: The type of the tensor. 
        It's given in terms of 'u' (contravariant) and 'd' (covariant).

    Returns:
        unique_permutations [set]: Unique permutations of the tensor indices
    
    Example: 
    >>> permutation_finder('udd')
    >>> ['udd', 'dud','ddu']
    """
    permt_list = list(permutations(tensor_type))
    unique_permutations = set([''.join(i) for i in permt_list])
    return unique_permutations


def Simplify(xtensor):
    """
    Simplifying the tensors via sympy s methods
    
    Args:
        xtensor [ndim-array]: The given tensor

    Returns:
        Simplified version of the tensor
    """
    return nsimplify(xtensor)


def derivative_of_metric(coord_sys, xmetric, i, j, k):
    """
    Taking the partial derivative of a given metric: \partial_i(g_jk)
    where g_jk is the metric and the \partial_i is the partial derivative with respect 
    to i'th component 
    
    Args:
        coord_sys [symbol]: The chosen coordinate system for the space-time (cartesian, spherical, etc.)
        xmetric [ndim-array]: The metric tensor, g_jk
        i,j,k [symbol]: Indices that runs from 0-ndim
        
    Returns: 
        The partial derivative of g_jk with respect to the [i]'th component
    """
    expr = xmetric[j, k]
    return Simplify(diff(expr, coord_sys[i]))


def derivative_of_chris(coord_sys, xchris_symb, i, j, k, l):
    """
    Taking the derivative of a given christoffel symbol; \partial_i (\Gamma^j_kl)
    where \Gamma^j_kl is the christoffel symbol and the \partial_i is the partial derivative 
    with respect to i'th component 
    
    Args:
        coord_sys [symbol]: The chosen coordinate system for the space-time (cartesian, spherical, etc.)
        xchris_symb [ndim-array]: The Christoffel Symbol C^j_kl
        i,j,k,l [symbol]: Indices that runs from 0-ndim
        
    Returns: 
        The partial derivative of C^j_kl with respect to the [i]'th component
    """
    expr = xchris_symb[j, k, l]
    return Simplify(diff(expr, coord_sys[i]))


class MetricTensor(object):
    def __init__(self, diag_comp, coord_sys):
        """
        Creating the metric tensor
        
        Args:
            coord_sys [symbol]: The chosen coordinate system (cartesian, spherical, etc.)
            diag_comp [list]: Diagonal components of the metric tensor

        Returns:
            self.diag_comp [list]: Diagonal components of the metric tensor
            self.coord_sys [symbol]: Chosen coordinate system
            self.metric_obj [ndim-array]: The metric tensor, g_mn
            self.metric_type [string]: Type of the metric tensor. Default type is 'dd'
            self.ndim [int]: Dimension of the space. It can be 2,3 or 4
            self.inverse_metric_obj [ndim-array]: The inverse of the metric tensor, g^mn
        
        Raises:
            ValueError: If the dimension of the space is not between 1 and 5
        """
        self.diag_comp = diag_comp
        self.coord_sys = coord_sys
        if 1 < len(diag_comp) < 5:
            self.ndim = len(diag_comp)
        else:
            raise ValueError('The dimension of the space can only be 2,3 or 4')
        self.metric_type = 'dd'
        metric_tensor = MutableSparseNDimArray(zeros((self.ndim,)*2))
        inverse_metric = MutableSparseNDimArray(zeros((self.ndim,)*2))
        for i in range(self.ndim):
            metric_tensor[i, i] = self.diag_comp[i]
            inverse_metric[i, i] = 1 / self.diag_comp[i]
        self.metric_obj = Simplify(metric_tensor)
        self.inverse_metric_obj = Simplify(inverse_metric)


    def get_metrictensor(self):
        """
        Returns the metric tensor w.r.t the given diagonal components
        """
        return self.metric_obj


    def get_type(self):
        """
        Returns the type of the metric tensor 
        """
        return self.metric_type


    def get_inverse_metrictensor(self):
        """
        Returns the inverse of the metric tensor
        """
        return self.inverse_metric_obj


    def raise_index(self, xmetric_tensor):
        """
        Raising the index of the metric tensor

        Args:
            xmetric_tensor [ndim-array]: The metric tensor  

        Returns:
            new_metric_tensor [ndim-array]: The metric tensor with a raised index
        """
        new_metric_tensor = MutableSparseNDimArray(zeros((self.ndim,)*2))
        for i, k in product(range(self.ndim), repeat=2):
            einstein_sum = 0
            for j in range(self.ndim):
                einstein_sum += xmetric_tensor[i,j] * self.inverse_metric_obj[j, k]
            new_metric_tensor[k, i] = einstein_sum
        return new_metric_tensor


    def vary_type(self, xmetric_tensor, new_type):
        """
        Varying the type of the metric tensor 
        
        Args:
            xmetric_tensor [ndim-array]: The given metric tensor
            new_type [string]: The new type of the metric tensor. It should be in terms of 
            'u': contravariant (upper-indices) and 'd': covariant (lower-indices)

        Raises:
            TypeError: If the type is given by wrong set of characters

        Returns:
            The new metric tensor with a given type
        """
        if new_type == 'dd':
            self.metric_type = new_type
            return self.metric_obj
        elif new_type in permutation_finder('ud'):
            self.metric_type = new_type
            return self.raise_index(xmetric_tensor)
        elif new_type == 'uu':
            self.metric_type = new_type
            return self.raise_index(self.raise_index(xmetric_tensor))
        else:
            raise TypeError('Please enter a valid tensor type in terms of "u": contravariant and "d": covariant')


class ChristoffelSymbol(MetricTensor):
    def __init__(self, diag_comp, coord_sys):
        """
        Creating the Christoffel Symbol 
        
        Args:
            coord_sys [symbol]: The chosen coordinate system (cartesian, spherical, etc.)
            diag_comp [list]: Diagonal components of the metric tensor

        Returns:
            self.chris_obj [ndim-array]: The Christoffel Symbol, C^m_ij
            self.chris_type [string]: The type of the Christoffel Symbol. The default type is 'udd'
        """
        MetricTensor.__init__(self, diag_comp, coord_sys)
        self.chris_type = 'udd'
        chris_sym = MutableSparseNDimArray(zeros((self.ndim,)*3))
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
        Returns the Christoffel Symbol w.r.t the given diagonal components
        """
        return self.chris_obj


    def get_type(self):
        """
        Returns the type of the Christoffel Symbol
        """
        return self.chris_type


    def raise_index(self, xchris_symbol):
        """
        Raising the index of the Christoffel Symbol

        Args:
            xchris_symbol [ndim-array]: The Christoffel Symbol

        Returns:
            new_chris_symbol [ndim-array]: The Christoffel Symbol with a raised index
        """
        new_chris_symbol = MutableSparseNDimArray(zeros((self.ndim,)*3))
        for i, m, k in product(range(self.ndim), repeat=3):
            einstein_sum = 0
            for j in range(self.ndim):
                einstein_sum += xchris_symbol[i, k, j] * self.inverse_metric_obj[j, m]
            new_chris_symbol[i, m, k] = einstein_sum
        return new_chris_symbol


    def raise_index1(self, xchris_symbol):
        """
        Raising the second index of the Christoffel Symbol

        Args:
            xchris_symbol [ndim-array]: The Christoffel Symbol

        Returns:
             new_chris_symbol [ndim-array]: The Christoffel Symbol with a raised index
        """
        new_chris_symbol = MutableSparseNDimArray(zeros((self.ndim,)*3))
        for i, m, n in product(range(self.ndim), repeat=3):
            einstein_sum = 0
            for k in range(self.ndim):
                einstein_sum += xchris_symbol[i, m, k] * self.inverse_metric_obj[k, n]
            new_chris_symbol[i, m, n] = einstein_sum
        return new_chris_symbol


    def lower_index(self, xchris_symbol):
        """
        Lowering the index of the Christoffel Symbol

        Args:
            xchris_symbol [ndim-array]: Given Christoffel Symbol

        Returns:
            new_chris_symbol [ndim-array]: The Christoffel Symbol with a lowered index
        """
        new_chris_symbol = MutableSparseNDimArray(zeros((self.ndim,)*3))
        for l, j, k in product(range(self.ndim), repeat=3):
            einstein_sum = 0
            for i in range(self.ndim):
                einstein_sum += xchris_symbol[i, j, k] * self.metric_obj[i, l]
            new_chris_symbol[l, j, k] = einstein_sum
        return new_chris_symbol


    def vary_type(self, xchris_symbol, new_type):
        """
        Varying the type of the Christoffel Symbol

        Args:
            xchris_symbol [ndim-array]: The given Christoffel Symbol
            new_type [string]: The new type of the Christoffel Symbol. It should be given 
            in terms of 'u': contravariant (upper-indices) and 'd': covariant (lower-indices)

        Raises:
            TypeError: If the type is given by wrong set of characters

        Returns:
            The new Christoffel Symbol with a given type
        """
        if new_type == 'ddd':
            self.chris_type = new_type
            return self.lower_index(xchris_symbol)
        elif new_type in permutation_finder('udd'):
            self.chris_type = new_type
            return self.chris_obj
        elif new_type in permutation_finder('uud'):
            self.chris_type = new_type
            return self.raise_index(xchris_symbol)
        elif new_type == 'uuu':
            self.chris_type = new_type
            return self.raise_index1(self.raise_index(xchris_symbol))
        else:
            raise TypeError('Please enter a valid tensor type in terms of "u": contravariant and "d": covariant')


    def nonzero_christoffelsymbol(self, xchris_symbol):
        """
        Printing the nonzero components of the Christoffel Symbol
        """
        for i, j, k in product(range(self.ndim), repeat=3):
            if xchris_symbol[i, j, k] != 0:
                display(Latex('$\\Gamma^{{{0}}}{{}}_{{{1} {2}}} = {3}$'.format(latex(self.coord_sys[i]), latex(self.coord_sys[j]),latex(self.coord_sys[k]), latex(xchris_symbol[i, j, k]))))


class RiemannTensor(ChristoffelSymbol):
    def __init__(self, diag_comp, coord_sys):
        """ 
        Creating a Riemann Tensor 
        
        Args:
            coord_sys [symbol]: The chosen coordinate system (cartesian, spherical, etc.)
            diag_comp [list]: Diagonal components of the metric tensor

        Returns:
            self.riemann_obj [ndim-array]: The Riemann Tensor, R^l_ijk
            self.riemann_type [string]: The type of the Riemann Tensor. The default type is 'uddd'
        """
        ChristoffelSymbol.__init__(self, diag_comp, coord_sys)
        self.riemann_type = 'uddd'
        riemann_tensor = MutableSparseNDimArray(zeros((self.ndim,)*4))
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
        Returns the Riemann Tensor w.r.t the given diagonal components
        """
        return self.riemann_obj

    def get_type(self):
        """
        Returns the type of the Riemann Tensor
        """
        return self.riemann_type

    def lower_index(self, xriemann_tensor):
        """
        Lowering the index of the Riemann Tensor

        Args:
            xriemann_tensor [ndim-array]: Given Riemann Tensor

        Returns:
            new_riemann_tensor [ndim-array]: The Riemann Tensor with a lowered index
        """
        new_riemann_tensor = MutableSparseNDimArray(zeros((self.ndim,)*4))
        for k, b, c, d in product(range(self.ndim), repeat=4):
            einstein_sum = 0
            for a in range(self.ndim):
                einstein_sum += xriemann_tensor[a,b, c, d] * self.metric_obj[a, k]
            new_riemann_tensor[k, b, c, d] = einstein_sum
        return new_riemann_tensor

    def raise_index(self, xriemann_tensor):
        """
        Raising the first index of the Riemann Tensor

        Args:
            xriemann_tensor [ndim-array]: Given Riemann Tensor

        Returns:
            new_riemann_tensor [ndim-array]: The Riemann Tensor with a raised index
        """
        new_riemann_tensor = MutableSparseNDimArray(zeros((self.ndim,)*4))
        for a, k, c, d in product(range(self.ndim), repeat=4):
            einstein_sum = 0
            for b in range(self.ndim):
                einstein_sum += xriemann_tensor[a, b,
                                                c, d] * self.inverse_metric_obj[b, k]
            new_riemann_tensor[a, k, c, d] = einstein_sum
        return new_riemann_tensor

    def raise_index1(self, xriemann_tensor):
        """
        Raising the second index of the Riemann Tensor

        Args:
            xriemann_tensor [ndim-array]: Given Riemann Tensor

        Returns:
            new_riemann_tensor [ndim-array]: The Riemann Tensor with a raised index
        """
        new_riemann_tensor = MutableSparseNDimArray(zeros((self.ndim,)*4))
        for a, k, l, d in product(range(self.ndim), repeat=4):
            einstein_sum = 0
            for c in range(self.ndim):
                einstein_sum += xriemann_tensor[a, k,
                                                c, d] * self.inverse_metric_obj[c, l]
            new_riemann_tensor[a, k, l, d] = einstein_sum
        return new_riemann_tensor

    def raise_index2(self, xriemann_tensor):
        """
        Raising the third index of the Riemann Tensor

        Args:
            xriemann_tensor [ndim-array]: Given Riemann Tensor

        Returns:
            new_riemann_tensor [ndim-array]: The Riemann Tensor with a raised index
        """
        new_riemann_tensor = MutableSparseNDimArray(zeros((self.ndim,)*4))
        for a, k, l, f in product(range(self.ndim), repeat=4):
            einstein_sum = 0
            for d in range(self.ndim):
                einstein_sum += xriemann_tensor[a, k,
                                                l, d] * self.inverse_metric_obj[d, f]
            new_riemann_tensor[a, k, l, f] = einstein_sum
        return new_riemann_tensor

    def vary_type(self, xriemann_tensor, new_type):
        """
        Varying the type of the Riemann Tensor

        Args:
            xriemann_tensor [ndim-array]: The given Riemann Tensor
            new_type [string]: The new type of the Riemann Tensor. It should be given
            in terms of 'u': contravariant (upper-indices) and 'd': covariant (lower-indices)

        Raises:
            TypeError: If the type is given by wrong set of characters

        Returns:
            The new Riemann Tensor with a given type
        """
        if new_type == 'dddd':
            self.riemann_type = new_type
            return self.lower_index(xriemann_tensor)
        elif new_type in permutation_finder('uddd'):
            self.riemann_type = new_type
            return self.riemann_obj
        elif new_type in permutation_finder('uudd'):
            self.riemann_type = new_type
            return self.raise_index(xriemann_tensor)
        elif new_type in permutation_finder('uuud'):
            self.riemann_type = new_type
            return self.raise_index1(self.raise_index(xriemann_tensor))
        elif new_type == 'uuuu':
            self.riemann_type = new_type
            return self.raise_index2(self.raise_index1(self.raise_index(xriemann_tensor)))
        else:
            raise TypeError(
                'Please enter a valid tensor type in terms of "u": contravariant and "d": covariant')


class RicciTensor(RiemannTensor):
    def __init__(self, diag_comp, coord_sys):
        """ 
        Creating a Ricci Tensor 
        
        Args:
            coord_sys [symbol]: The chosen coordinate system (cartesian, spherical, etc.)
            diag_comp [list]: Diagonal components of the metric tensor

        Returns:
            self.riccitensor_obj [ndim-array]: The Ricci Tensor, R_ik
            self.riccitensor_type [string]: The type of the Ricci Tensor. The default type is 'dd'            
        """
        RiemannTensor.__init__(self, diag_comp ,coord_sys)
        self.riccitensor_type = 'dd'
        ricci_tensor = MutableSparseNDimArray(zeros((self.ndim,)*2))
        for i, k in product(range(self.ndim), repeat=2):
            einstein_sum = 0
            for j in range(self.ndim):
                einstein_sum += self.riemann_obj[j, i, j, k]
            ricci_tensor[i, k] = einstein_sum
        self.riccitensor_obj = Simplify(ricci_tensor)


    def get_riccitensor(self):
        """
        Returns the Ricci Tensor w.r.t the given diagonal components
        """
        return self.riccitensor_obj


    def get_type(self):
        """
        Returns the type of the Ricci Tensor
        """
        return self.riccitensor_type


    def raise_index(self, xricci_tensor):
        """
        Raising the index of the Ricci Tensor

        Args:
            xricci_tensor [ndim-array]: The Ricci Tensor  

        Returns:
            new_ricci_tensor [ndim-array]: The Ricci Tensor with a raised index
        """
        new_ricci_tensor = MutableSparseNDimArray(zeros((self.ndim,)*2))
        for k, i in product(range(self.ndim), repeat=2):
            einstein_sum = 0
            for j in range(self.ndim):
                einstein_sum += xricci_tensor[i,
                    j] * self.inverse_metric_obj[j, k]
            new_ricci_tensor[k, i] = einstein_sum
        return new_ricci_tensor


    def vary_type(self, xricci_tensor, new_type):
        """
        Varying the type of the Ricci Tensor

        Args:
            xricci_tensor [ndim-array]: The given Ricci Tensor
            new_type [string]: The new type of the Ricci Tensor. It should be given
            in terms of 'u': contravariant (upper-indices) and 'd': covariant (lower-indices)

        Raises:
            TypeError: If the type is given by wrong set of characters

        Returns:
            The new Ricci Tensor with a given type
        """
        if new_type == 'dd':
            self.riccitensor_type = new_type
            return self.riccitensor_obj
        elif new_type in permutation_finder('ud'):
            self.riccitensor_type = new_type
            return self.raise_index(xricci_tensor)
        elif new_type == 'uu':
            self.riccitensor_type = new_type
            return self.raise_index(self.raise_index(xricci_tensor))
        else:
            raise TypeError(
                'Please enter a valid tensor type in terms of "u": contravariant and "d": covariant')


class RicciScalar(RicciTensor):
    def __init__(self, diag_comp, coord_sys):
        """ 
        Creating a Ricci Scalar 
    
        Args:
            coord_sys [symbol]: The chosen coordinate system (cartesian, spherical, etc.)
            diag_comp [list]: Diagonal components of the metric tensor

        Returns:
            self.ricciscalar_obj [int/symbol]: The Ricci Scalar, R           
        """
        RicciTensor.__init__(self, diag_comp, coord_sys)
        ricci_scalar = 0
        for i, k in product(range(self.ndim), repeat=2):
            ricci_scalar += self.inverse_metric_obj[i,
                k] * self.riccitensor_obj[i, k]
        self.ricciscalar_obj = Simplify(ricci_scalar)


    def get_ricciscalar(self):
        """
        Returns the Ricci Scalar
        """
        return self.ricciscalar_obj


class TracelessRicciTensor(RicciScalar):
    def __init__(self, diag_comp, coord_sys):
        """ 
        Creating a Traceless Ricci Tensor
        
        Args:
            coord_sys [symbol]: The chosen coordinate system (cartesian, spherical, etc.)
            diag_comp [list]: Diagonal components of the metric tensor

        Returns:
            self.trclss_riccitensor_obj [ndim-array]: The Traceless Ricci Tensor, Z_ij
            self.trclss_riccitensor_type [string]: The type of the Traceless Ricci Tensor. The default type is 'dd'            
        """
        self.trclss_riccitensor_type = 'dd'
        RicciScalar.__init__(self, diag_comp, coord_sys)
        trclss_ricci_tensor = MutableSparseNDimArray(zeros((self.ndim,)*2))
        for i, k in product(range(self.ndim), repeat=2):
            trclss_ricci_tensor[i, k] = self.riccitensor_obj[i, k] - \
                (1/self.ndim) * self.ricciscalar_obj * self.metric_obj[i, k]
        self.trclss_riccitensor_obj = Simplify(trclss_ricci_tensor)


    def get_trclss_riccitensor(self):
        """
        Returns the Traceless Ricci Tensor w.r.t the given diagonal components
        """
        return self.trclss_riccitensor_obj


    def get_type(self):
        """
        Returns the type of the Traceless Ricci Tensor
        """
        return self.trclss_riccitensor_type


    def raise_index(self, xtrclss_riccitensor):
        """
        Raising the index of the Traceless Ricci Tensor

        Args:
            xtrclss_ricci_tensor [ndim-array]: Traceless Ricci Tensor  

        Returns:
            new_trclss_riccitensor [ndim-array]: The Traceless Ricci Tensor with a raised index
        """
        new_trclss_riccitensor = MutableSparseNDimArray(zeros((self.ndim,)*2))
        for k, i in product(range(self.ndim), repeat=2):
            einstein_sum = 0
            for j in range(self.ndim):
                einstein_sum += xtrclss_riccitensor[i,
                    j] * self.inverse_metric_obj[j, k]
            new_trclss_riccitensor[k, i] = einstein_sum
        return new_trclss_riccitensor


    def vary_type(self, xtrclss_riccitensor, new_type):
        """
        Varying the type of the Traceless Ricci Tensor

        Args:
            xtrclss_ricci_tensor [ndim-array]: The given Traceless Ricci Tensor
            new_type [string]: The new type of the Traceless Ricci Tensor. It should be given
            in terms of 'u': contravariant (upper-indices) and 'd': covariant (lower-indices)

        Raises:
            TypeError: If the type is given by wrong set of characters

        Returns:
            The new Traceless Ricci Tensor with a given type
        """
        if new_type == 'dd':
            self.trclss_riccitensor_type = new_type
            return self.trclss_riccitensor_obj
        elif new_type in permutation_finder('ud'):
            self.trclss_riccitensor_type = new_type
            return self.raise_index(xtrclss_riccitensor)
        elif new_type == 'uu':
            self.trclss_riccitensor_type = new_type
            return self.raise_index(self.raise_index(xtrclss_riccitensor))
        else:
            raise TypeError(
                'Please enter a valid tensor type in terms of "u": contravariant and "d": covariant')


class EinsteinTensor(RicciScalar):
    def __init__(self, diag_comp, coord_sys):
        """
        Creating an Einstein Tensor
        
        Args:
            coord_sys [symbol]: The chosen coordinate system (cartesian, spherical, etc.)
            diag_comp [list]: Diagonal components of the metric tensor

        Returns:
            self.einsteintensor_obj [ndim-array]: The Einstein Tensor, G_ij
            self.einsteintensor_type [string]: The type of the Einstein Tensor. The default type is 'dd'            
        """
        RicciScalar.__init__(self, diag_comp, coord_sys)
        self.einsteintensor_type = 'dd'
        einstein_tensor = MutableSparseNDimArray(zeros((self.ndim,)*2))
        for i, k in product(range(self.ndim), repeat=2):
            einstein_tensor[i, k] = self.riccitensor_obj[i, k] - \
                (1/2) * self.ricciscalar_obj * self.metric_obj[i, k]
        self.einsteintensor_obj = Simplify(einstein_tensor)


    def get_einsteintensor(self):
        """
        Returns the Einstein Tensor w.r.t the given diagonal components
        """
        return self.einsteintensor_obj


    def get_type(self):
        """
        Returns the type of the Einstein Tensor 
        """
        return self.einsteintensor_type


    def raise_index(self, xeinstein_tensor):
        """
        Raising the index of the Einstein Tensor

        Args:
            xeinstein_tensor [ndim-array]: The Einstein Tensor  

        Returns:
            [ndim-array]: The Einstein Tensor with a raised index
        """
        new_einstein_tensor = MutableSparseNDimArray(zeros((self.ndim,)*2))
        for k, i in product(range(self.ndim), repeat=2):
            einstein_sum = 0
            for j in range(self.ndim):
                einstein_sum += xeinstein_tensor[i,j] * self.inverse_metric_obj[j, k]
            new_einstein_tensor[k, i] = einstein_sum
        return new_einstein_tensor 


    def vary_type(self, xeinstein_tensor, new_type):
        """
        Varying the type of the Einstein Tensor

        Args:
            xeinstein_tensor [ndim-array]: The given Einstein Tensor
            new_type [string]: The new type of the Einstein Tensor. It should be given
            in terms of 'u': contravariant (upper-indices) and 'd': covariant (lower-indices)

        Raises:
            TypeError: If the type is given by wrong set of characters

        Returns:
            The new Einstein Tensor with a given type
        """
        if new_type == 'dd':
            self.einsteintensor_type = new_type
            return self.einsteintensor_obj
        elif new_type in permutation_finder('ud'):
            self.einsteintensor_type  = new_type
            return self.raise_index(xeinstein_tensor)
        elif new_type == 'uu':
            self.einsteintensor_type = new_type
            return self.raise_index(self.raise_index(xeinstein_tensor))
        else:
            raise TypeError(
                'Please enter a valid tensor type in terms of "u": contravariant and "d": covariant')
