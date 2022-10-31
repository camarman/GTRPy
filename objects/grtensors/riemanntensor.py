from itertools import product

from numpy import einsum, zeros
from objects.grtensors.christoffelsymbol import ChristoffelSymbol
from objects.simplify_objects import Simplify
from sympy import Array, MutableDenseNDimArray, diff


def derivative_of_chris(coord_sys, chris_symb, i, j, k, l):
    """
    Taking the partial derivative of a given christoffel symbol [Gamma^j_kl] with respect to the
    [i]'th component

    Args:
        coord_sys [list]: The coordinate system given as a list (e.g., [t,x,y,z])
        chris_symb [sympy.tensor]: Given christoffel symbol, Gamma^j_kl
        i,j,k,l [int]: Coordinate indices; (0-ndim)
    """
    return Simplify(diff(chris_symb[j, k, l], coord_sys[i]))


class RiemannTensor(ChristoffelSymbol):
    def __init__(self, metric_tensor, coord_sys):
        """
        Creating the riemann tensor object

        Args:
            metric_tensor [list]: The metric tensor, provided by the user
            coord_sys [list]: The coordinate system given as a list (e.g., [t,x,y,z])

        Returns:
            self.riemann_type [str]: Type of the riemann tensor. Default type is 'uddd'
            self.riemann_obj [sympy.tensor]: The riemann tensor, R^l_ijk
        """
        ChristoffelSymbol.__init__(self, metric_tensor, coord_sys)
        self.riemann_type = 'uddd'
        riemann_tensor = MutableDenseNDimArray(zeros((self.ndim,)*4))
        for l, i, j, k in product(range(self.ndim), repeat=4):
            Q1 = derivative_of_chris(
                self.coord_sys, self.chris_obj, j, l, i, k)
            Q2 = derivative_of_chris(
                self.coord_sys, self.chris_obj, i, l, j, k)
            einstein_sum = 0
            for p in range(self.ndim):
                I1 = self.chris_obj[p, i, k] * self.chris_obj[l, j, p]
                I2 = self.chris_obj[p, j, k] * self.chris_obj[l, i, p]
                einstein_sum += (I1 - I2)
            riemann_tensor[l, i, j, k] = Q1 - Q2 + einstein_sum
        self.riemann_obj = riemann_tensor


    def get_riemanntensor(self):
        """
        Returns the riemann tensor object
        """
        return Simplify(self.riemann_obj)


    def get_riemanntensor_type(self):
        """
        Returns the type of the riemann tensor
        """
        return self.riemann_type


    def lower_index(self, xriemann_tensor):
        """
        Lowering the index of the riemann tensor

        Args:
            xriemann_tensor [sympy.tensor]: Given riemann tensor
        """
        return Array(einsum('abcd,ak->kbcd', xriemann_tensor, self.metric_obj, optimize='optimal'))


    def raise_index(self, xriemann_tensor):
        """
        Raising the first index of the riemann tensor

        Args:
            xriemann_tensor [sympy.tensor]: Given riemann tensor
        """
        return Array(einsum('abcd,bk->akcd', xriemann_tensor, self.inverse_metric_obj, optimize='optimal'))


    def raise_index1(self, xriemann_tensor):
        """
        Raising the second index of the riemann tensor

        Args:
            xriemann_tensor [sympy.tensor]: Given riemann tensor
        """
        return Array(einsum('akcd,cl->akld', xriemann_tensor, self.inverse_metric_obj, optimize='optimal'))


    def raise_index2(self, xriemann_tensor):
        """
        Raising the third index of the riemann tensor

        Args:
            xriemann_tensor [sympy.tensor]: Given riemann tensor
        """
        return Array(einsum('akld,df->aklf', xriemann_tensor, self.inverse_metric_obj, optimize='optimal'))


    def vary_riemanntensor_type(self, xriemann_tensor, new_type):
        """
        Varying the type of the riemann tensor

        Args:
            xriemann_tensor [sympy.tensor]: Given riemann tensor
            new_type [str]: The new type of the riemann tensor. It should be given
            in terms of 'u': contravariant (upper-indices) and 'd': covariant (lower-indices)

        Returns:
            The new riemann tensor for a given type
        """
        self.riemann_type = new_type
        if new_type == 'dddd':
            return Simplify(self.lower_index(xriemann_tensor))
        elif new_type == 'uddd':
            return Simplify(self.riemann_obj)
        elif new_type == 'uudd':
            return Simplify(self.raise_index(xriemann_tensor))
        elif new_type == 'uuud':
            return Simplify(self.raise_index1(self.raise_index(xriemann_tensor)))
        elif new_type == 'uuuu':
            return Simplify(self.raise_index2(self.raise_index1(self.raise_index(xriemann_tensor))))
