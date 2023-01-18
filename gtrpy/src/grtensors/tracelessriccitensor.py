from itertools import product
from numpy import einsum, zeros
from sympy import Array, MutableDenseNDimArray

from gtrpy.src.grtensors.ricciscalar import RicciScalar
from gtrpy.tools.simplify_objects import Simplify


class TracelessRicciTensor(RicciScalar):
    def __init__(self, metric_tensor, coord_sys):
        """
        Creating the Traceless Ricci tensor object

        Args:
            metric_tensor [list]: The metric tensor, provided by the user
            coord_sys     [list]: The coordinate system given as a list (e.g., [t,x,y,z])

        Returns:
            self.trclss_riccitensor_type [str]         : Type of the Traceless Ricci tensor. Default type is 'dd'
            self.trclss_riccitensor_obj  [sympy.tensor]: Traceless Ricci tensor, Z_ij

        """
        RicciScalar.__init__(self, metric_tensor, coord_sys)
        self.trclss_riccitensor_type = 'dd'
        trclss_ricci_tensor = MutableDenseNDimArray(zeros((self.ndim,)*2))
        for i, j in product(range(self.ndim), repeat=2):
            trclss_ricci_tensor[i, j] = self.riccitensor_obj[i, j] - (1/self.ndim)*self.ricciscalar_obj*self.metric_obj[i, j]
        self.trclss_riccitensor_obj = trclss_ricci_tensor


    def get_trclss_riccitensor(self):
        """
        Returns the Traceless Ricci tensor object
        """
        return Simplify(self.trclss_riccitensor_obj)


    def get_trclss_riccitensor_type(self):
        """
        Returns the type of the Traceless Ricci tensor
        """
        return self.trclss_riccitensor_type


    def raise_index(self, xtrclss_riccitensor):
        """
        Raising the index of the Traceless Ricci tensor

        Args:
            xtrclss_ricci_tensor [sympy.tensor]: Given Traceless Ricci tensor
        """
        return Array(einsum('ij,jk->ki', xtrclss_riccitensor, self.inverse_metric_obj, optimize='optimal'))


    def raise_index1(self, xtrclss_riccitensor):
        """
        Raising the second index of the Traceless Ricci tensor

        Args:
            xtrclss_ricci_tensor [sympy.tensor]: Given Traceless Ricci tensor
        """
        return Array(einsum('ki,il->kl', xtrclss_riccitensor, self.inverse_metric_obj, optimize='optimal'))


    def vary_trclss_riccitensor_type(self, new_type):
        """
        Varying the type of the Traceless Ricci tensor

        Args:
            new_type [str]: The new type of the Traceless Ricci tensor.
                            It should be given in terms of:
                            'u': contravariant (upper-indices)
                            'd': covariant (lower-indices)

        Returns:
            The new Traceless Ricci tensor for a given type
        """
        self.trclss_riccitensor_type = new_type
        if new_type == 'dd':
            return Simplify(self.trclss_riccitensor_obj)
        elif new_type == 'ud':
            return Simplify(self.raise_index(self.trclss_riccitensor_obj))
        elif new_type == 'uu':
            return Simplify(self.raise_index1(self.raise_index(self.trclss_riccitensor_obj)))
