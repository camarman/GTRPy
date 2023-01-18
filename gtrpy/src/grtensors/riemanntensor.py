from itertools import product
from numpy import einsum, zeros
from sympy import Array, MutableDenseNDimArray, diff

from gtrpy.src.grtensors.christoffelsymbol import ChristoffelSymbol
from gtrpy.tools.simplify_objects import Simplify


def derivative_of_chris(coord_sys, chris_symb, l, k, i, j):
    """
    Taking the partial derivative of a given Christoffel symbol [Gamma^k_ij] with respect to the
    [l]'th component

    Args:
        coord_sys  [list]        : The coordinate system given as a list (e.g., [t,x,y,z])
        chris_symb [sympy.tensor]: Given Christoffel symbol, Gamma^k_ij
        l,k,i,j    [int]         : Coordinate indices (0-ndim)
    """
    return Simplify(diff(chris_symb[k, i, j], coord_sys[l]))


class RiemannTensor(ChristoffelSymbol):
    def __init__(self, metric_tensor, coord_sys):
        """
        Creating the Riemann tensor object

        Args:
            metric_tensor [list]: The metric tensor, provided by the user
            coord_sys     [list]: The coordinate system given as a list (e.g., [t,x,y,z])

        Returns:
            self.riemann_type [str]         : Type of the Riemann tensor. Default type is 'uddd'
            self.riemann_obj  [sympy.tensor]: The Riemann tensor, R^l_ijk
        """
        ChristoffelSymbol.__init__(self, metric_tensor, coord_sys)
        self.riemann_type = 'uddd'
        riemann_tensor = MutableDenseNDimArray(zeros((self.ndim,)*4))
        for l, i, j, k in product(range(self.ndim), repeat=4):
            Q1 = derivative_of_chris(self.coord_sys, self.chris_obj, j, l, i, k)
            Q2 = derivative_of_chris(self.coord_sys, self.chris_obj, k, l, i, j)
            einstein_sum = 0
            for m in range(self.ndim):
                I1 = self.chris_obj[l, m, j] * self.chris_obj[m, i, k]
                I2 = self.chris_obj[l, m, k] * self.chris_obj[m, i, j]
                einstein_sum += (I1 - I2)
            riemann_tensor[l, i, j, k] = Q1 - Q2 + einstein_sum
        self.riemann_obj = riemann_tensor


    def get_riemanntensor(self):
        """
        Returns the Riemann tensor object
        """
        return Simplify(self.riemann_obj)


    def get_riemanntensor_type(self):
        """
        Returns the type of the Riemann tensor
        """
        return self.riemann_type


    def lower_index(self, xriemann_tensor):
        """
        Lowering the index of the Riemann tensor

        Args:
            xriemann_tensor [sympy.tensor]: Given Riemann tensor
        """
        return Array(einsum('lijk,lm->ijkm', xriemann_tensor, self.metric_obj, optimize='optimal'))


    def raise_index(self, xriemann_tensor):
        """
        Raising the first index of the Riemann tensor

        Args:
            xriemann_tensor [sympy.tensor]: Given Riemann tensor
        """
        return Array(einsum('lijk,im->lmjk', xriemann_tensor, self.inverse_metric_obj, optimize='optimal'))


    def raise_index1(self, xriemann_tensor):
        """
        Raising the second index of the Riemann tensor

        Args:
            xriemann_tensor [sympy.tensor]: Given Riemann tensor
        """
        return Array(einsum('lmjk,jn->lmnk', xriemann_tensor, self.inverse_metric_obj, optimize='optimal'))


    def raise_index2(self, xriemann_tensor):
        """
        Raising the third index of the Riemann tensor

        Args:
            xriemann_tensor [sympy.tensor]: Given Riemann tensor
        """
        return Array(einsum('lmnk,kp->lmnp', xriemann_tensor, self.inverse_metric_obj, optimize='optimal'))


    def vary_riemanntensor_type(self, new_type):
        """
        Varying the type of the Riemann tensor

        Args:
            new_type [str]: The new type of the Riemann tensor.
                            It should be given in terms of:
                            'u': contravariant (upper-indices)
                            'd': covariant (lower-indices)

        Returns:
            The new Riemann tensor for a given type
        """
        self.riemann_type = new_type
        if new_type == 'dddd':
            return Simplify(self.lower_index(self.riemann_obj))
        elif new_type == 'uddd':
            return Simplify(self.riemann_obj)
        elif new_type == 'uudd':
            return Simplify(self.raise_index(self.riemann_obj))
        elif new_type == 'uuud':
            return Simplify(self.raise_index1(self.raise_index(self.riemann_obj)))
        elif new_type == 'uuuu':
            return Simplify(self.raise_index2(self.raise_index1(self.raise_index(self.riemann_obj))))
