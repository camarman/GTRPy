from itertools import product

from numpy import einsum, zeros
from objects.grtensors.riemanntensor import RiemannTensor
from objects.simplify_objects import Simplify
from sympy import Array, MutableDenseNDimArray


class RicciTensor(RiemannTensor):
    def __init__(self, metric_tensor, coord_sys):
        """
        Creating the ricci tensor object

        Args:
            metric_tensor [list]: The metric tensor, provided by the user
            coord_sys [list]: The coordinate system given as a list (e.g., [t,x,y,z])

        Returns:
            self.riccitensor_type [str]: Type of the ricci tensor. Default type is 'dd'
            self.riccitensor_obj [sympy.tensor]: The ricci tensor, R_ik
        """
        RiemannTensor.__init__(self, metric_tensor, coord_sys)
        self.riccitensor_type = 'dd'
        ricci_tensor = MutableDenseNDimArray(zeros((self.ndim,)*2))
        for i, k in product(range(self.ndim), repeat=2):
            einstein_sum = 0
            for j in range(self.ndim):
                einstein_sum += self.riemann_obj[j, i, j, k]
            ricci_tensor[i, k] = einstein_sum
        self.riccitensor_obj = ricci_tensor


    def get_riccitensor(self):
        """
        Returns the ricci tensor object
        """
        return Simplify(self.riccitensor_obj)


    def get_riccitensor_type(self):
        """
        Returns the type of the ricci tensor
        """
        return self.riccitensor_type


    def raise_index(self, xricci_tensor):
        """
        Raising the index of the ricci tensor

        Args:
            xricci_tensor [sympy.tensor]: Given ricci tensor
        """
        return Array(einsum('ij,jk->ik', xricci_tensor, self.inverse_metric_obj, optimize='optimal'))


    def vary_riccitensor_type(self, xricci_tensor, new_type):
        """
        Varying the type of the ricci tensor

        Args:
            xricci_tensor [sympy.tensor]: Given ricci tensor
            new_type [str]: The new type of the ricci tensor. It should be given
            in terms of 'u': contravariant (upper-indices) and 'd': covariant (lower-indices)

        Returns:
            The new ricci tensor for a given type
        """
        self.riccitensor_type = new_type
        if new_type == 'dd':
            return Simplify(self.riccitensor_obj)
        elif new_type == 'ud':
            return Simplify(self.raise_index(xricci_tensor))
        elif new_type == 'uu':
            return Simplify(self.raise_index(self.raise_index(xricci_tensor)))
