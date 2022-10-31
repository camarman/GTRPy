from itertools import product

from numpy import einsum, zeros
from objects.grtensors.ricciscalar import RicciScalar
from objects.simplify_objects import Simplify
from sympy import Array, MutableDenseNDimArray


class TracelessRicciTensor(RicciScalar):
    def __init__(self, metric_tensor, coord_sys):
        """
        Creating the traceless ricci tensor object

        Args:
            metric_tensor [list]: The metric tensor, provided by the user
            coord_sys [list]: The coordinate system given as a list (e.g., [t,x,y,z])

        Returns:
            self.trclss_riccitensor_type [str]: Type of the traceless ricci tensor. Default type is 'dd'
            self.trclss_riccitensor_obj [sympy.tensor]: The traceless ricci tensor, Z_ij

        """
        RicciScalar.__init__(self, metric_tensor, coord_sys)
        self.trclss_riccitensor_type = 'dd'
        trclss_ricci_tensor = MutableDenseNDimArray(zeros((self.ndim,)*2))
        for i, k in product(range(self.ndim), repeat=2):
            trclss_ricci_tensor[i, k] = self.riccitensor_obj[i, k] - \
                (1/self.ndim) * self.ricciscalar_obj * self.metric_obj[i, k]
        self.trclss_riccitensor_obj = trclss_ricci_tensor


    def get_trclss_riccitensor(self):
        """
        Returns the traceless ricci tensor object
        """
        return Simplify(self.trclss_riccitensor_obj)


    def get_trclss_riccitensor_type(self):
        """
        Returns the type of the traceless ricci tensor
        """
        return self.trclss_riccitensor_type


    def raise_index(self, xtrclss_riccitensor):
        """
        Raising the index of the traceless ricci tensor

        Args:
            xtrclss_ricci_tensor [sympy.tensor]: Given traceless ricci tensor
        """
        return Array(einsum('ij,jk->ki', xtrclss_riccitensor, self.inverse_metric_obj, optimize='optimal'))


    def vary_trclss_riccitensor_type(self, xtrclss_riccitensor, new_type):
        """
        Varying the type of the traceless ricci tensor

        Args:
            xtrclss_ricci_tensor [sympy.tensor]: Given traceless ricci tensor
            new_type [str]: The new type of the traceless ricci tensor. It should be given
            in terms of 'u': contravariant (upper-indices) and 'd': covariant (lower-indices)

        Returns:
            The new traceless ricci tensor for a given type
        """
        self.trclss_riccitensor_type = new_type
        if new_type == 'dd':
            return Simplify(self.trclss_riccitensor_obj)
        elif new_type == 'ud':
            return Simplify(self.raise_index(xtrclss_riccitensor))
        elif new_type == 'uu':
            return Simplify(self.raise_index(self.raise_index(xtrclss_riccitensor)))
