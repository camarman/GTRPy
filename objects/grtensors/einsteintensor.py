from itertools import product

from numpy import einsum, zeros
from objects.grtensors.ricciscalar import RicciScalar
from objects.simplifyobjects import Simplify
from sympy import Array, MutableDenseNDimArray


class EinsteinTensor(RicciScalar):
    def __init__(self, metric_tensor, coord_sys):
        """
        Creating the einstein tensor object

        Args:
            metric_tensor [list]: The metric tensor, provided by the user
            coord_sys [list]: The coordinate system given as a list (e.g., [t,x,y,z])

        Returns:
            self.einsteintensor_type [str]: Type of the einstein tensor. Default type is 'dd'
            self.einsteintensor_obj [sympy.tensor]: The einstein tensor, G_ij
        """
        RicciScalar.__init__(self, metric_tensor, coord_sys)
        self.einsteintensor_type = 'dd'
        einstein_tensor = MutableDenseNDimArray(zeros((self.ndim,)*2))
        for i, k in product(range(self.ndim), repeat=2):
            einstein_tensor[i, k] = self.riccitensor_obj[i, k] - \
                (1/2) * self.ricciscalar_obj * self.metric_obj[i, k]
        self.einsteintensor_obj = einstein_tensor

    def get_einsteintensor(self):
        """
        Returns the einstein tensor object
        """
        return Simplify(self.einsteintensor_obj)

    def get_einsteintensor_type(self):
        """
        Returns the type of the einstein tensor
        """
        return self.einsteintensor_type

    def raise_index(self, xeinstein_tensor):
        """
        Raising the index of the einstein tensor

        Args:
            xeinstein_tensor [sympy.tensor]: Given einstein tensor
        """
        return Array(einsum('ij,jk->ki', xeinstein_tensor, self.inverse_metric_obj, optimize='optimal'))

    def vary_einsteintensor_type(self, xeinstein_tensor, new_type):
        """
        Varying the type of the einstein tensor

        Args:
            xeinstein_tensor [sympy.tensor]: Given einstein tensor
            new_type [str]: The new type of the einstein tensor. It should be given
            in terms of 'u': contravariant (upper-indices) and 'd': covariant (lower-indices)

        Returns:
            The new einstein tensor for a given type
        """
        self.einsteintensor_type = new_type
        if new_type == 'dd':
            return Simplify(self.einsteintensor_obj)
        elif new_type == 'ud':
            return Simplify(self.raise_index(xeinstein_tensor))
        elif new_type == 'uu':
            return Simplify(self.raise_index(self.raise_index(xeinstein_tensor)))
