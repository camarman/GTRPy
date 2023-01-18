from itertools import product
from sympy import simplify

from gtrpy.src.grtensors.riccitensor import RicciTensor


class RicciScalar(RicciTensor):
    def __init__(self, metric_tensor, coord_sys):
        """
        Creating the Ricci scalar object

        Args:
            metric_tensor [list]: The metric tensor, provided by the user
            coord_sys     [list]: The coordinate system given as a list (e.g., [t,x,y,z])

        Returns:
            self.ricciscalar_obj [int/symbol]: The Ricci scalar, R
        """
        RicciTensor.__init__(self, metric_tensor, coord_sys)
        ricci_scalar = 0
        for i, j in product(range(self.ndim), repeat=2):
            ricci_scalar += self.inverse_metric_obj[i, j]*self.riccitensor_obj[i, j]
        self.ricciscalar_obj = ricci_scalar


    def get_ricciscalar(self):
        """
        Returns the Ricci scalar object
        """
        return simplify(self.ricciscalar_obj)
