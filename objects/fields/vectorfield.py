from objects.grtensors.christoffelsymbol import ChristoffelSymbol
from objects.simplifyobjects import Simplify
from sympy import Array, diff


class VectorField():
    def __init__(self, metric_tensor, coord_sys, vector_field, vector_field_type):
        """
        Creating the vector field object

        Args:
            metric_tensor [list]: The metric tensor, provided by the user
            coord_sys [list]: The coordinate system given as a list (e.g., [t,x,y,z])
            vector_field [list]: The vector field, provided by the user
            vector_field_type [str]: Type of the vector field. It should be given
            in terms of 'u': contravariant (upper-indices) and 'd': covariant (lower-indices)
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
            index [int]: The index of the coordinate system given as an integer; (0-ndim)
        """
        cs = ChristoffelSymbol(self.metric_obj, self.coord_sys)
        chris_symbol = cs.get_christoffelsymbol()
        cd_vector_field = []
        if self.vector_field_type == 'u':
            for a in range(self.ndim):
                V_partial = diff(self.vector_field[a], self.coord_sys[index])
                einstein_sum = 0
                for b in range(self.ndim):
                    einstein_sum += chris_symbol[a,
                                                 index, b]*self.vector_field[b]
                cov_V = V_partial + einstein_sum
                cd_vector_field.append(cov_V)

        elif self.vector_field_type == 'd':
            for a in range(self.ndim):
                V_partial = diff(self.vector_field[a], self.coord_sys[index])
                einstein_sum = 0
                for b in range(self.ndim):
                    einstein_sum += chris_symbol[b,
                                                 index, a]*self.vector_field[b]
                cov_V = V_partial - einstein_sum
                cd_vector_field.append(cov_V)
        return Simplify(Array(cd_vector_field))

    def cal_lie_derivative(self, X):
        """
        The lie derivative of a vector field with respect to another vector field, X

        Args:
            X [list]: Given vector field that the lie derivative is taken w.r.t
        """
        ld_vector_field = []
        if self.vector_field_type == 'u':
            for a in range(self.ndim):
                einstein_sum = 0
                for c in range(self.ndim):
                    einstein_sum += X[c]*diff(self.vector_field[a], self.coord_sys[c]) - \
                        self.vector_field[c]*diff(X[a], self.coord_sys[c])
                ld_vector_field.append(einstein_sum)

        elif self.vector_field_type == 'd':
            for a in range(self.ndim):
                einstein_sum = 0
                for c in range(self.ndim):
                    einstein_sum += X[c]*diff(self.vector_field[a], self.coord_sys[c]) + \
                        self.vector_field[c]*diff(X[c], self.coord_sys[a])
                ld_vector_field.append(einstein_sum)
        return Simplify(Array(ld_vector_field))
