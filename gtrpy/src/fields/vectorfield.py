from numpy import einsum, zeros
from sympy import Array, MutableDenseNDimArray, diff

from gtrpy.src.fields.tensorfield import TensorField
from gtrpy.src.grtensors.christoffelsymbol import ChristoffelSymbol
from gtrpy.src.grtensors.metrictensor import MetricTensor
from gtrpy.tools.simplify_objects import Simplify


class VectorField():
    def __init__(self, metric_tensor, coord_sys, vector_field, vector_field_type):
        """
        Creating the vector field object

        Args:
            metric_tensor     [list]: The metric tensor, provided by the user
            coord_sys         [list]: The coordinate system given as a list (e.g., [t,x,y,z])
            vector_field      [list]: The vector field, provided by the user
            vector_field_type [str] : Type of the vector field.
                                      It should be given in terms of:
                                      'u': contravariant (upper-indices)
                                      'd': covariant (lower-indices)
        """
        self.metric_obj = metric_tensor
        self.coord_sys = coord_sys
        self.vector_field = vector_field
        self.vector_field_type = vector_field_type
        self.ndim = len(coord_sys)


    def get_vectorfield(self):
        """
        Returns the vector field object
        """
        return Simplify(self.vector_field)


    def get_vectorfield_type(self):
        """
        Returns the type of the vector field
        """
        return self.vector_field_type


    def cal_covariant_derivative(self, index):
        """
        The covariant derivative of a vector field for a given type and index

        Args:
            index [int]: The index of the coordinate system given as an integer (0-ndim)
        """
        cs = ChristoffelSymbol(self.metric_obj, self.coord_sys)
        chris_symbol = cs.get_christoffelsymbol()
        cd_vector_field = []
        if self.vector_field_type == 'u':
            for i in range(self.ndim):
                V_partial = diff(self.vector_field[i], self.coord_sys[index])
                einstein_sum = 0
                for j in range(self.ndim):
                    einstein_sum += chris_symbol[i, j, index]*self.vector_field[j]
                cov_V = V_partial + einstein_sum
                cd_vector_field.append(cov_V)

        elif self.vector_field_type == 'd':
            for i in range(self.ndim):
                V_partial = diff(self.vector_field[i], self.coord_sys[index])
                einstein_sum = 0
                for j in range(self.ndim):
                    einstein_sum += chris_symbol[j, i, index]*self.vector_field[j]
                cov_V = V_partial - einstein_sum
                cd_vector_field.append(cov_V)
        return Simplify(Array(cd_vector_field))


    def cal_lie_derivative(self, X):
        """
        The Lie derivative of a vector field with respect to another vector field, X

        Args:
            X [list]: Given vector field that the Lie derivative is taken w.r.t
        """
        ld_vector_field = []
        if self.vector_field_type == 'u':
            for i in range(self.ndim):
                einstein_sum = 0
                for j in range(self.ndim):
                    einstein_sum += X[j]*diff(self.vector_field[i], self.coord_sys[j]) - self.vector_field[j]*diff(X[i], self.coord_sys[j])
                ld_vector_field.append(einstein_sum)

        elif self.vector_field_type == 'd':
            for i in range(self.ndim):
                einstein_sum = 0
                for j in range(self.ndim):
                    einstein_sum += X[j]*diff(self.vector_field[i], self.coord_sys[j]) + self.vector_field[j]*diff(X[j], self.coord_sys[i])
                ld_vector_field.append(einstein_sum)
        return Simplify(Array(ld_vector_field))


    def isKillingField(self, xvector_field):
        """
        Checking if a giving vector field with type (1,0) is a Killing field or not
        """
        g = TensorField(self.metric_obj, self.coord_sys, self.metric_obj, 'dd')
        if g.cal_lie_derivative(xvector_field) == MutableDenseNDimArray(zeros((4,)*2)):
            return True
        return False


    def vary_vectorfield_type(self):
        """
        Varying the type of the vector field
        """
        if self.vector_field_type == 'u':
            return Simplify(Array(einsum('i,ij->j', self.vector_field, self.metric_obj, optimize='optimal')))
        elif self.vector_field_type == 'd':
            mt = MetricTensor(self.metric_obj, self.coord_sys)
            inverse_metric = mt.get_inverse()
            return Simplify(Array(einsum('i,ij->j', self.vector_field, inverse_metric, optimize='optimal')))
