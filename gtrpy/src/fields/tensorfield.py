from itertools import product
from numpy import einsum, zeros
from sympy import Array, MutableDenseNDimArray, diff

from gtrpy.src.grtensors.christoffelsymbol import ChristoffelSymbol
from gtrpy.src.grtensors.metrictensor import MetricTensor
from gtrpy.tools.simplify_objects import Simplify


class TensorField():
    def __init__(self, metric_tensor, coord_sys, tensor_field, tensor_field_type):
        """
        Creating the tensor field object

        Args:
            metric_tensor     [list]: The metric tensor, provided by the user
            coord_sys         [list]: The coordinate system given as a list (e.g., [t,x,y,z])
            tensor_field      [list]: The tensor field, provided by the user
            tensor_field_type [str] : Type of the tensor field.
                                      It should be given in terms of:
                                      'u': contravariant (upper-indices)
                                      'd': covariant (lower-indices)
        """
        self.metric_obj = metric_tensor
        self.coord_sys = coord_sys
        self.tensor_field = tensor_field
        self.tensor_field_type = tensor_field_type
        self.ndim = len(coord_sys)


    def get_tensorfield(self):
        """
        Returns the tensor field object
        """
        return Simplify(self.tensor_field)


    def get_tensorfield_type(self):
        """
        Returns the type of the tensor field
        """
        return self.tensor_field_type


    def cal_covariant_derivative(self, index):
        """
        The covariant derivative of a tensor field for a given type and index

        Args:
            index [int]: The index of the coordinate system given as an integer (0-ndim)
        """
        cs = ChristoffelSymbol(self.metric_obj, self.coord_sys)
        chris_symbol = cs.get_christoffelsymbol()
        cd_tensor_field = MutableDenseNDimArray(zeros((self.ndim,)*2))
        if self.tensor_field_type == 'uu':
            for i, j in product(range(self.ndim), repeat=2):
                T_partial = diff(self.tensor_field[i][j], self.coord_sys[index])
                einstein_sum1, einstein_sum2 = 0, 0
                for l in range(self.ndim):
                    einstein_sum1 += self.tensor_field[l][j]*chris_symbol[i, l, index]
                    einstein_sum2 += self.tensor_field[i][l]*chris_symbol[j, l, index]
                cd_tensor_field[i, j] = T_partial + einstein_sum1 + einstein_sum2

        elif self.tensor_field_type == 'ud':
            for i, j in product(range(self.ndim), repeat=2):
                T_partial = diff(self.tensor_field[i][j], self.coord_sys[index])
                einstein_sum1, einstein_sum2 = 0, 0
                for l in range(self.ndim):
                    einstein_sum1 += self.tensor_field[l][j]*chris_symbol[i, l, index]
                    einstein_sum1 += self.tensor_field[i][l]*chris_symbol[l, j, index]
                cd_tensor_field[i, j] = T_partial + einstein_sum1 - einstein_sum2

        elif self.tensor_field_type == 'dd':
            for i, j in product(range(self.ndim), repeat=2):
                T_partial = diff(self.tensor_field[i][j], self.coord_sys[index])
                einstein_sum1, einstein_sum2 = 0, 0
                for l in range(self.ndim):
                    einstein_sum1 += self.tensor_field[l][j]*chris_symbol[l, i, index]
                    einstein_sum2 += self.tensor_field[i][l]*chris_symbol[l, j, index]
                cd_tensor_field[i, j] = T_partial - einstein_sum1 - einstein_sum2
        return Simplify(cd_tensor_field)


    def cal_lie_derivative(self, X):
        """
        The Lie derivative of a tensor field with respect to vector field, X

        Args:
            X [list]: Given vector field that the Lie derivative is taken w.r.t
        """
        ld_tensor_field = MutableDenseNDimArray(zeros((self.ndim,)*2))
        if self.tensor_field_type == 'uu':
            for i, j in product(range(self.ndim), repeat=2):
                einstein_sum = 0
                for k in range(self.ndim):
                    S1 = X[k]*diff(self.tensor_field[i][j], self.coord_sys[k])
                    S2 = self.tensor_field[i][k]*diff(X[j], self.coord_sys[k])
                    S3 = self.tensor_field[k][j]*diff(X[i], self.coord_sys[k])
                    einstein_sum += S1 - S2 - S3
                ld_tensor_field[i, j] = einstein_sum

        elif self.tensor_field_type == 'ud':
            for i, j in product(range(self.ndim), repeat=2):
                einstein_sum = 0
                for k in range(self.ndim):
                    S1 = X[k]*diff(self.tensor_field[i][j], self.coord_sys[k])
                    S2 = self.tensor_field[k][j]*diff(X[i], self.coord_sys[k])
                    S3 = self.tensor_field[i][k]*diff(X[k], self.coord_sys[j])
                    einstein_sum += S1 - S2 + S3
                ld_tensor_field[i, j] = einstein_sum

        elif self.tensor_field_type == 'dd':
            for i, j in product(range(self.ndim), repeat=2):
                einstein_sum = 0
                for k in range(self.ndim):
                    S1 = X[k]*diff(self.tensor_field[i][j], self.coord_sys[k])
                    S2 = self.tensor_field[k][j]*diff(X[k], self.coord_sys[i])
                    S3 = self.tensor_field[i][k]*diff(X[k], self.coord_sys[j])
                    einstein_sum += S1 + S2 + S3
                ld_tensor_field[i, j] = einstein_sum
        return Simplify(ld_tensor_field)


    def vary_tensorfield_type(self, new_type):
        """
        Varying the type of the tensor field

        Args:
            new_type [str]: The new type of the tensor field.
                            It should be given in terms of:
                            'u': contravariant (upper-indices)
                            'd': covariant (lower-indices)

        Returns:
            The new tensor field for a given type
        """
        # Defining the inverse metric for the calculations
        mt = MetricTensor(self.metric_obj, self.coord_sys)
        inverse_metric = mt.get_inverse()

        if self.tensor_field_type == 'uu':
            if new_type == 'ud':
                return Simplify(Array(einsum('ij,jk->ik', self.tensor_field, self.metric_obj, optimize='optimal')))
            if new_type == 'dd':
                return Simplify(Array(einsum('ij,jk,il->kl', self.tensor_field, self.metric_obj, self.metric_obj, optimize='optimal')))

        elif self.tensor_field_type == 'ud':
            if new_type == 'uu':
                return Simplify(Array(einsum('ij,jk->ik', self.tensor_field, inverse_metric, optimize='optimal')))
            if new_type == 'dd':
                return Simplify(Array(einsum('ij,ik->jk', self.tensor_field, self.metric_obj, optimize='optimal')))

        elif self.tensor_field_type == 'dd':
            if new_type == 'ud':
                return Simplify(Array(einsum('ij,jk->ki', self.tensor_field, inverse_metric, optimize='optimal')))
            if new_type == 'uu':
                return Simplify(Array(einsum('ij,jk,il->kl', self.tensor_field, inverse_metric, inverse_metric, optimize='optimal')))