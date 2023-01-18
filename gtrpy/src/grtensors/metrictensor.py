from numpy import array, einsum
from sympy import Array, Matrix

from gtrpy.tools.simplify_objects import Simplify


class MetricTensor(object):
    def __init__(self, metric_tensor, coord_sys):
        """
        Creating the metric tensor object

        Args:
            metric_tensor [list]: The metric tensor
            coord_sys     [list]: The coordinate system given as a list (e.g., [t,x,y,z])

        Returns:
            self.metric_obj         [sympy.tensor]: The metric tensor, g_ij
            self.coord_sys          [np.ndarray]  : The coordinate system (cartesian, spherical, etc.)
            self.metric_type        [str]         : Type of the metric tensor. Default type is 'dd'
            self.inverse_metric_obj [sympy.tensor]: The inverse of the metric tensor, g^ij
            self.ndim               [int]         : Dimension of the space. It can be 3 or 4
        """
        self.metric_obj = Array(metric_tensor)
        self.coord_sys = array(coord_sys)
        self.metric_type = 'dd'
        self.inverse_metric_obj = Array(Matrix(metric_tensor).inv())
        self.ndim = len(coord_sys)


    def get_metrictensor(self):
        """
        Returns the metric tensor object
        """
        return Simplify(self.metric_obj)


    def get_metrictensor_type(self):
        """
        Returns the type of the metric tensor
        """
        return self.metric_type


    def get_inverse(self):
        """
        Returns the inverse of the metric tensor
        """
        return Simplify(self.inverse_metric_obj)


    def raise_index(self, xmetric_tensor):
        """
        Raising the index of the metric tensor

        Args:
            xmetric_tensor [sympy.tensor]: Given metric tensor
        """
        return Array(einsum('ij,jk->ki', xmetric_tensor, self.inverse_metric_obj, optimize='optimal'))


    def raise_index1(self, xmetric_tensor):
        """
        Raising the second index of the metric tensor

        Args:
            xmetric_tensor [sympy.tensor]: Given metric tensor
        """
        return Array(einsum('ki,il->kl', xmetric_tensor, self.inverse_metric_obj, optimize='optimal'))


    def vary_metrictensor_type(self, new_type):
        """
        Varying the type of the metric tensor

        Args:
            new_type [str]: The new type of the metric tensor.
                            It should be given in terms of:
                            'u': contravariant (upper-indices)
                            'd': covariant (lower-indices)

        Returns:
            The new metric tensor for a given type
        """
        self.metric_type = new_type
        if new_type == 'dd':
            return Simplify(self.metric_obj)
        elif new_type == 'ud':
            return Simplify(self.raise_index(self.metric_obj))
        elif new_type == 'uu':
            return Simplify(self.raise_index1(self.raise_index(self.metric_obj)))
