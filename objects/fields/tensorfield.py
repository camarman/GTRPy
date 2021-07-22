from itertools import product

from numpy import zeros
from objects.grtensors.christoffelsymbol import ChristoffelSymbol
from objects.simplifyobjects import Simplify
from sympy import MutableDenseNDimArray, diff


class TensorField():
    def __init__(self, metric_tensor, coord_sys, tensor_field, tensor_field_type):
        """
        Creating the tensor field object

        Args:
            metric_tensor [list]: The metric tensor, provided by the user
            coord_sys [list]: The coordinate system given as a list (e.g., [t,x,y,z])
            tensor_field [list]: The tensor field, provided by the user
            tensor_field_type [str]: Type of the tensor field. It should be given
            in terms of 'u': contravariant (upper-indices) and 'd': covariant (lower-indices)
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
            index [int]: The index of the coordinate system given as an integer; (0-ndim)
        """
        cs = ChristoffelSymbol(self.metric_obj, self.coord_sys)
        chris_symbol = cs.get_christoffelsymbol()
        cd_tensor_field = MutableDenseNDimArray(zeros((self.ndim,)*2))
        if self.tensor_field_type == 'uu':
            for a, b in product(range(self.ndim), repeat=2):
                T_partial = diff(
                    self.tensor_field[a][b], self.coord_sys[index])
                einstein_sum1, einstein_sum2 = 0, 0
                for d in range(self.ndim):
                    einstein_sum1 += chris_symbol[a,
                                                  index, d]*self.tensor_field[d][b]
                    einstein_sum2 += chris_symbol[b,
                                                  index, d]*self.tensor_field[a][d]
                cd_tensor_field[a, b] = T_partial + \
                    einstein_sum1 + einstein_sum2

        elif self.tensor_field_type == 'ud':
            for a, b in product(range(self.ndim), repeat=2):
                T_partial = diff(
                    self.tensor_field[a][b], self.coord_sys[index])
                einstein_sum1, einstein_sum2 = 0, 0
                for d in range(self.ndim):
                    einstein_sum1 += chris_symbol[a,
                                                  index, d]*self.tensor_field[d][b]
                    einstein_sum1 += chris_symbol[d,
                                                  index, b]*self.tensor_field[a][d]
                cd_tensor_field[a, b] = T_partial + \
                    einstein_sum1 - einstein_sum2

        elif self.tensor_field_type == 'dd':
            for a, b in product(range(self.ndim), repeat=2):
                T_partial = diff(
                    self.tensor_field[a][b], self.coord_sys[index])
                einstein_sum1, einstein_sum2 = 0, 0
                for d in range(self.ndim):
                    einstein_sum1 += chris_symbol[d,
                                                  index, a]*self.tensor_field[d][b]
                    einstein_sum2 += chris_symbol[d,
                                                  index, b]*self.tensor_field[a][d]
                cd_tensor_field[a, b] = T_partial - \
                    einstein_sum1 - einstein_sum2
        return Simplify(cd_tensor_field)

    def cal_lie_derivative(self, X):
        """
        The lie derivative of a tensor field with respect to vector field, X

        Args:
           X [list]: Given vector field that the lie derivative is taken w.r.t
        """
        ld_tensor_field = MutableDenseNDimArray(zeros((self.ndim,)*2))
        if self.tensor_field_type == 'uu':
            for a, b in product(range(self.ndim), repeat=2):
                einstein_sum = 0
                for c in range(self.ndim):
                    S1 = X[c]*diff(self.tensor_field[a][b], self.coord_sys[c])
                    S2 = self.tensor_field[c][b]*diff(X[a], self.coord_sys[c])
                    S3 = self.tensor_field[a][c]*diff(X[b], self.coord_sys[c])
                    einstein_sum += S1 - S2 - S3
                ld_tensor_field[a, b] = einstein_sum

        elif self.tensor_field_type == 'ud':
            for a, b in product(range(self.ndim), repeat=2):
                einstein_sum = 0
                for c in range(self.ndim):
                    S1 = X[c]*diff(self.tensor_field[a][b], self.coord_sys[c])
                    S2 = self.tensor_field[c][b]*diff(X[a], self.coord_sys[c])
                    S3 = self.tensor_field[a][c]*diff(X[c], self.coord_sys[b])
                    einstein_sum += S1 - S2 + S3
                ld_tensor_field[a, b] = einstein_sum

        elif self.tensor_field_type == 'dd':
            for a, b in product(range(self.ndim), repeat=2):
                einstein_sum = 0
                for c in range(self.ndim):
                    S1 = X[c]*diff(self.tensor_field[a][b], self.coord_sys[c])
                    S2 = self.tensor_field[c][b]*diff(X[c], self.coord_sys[a])
                    S3 = self.tensor_field[a][c]*diff(X[c], self.coord_sys[b])
                    einstein_sum += S1 + S2 + S3
                ld_tensor_field[a, b] = einstein_sum
        return Simplify(ld_tensor_field)
