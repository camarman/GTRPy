from itertools import product
from numpy import einsum, zeros
from sympy import Array, MutableDenseNDimArray

from gtrpy.src.grtensors.ricciscalar import RicciScalar
from gtrpy.tools.simplify_objects import Simplify


class WeylTensor(RicciScalar):
    def __init__(self, metric_tensor, coord_sys):
        """
        Creating the Weyl tensor object

        Args:
            metric_tensor [list]: The metric tensor, provided by the user
            coord_sys     [list]: The coordinate system given as a list (e.g., [t,x,y,z])

        Returns:
            self.weyltensor_type [str]         : Type of the Weyl tensor. Default type is 'dddd'
            self.weyltensor_obj  [sympy.tensor]: The Weyl tensor, C_ijkl
        """
        RicciScalar.__init__(self, metric_tensor, coord_sys)
        self.weyltensor_type = 'dddd'
        weyl_tensor = MutableDenseNDimArray(zeros((self.ndim,)*4))
        riemanntensor_13 = self.get_riemanntensor()
        riemanntensor_04 = self.vary_riemanntensor_type('dddd')
        for i, j, k, l in product(range(self.ndim), repeat=4):
            I_11 = self.metric_obj[i, l]*self.riccitensor_obj[k, j]
            I_12 = self.metric_obj[j, k]*self.riccitensor_obj[l, i]
            I_13 = self.metric_obj[i, k]*self.riccitensor_obj[l, j]
            I_14 = self.metric_obj[j, l]*self.riccitensor_obj[k, i]
            I_1 = (self.ndim-2)**(-1)*(I_11 + I_12 - I_13 - I_14)

            I_21 = self.metric_obj[i, k]*self.metric_obj[l, j]
            I_22 = self.metric_obj[i, l]*self.metric_obj[k, j]
            I_2 = ((self.ndim-1)*(self.ndim-2))**(-1)*self.ricciscalar_obj*(I_21 - I_22)

            weyl_tensor[i, j, k, l] = riemanntensor_04[i, j, k, l] + I_1 + I_2
        self.weyltensor_obj = weyl_tensor


    def get_weyltensor(self):
        """
        Returns the Weyl tensor object
        """
        return Simplify(self.weyltensor_obj)


    def get_weyltensor_type(self):
        """
        Returns the type of the Weyl tensor
        """
        return self.weyltensor_type


    def raise_index(self, xweyl_tensor):
        """
        Raising the first index of the Weyl tensor

        Args:
            xweyl_tensor [sympy.tensor]: Given Weyl tensor
        """
        return Array(einsum('ijkl,im->mjkl', xweyl_tensor, self.inverse_metric_obj, optimize='optimal'))


    def raise_index1(self, xweyl_tensor):
        """
        Raising the second index of the Weyl tensor

        Args:
            xweyl_tensor [sympy.tensor]: Given Weyl tensor
        """
        return Array(einsum('mjkl,jn->mnkl', xweyl_tensor, self.inverse_metric_obj, optimize='optimal'))


    def raise_index2(self, xweyl_tensor):
        """
        Raising the third index of the Weyl tensor

        Args:
            xweyl_tensor [sympy.tensor]: Given Weyl tensor
        """
        return Array(einsum('mnkl,kp->mnpl', xweyl_tensor, self.inverse_metric_obj, optimize='optimal'))


    def raise_index3(self, xweyl_tensor):
        """
        Raising the fourth index of the Weyl tensor

        Args:
            xweyl_tensor [sympy.tensor]: Given Weyl tensor
        """
        return Array(einsum('mnpl,lr->mnpr', xweyl_tensor, self.inverse_metric_obj, optimize='optimal'))


    def vary_weyltensor_type(self, new_type):
        """
        Varying the type of the Weyl tensor

        Args:
            new_type [str]: The new type of the Weyl tensor.
                            It should be given in terms of:
                            'u': contravariant (upper-indices)
                            'd': covariant (lower-indices)

        Returns:
            The new Weyl tensor for a given type
        """
        self.weyltensor_type = new_type
        if new_type == 'dddd':
            return Simplify(self.weyltensor_obj)
        elif new_type == 'uddd':
            return Simplify(self.raise_index(self.weyltensor_obj))
        elif new_type == 'uudd':
            return Simplify(self.raise_index1(self.raise_index(self.weyltensor_obj)))
        elif new_type == 'uuud':
            return Simplify(self.raise_index2(self.raise_index1(self.raise_index(self.weyltensor_obj))))
        elif new_type == 'uuuu':
            return Simplify(self.raise_index3(self.raise_index2(self.raise_index1(self.raise_index(self.weyltensor_obj)))))
