from itertools import product

from numpy import einsum, zeros
from objects.grtensors.metrictensor import MetricTensor
from objects.simplifyobjects import Simplify
from sympy import Array, MutableDenseNDimArray, diff


def derivative_of_metric(coord_sys, metric_tensor, i, j, k):
    """
    Taking the partial derivative of a given metric tensor [g_jk] with respect to the
    [i]'th component

    Args:
        coord_sys [list]: The coordinate system given as a list (e.g., [t,x,y,z])
        metric_tensor [sympy.tensor]: Given metric tensor, g_jk
        i,j,k [int]: Coordinate indices; (0-ndim)
    """
    return Simplify(diff(metric_tensor[j, k], coord_sys[i]))


class ChristoffelSymbol(MetricTensor):
    def __init__(self, metric_tensor, coord_sys):
        """
        Creating the christoffel symbol object

        Args:
            metric_tensor [list]: The metric tensor, provided by the user
            coord_sys [list]: The coordinate system given as a list (e.g., [t,x,y,z])

        Returns:
            self.chris_type [str]: Type of the christoffel symbol. Default type is 'udd'
            self.chris_obj [sympy.tensor]: The christoffel symbol, Gamma^m_ij
        """
        MetricTensor.__init__(self, metric_tensor, coord_sys)
        self.chris_type = 'udd'
        chris_sym = MutableDenseNDimArray(zeros((self.ndim,)*3))
        for m, i, j in product(range(self.ndim), repeat=3):
            einstein_sum = 0
            for k in range(self.ndim):
                I1 = derivative_of_metric(
                    self.coord_sys, self.metric_obj, j, k, i)
                I2 = derivative_of_metric(
                    self.coord_sys, self.metric_obj, i, k, j)
                I3 = derivative_of_metric(
                    self.coord_sys, self.metric_obj, k, i, j)
                S = I1 + I2 - I3
                einstein_sum += 1/2 * self.inverse_metric_obj[m, k] * S
            chris_sym[m, i, j] = einstein_sum
        self.chris_obj = chris_sym

    def get_christoffelsymbol(self):
        """
        Returns the christoffel symbol object
        """
        return Simplify(self.chris_obj)

    def get_christoffelsymbol_type(self):
        """
        Returns the type of the christoffel symbol
        """
        return self.chris_type

    def lower_index(self, xchris_symbol):
        """
        Lowering the index of the christoffel symbol

        Args:
            xchris_symbol [sympy.tensor]: Given christoffel symbol
        """
        return Array(einsum('ijk,il->ljk', xchris_symbol, self.metric_obj, optimize='optimal'))

    def raise_index(self, xchris_symbol):
        """
        Raising the index of the christoffel symbol

        Args:
            xchris_symbol [sympy.tensor]: Given christoffel symbol
        """
        return Array(einsum('ikj,jm->imk', xchris_symbol, self.inverse_metric_obj, optimize='optimal'))

    def raise_index1(self, xchris_symbol):
        """
        Raising the second index of the christoffel symbol

        Args:
            xchris_symbol [sympy.tensor]: Given christoffel symbol
        """
        return Array(einsum('imk,kn->imn', xchris_symbol, self.inverse_metric_obj, optimize='optimal'))

    def vary_christoffelsymbol_type(self, xchris_symbol, new_type):
        """
        Varying the type of the christoffel symbol

        Args:
            xchris_symbol [sympy.tensor]: Given christoffel symbol
            new_type [str]: The new type of the christoffel symbol. It should be given
            in terms of 'u': contravariant (upper-indices) and 'd': covariant (lower-indices)

        Returns:
            The new christoffel symbol for a given type
        """
        self.chris_type = new_type
        if new_type == 'ddd':
            return Simplify(self.lower_index(xchris_symbol))
        elif new_type == 'udd':
            return Simplify(self.chris_obj)
        elif new_type == 'uud':
            return Simplify(self.raise_index(xchris_symbol))
        elif new_type == 'uuu':
            return Simplify(self.raise_index1(self.raise_index(xchris_symbol)))
