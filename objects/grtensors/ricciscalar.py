from itertools import product

from objects.grtensors.riccitensor import RicciTensor
from sympy import simplify


class RicciScalar(RicciTensor):
    def __init__(self, metric_tensor, coord_sys):
        """
        Creating the ricci scalar object

        Args:
            metric_tensor [list]: The metric tensor, provided by the user
            coord_sys [list]: The coordinate system given as a list (e.g., [t,x,y,z])

        Returns:
            self.ricciscalar_obj [int/symbol]: The ricci scalar, R
        """
        RicciTensor.__init__(self, metric_tensor, coord_sys)
        ricci_scalar = 0
        for i, k in product(range(self.ndim), repeat=2):
            ricci_scalar += self.inverse_metric_obj[i,
                                                    k] * self.riccitensor_obj[i, k]
        self.ricciscalar_obj = ricci_scalar


    def get_ricciscalar(self):
        """
        Returns the ricci scalar object
        """
        return simplify(self.ricciscalar_obj)
