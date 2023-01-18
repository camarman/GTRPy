from itertools import product
from numpy import einsum, zeros
from sympy import Array, MutableDenseNDimArray, diff

from gtrpy.src.grtensors.metrictensor import MetricTensor
from gtrpy.tools.simplify_objects import Simplify


def derivative_of_metric(coord_sys, metric_tensor, k, i, j):
    """
    Taking the partial derivative of a given metric tensor [g_ij] with respect to the
    [k]'th component

    Args:
        coord_sys     [list]        : The coordinate system given as a list (e.g., [t,x,y,z])
        metric_tensor [sympy.tensor]: Given metric tensor, g_ij
        k,i,j         [int]         : Coordinate indices (0-ndim)
    """
    return Simplify(diff(metric_tensor[i, j], coord_sys[k]))


class ChristoffelSymbol(MetricTensor):
    def __init__(self, metric_tensor, coord_sys):
        """
        Creating the Christoffel symbol object

        Args:
            metric_tensor [list]: The metric tensor, provided by the user
            coord_sys     [list]: The coordinate system given as a list (e.g., [t,x,y,z])

        Returns:
            self.chris_type [str]         : Type of the Christoffel symbol. Default type is 'udd'
            self.chris_obj  [sympy.tensor]: The Christoffel symbol, Gamma^k_ij
        """
        MetricTensor.__init__(self, metric_tensor, coord_sys)
        self.chris_type = 'udd'
        chris_sym = MutableDenseNDimArray(zeros((self.ndim,)*3))
        for k, i, j in product(range(self.ndim), repeat=3):
            einstein_sum = 0
            for l in range(self.ndim):
                I1 = derivative_of_metric(self.coord_sys, self.metric_obj, j, l, i)
                I2 = derivative_of_metric(self.coord_sys, self.metric_obj, i, l, j)
                I3 = derivative_of_metric(self.coord_sys, self.metric_obj, l, i, j)
                S = I1 + I2 - I3
                einstein_sum += 1/2 * self.inverse_metric_obj[k, l] * S
            chris_sym[k, i, j] = einstein_sum
        self.chris_obj = chris_sym


    def get_christoffelsymbol(self):
        """
        Returns the Christoffel symbol object
        """
        return Simplify(self.chris_obj)


    def get_christoffelsymbol_type(self):
        """
        Returns the type of the Christoffel symbol
        """
        return self.chris_type


    def lower_index(self, xchris_symbol):
        """
        Lowering the index of the Christoffel symbol

        Args:
            xchris_symbol [sympy.tensor]: Given Christoffel symbol
        """
        return Array(einsum('kij,kl->ijl', xchris_symbol, self.metric_obj, optimize='optimal'))


    def raise_index(self, xchris_symbol):
        """
        Raising the index of the Christoffel symbol

        Args:
            xchris_symbol [sympy.tensor]: Given Christoffel symbol
        """
        return Array(einsum('kij,il->klj', xchris_symbol, self.inverse_metric_obj, optimize='optimal'))


    def raise_index1(self, xchris_symbol):
        """
        Raising the second index of the Christoffel symbol

        Args:
            xchris_symbol [sympy.tensor]: Given Christoffel symbol
        """
        return Array(einsum('klj,jm->klm', xchris_symbol, self.inverse_metric_obj, optimize='optimal'))


    def vary_christoffelsymbol_type(self, new_type):
        """
        Varying the type of the Christoffel symbol

        Args:
            new_type [str]: The new type of the Christoffel symbol.
                            It should be given in terms of:
                            'u': contravariant (upper-indices)
                            'd': covariant (lower-indices)

        Returns:
            The new Christoffel symbol for a given type
        """
        self.chris_type = new_type
        if new_type == 'ddd':
            return Simplify(self.lower_index(self.chris_obj))
        elif new_type == 'udd':
            return Simplify(self.chris_obj)
        elif new_type == 'uud':
            return Simplify(self.raise_index(self.chris_obj))
        elif new_type == 'uuu':
            return Simplify(self.raise_index1(self.raise_index(self.chris_obj)))
