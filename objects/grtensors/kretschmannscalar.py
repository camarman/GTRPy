from itertools import product

from objects.grtensors.riemanntensor import RiemannTensor
from sympy import simplify


class KretschmannScalar(RiemannTensor):
    def __init__(self, metric_tensor, coord_sys):
        """
        Creating the kretschmann scalar object

        Args:
            metric_tensor [list]: The metric tensor, provided by the user
            coord_sys [list]: The coordinate system given as a list (e.g., [t,x,y,z])

        Returns:
            self.kretschmannscalar_obj [int/symbol]: The kretschmann scalar, K
        """
        RiemannTensor.__init__(self, metric_tensor, coord_sys)
        riemanntensor_13 = self.get_riemanntensor()
        riemanntensor_04 = self.vary_riemanntensor_type(
            riemanntensor_13, 'dddd')
        riemanntensor_40 = self.vary_riemanntensor_type(
            riemanntensor_13, 'uuuu')
        kretschmann_scalar = 0
        for a, b, c, d in product(range(self.ndim), repeat=4):
            kretschmann_scalar += riemanntensor_04[a,
                                                   b, c, d] * riemanntensor_40[a, b, c, d]
        self.kretschmannscalar_obj = kretschmann_scalar

    def get_kretschmannscalar(self):
        """
        Returns the kretschmann scalar object
        """
        return simplify(self.kretschmannscalar_obj)
