from itertools import product
from numpy import einsum, zeros
from sympy import Array, MutableDenseNDimArray

from gtrpy.src.grtensors.riemanntensor import RiemannTensor
from gtrpy.tools.simplify_objects import Simplify


class RicciTensor(RiemannTensor):
    def __init__(self, metric_tensor, coord_sys):
        """
        Creating the Ricci tensor object

        Args:
            metric_tensor [list]: The metric tensor, provided by the user
            coord_sys     [list]: The coordinate system given as a list (e.g., [t,x,y,z])

        Returns:
            self.riccitensor_type [str]         : Type of the Ricci tensor. Default type is 'dd'
            self.riccitensor_obj  [sympy.tensor]: The Ricci tensor, R_ij
        """
        RiemannTensor.__init__(self, metric_tensor, coord_sys)
        self.riccitensor_type = 'dd'
        ricci_tensor = MutableDenseNDimArray(zeros((self.ndim,)*2))
        for i, j in product(range(self.ndim), repeat=2):
            einstein_sum = 0
            for k in range(self.ndim):
                einstein_sum += self.riemann_obj[k, i, k, j]
            ricci_tensor[i, j] = einstein_sum
        self.riccitensor_obj = ricci_tensor


    def get_riccitensor(self):
        """
        Returns the Ricci tensor object
        """
        return Simplify(self.riccitensor_obj)


    def get_riccitensor_type(self):
        """
        Returns the type of the Ricci tensor
        """
        return self.riccitensor_type


    def raise_index(self, xricci_tensor):
        """
        Raising the index of the Ricci tensor

        Args:
            xricci_tensor [sympy.tensor]: Given Ricci tensor
        """
        return Array(einsum('ij,jk->ki', xricci_tensor, self.inverse_metric_obj, optimize='optimal'))


    def raise_index1(self, xricci_tensor):
        """
        Raising the second index of the Ricci tensor

        Args:
            xricci_tensor [sympy.tensor]: Given Ricci tensor
        """
        return Array(einsum('ki,il->kl', xricci_tensor, self.inverse_metric_obj, optimize='optimal'))


    def vary_riccitensor_type(self, new_type):
        """
        Varying the type of the Ricci tensor

        Args:
            new_type [str]: The new type of the Ricci tensor.
                            It should be given in terms of:
                            'u': contravariant (upper-indices)
                            'd': covariant (lower-indices)

        Returns:
            The new Ricci tensor for a given type
        """
        self.riccitensor_type = new_type
        if new_type == 'dd':
            return Simplify(self.riccitensor_obj)
        elif new_type == 'ud':
            return Simplify(self.raise_index(self.riccitensor_obj))
        elif new_type == 'uu':
            return Simplify(self.raise_index1(self.raise_index(self.riccitensor_obj)))
