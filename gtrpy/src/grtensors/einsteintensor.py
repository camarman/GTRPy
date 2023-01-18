from itertools import product
from numpy import einsum, zeros
from sympy import Array, MutableDenseNDimArray

from gtrpy.src.grtensors.ricciscalar import RicciScalar
from gtrpy.tools.simplify_objects import Simplify


class EinsteinTensor(RicciScalar):
    def __init__(self, metric_tensor, coord_sys):
        """
        Creating the Einstein tensor object

        Args:
            metric_tensor [list]: The metric tensor, provided by the user
            coord_sys     [list]: The coordinate system given as a list (e.g., [t,x,y,z])

        Returns:
            self.einsteintensor_type [str]         : Type of the Einstein tensor. Default type is 'dd'
            self.einsteintensor_obj  [sympy.tensor]: The Einstein tensor, G_ij
        """
        RicciScalar.__init__(self, metric_tensor, coord_sys)
        self.einsteintensor_type = 'dd'
        einstein_tensor = MutableDenseNDimArray(zeros((self.ndim,)*2))
        for i, j in product(range(self.ndim), repeat=2):
            einstein_tensor[i, j] = self.riccitensor_obj[i, j] - (1/2)*self.ricciscalar_obj*self.metric_obj[i, j]
        self.einsteintensor_obj = einstein_tensor


    def get_einsteintensor(self):
        """
        Returns the Einstein tensor object
        """
        return Simplify(self.einsteintensor_obj)


    def get_einsteintensor_type(self):
        """
        Returns the type of the Einstein tensor
        """
        return self.einsteintensor_type


    def raise_index(self, xeinstein_tensor):
        """
        Raising the index of the Einstein tensor

        Args:
            xeinstein_tensor [sympy.tensor]: Given Einstein tensor
        """
        return Array(einsum('ij,jk->ki', xeinstein_tensor, self.inverse_metric_obj, optimize='optimal'))


    def raise_index1(self, xeinstein_tensor):
        """
        Raising the second index of the Einstein tensor

        Args:
            xeinstein_tensor [sympy.tensor]: Given Einstein tensor
        """
        return Array(einsum('ki,il->kl', xeinstein_tensor, self.inverse_metric_obj, optimize='optimal'))


    def vary_einsteintensor_type(self, new_type):
        """
        Varying the type of the Einstein tensor

        Args:
            new_type [str]: The new type of the Einstein tensor.
                            It should be given in terms of:
                            'u': contravariant (upper-indices)
                            'd': covariant (lower-indices)

        Returns:
            The new Einstein tensor for a given type
        """
        self.einsteintensor_type = new_type
        if new_type == 'dd':
            return Simplify(self.einsteintensor_obj)
        elif new_type == 'ud':
            return Simplify(self.raise_index(self.einsteintensor_obj))
        elif new_type == 'uu':
            return Simplify(self.raise_index1(self.raise_index(self.einsteintensor_obj)))
