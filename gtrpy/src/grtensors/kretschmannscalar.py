from itertools import product
from sympy import simplify

from gtrpy.src.grtensors.riemanntensor import RiemannTensor


class KretschmannScalar(RiemannTensor):
    def __init__(self, metric_tensor, coord_sys):
        """
        Creating the Kretschmann scalar object

        Args:
            metric_tensor [list]: The metric tensor, provided by the user
            coord_sys     [list]: The coordinate system given as a list (e.g., [t,x,y,z])

        Returns:
            self.kretschmannscalar_obj [int/symbol]: The Kretschmann scalar, K
        """
        RiemannTensor.__init__(self, metric_tensor, coord_sys)
        riemanntensor_13 = self.get_riemanntensor()
        riemanntensor_04 = self.vary_riemanntensor_type('dddd')
        riemanntensor_40 = self.vary_riemanntensor_type('uuuu')
        kretschmann_scalar = 0
        for i, j, k, l in product(range(self.ndim), repeat=4):
            kretschmann_scalar += riemanntensor_04[i, j, k, l] * riemanntensor_40[i, j, k, l]
        self.kretschmannscalar_obj = kretschmann_scalar


    def get_kretschmannscalar(self):
        """
        Returns the Kretschmann scalar object
        """
        return simplify(self.kretschmannscalar_obj)
