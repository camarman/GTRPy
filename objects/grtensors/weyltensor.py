from itertools import product

from numpy import einsum, zeros
from objects.grtensors.ricciscalar import RicciScalar
from objects.simplify_objects import Simplify
from sympy import Array, MutableDenseNDimArray


class WeylTensor(RicciScalar):
    def __init__(self, metric_tensor, coord_sys):
        """
        Creating the weyl tensor object

        Args:
            metric_tensor [list]: The metric tensor, provided by the user
            coord_sys [list]: The coordinate system given as a list (e.g., [t,x,y,z])

        Returns:
            self.weyltensor_type [str]: Type of the weyl tensor. Default type is 'dddd'
            self.weyltensor_obj [sympy.tensor]: The weyl tensor, C_iklm
        """
        RicciScalar.__init__(self, metric_tensor, coord_sys)
        self.weyltensor_type = 'dddd'
        weyl_tensor = MutableDenseNDimArray(zeros((self.ndim,)*4))
        riemanntensor_13 = self.get_riemanntensor()
        riemanntensor_04 = self.vary_riemanntensor_type(
            riemanntensor_13, 'dddd')
        for i, k, l, m in product(range(self.ndim), repeat=4):
            I_1 = (self.ndim-2)**(-1) * (self.riccitensor_obj[i, m]*self.metric_obj[k, l] - self.riccitensor_obj[i, l] *
                                         self.metric_obj[k, m] + self.riccitensor_obj[k, l]*self.metric_obj[i, m] - self.riccitensor_obj[k, m]*self.metric_obj[i, l])
            I_2 = ((self.ndim-1)*(self.ndim-2))**(-1) * self.ricciscalar_obj * \
                (self.metric_obj[i, l]*self.metric_obj[k, m] -
                 self.metric_obj[i, m]*self.metric_obj[k, l])
            weyl_tensor[i, k, l, m] = riemanntensor_04[i, k, l, m] + I_1 + I_2
        self.weyltensor_obj = weyl_tensor


    def get_weyltensor(self):
        """
        Returns the weyl tensor object
        """
        return Simplify(self.weyltensor_obj)


    def get_weyltensor_type(self):
        """
        Returns the type of the weyl tensor
        """
        return self.weyltensor_type


    def raise_index(self, xweyl_tensor):
        """
        Raising the first index of the weyl tensor

        Args:
            xweyl_tensor [sympy.tensor]: Given weyl tensor
        """
        return Array(einsum('iklm,ai->aklm', xweyl_tensor, self.inverse_metric_obj, optimize='optimal'))


    def raise_index1(self, xweyl_tensor):
        """
        Raising the second index of the weyl tensor

        Args:
            xweyl_tensor [sympy.tensor]: Given weyl tensor
        """
        return Array(einsum('aklm,bk->ablm', xweyl_tensor, self.inverse_metric_obj, optimize='optimal'))


    def raise_index2(self, xweyl_tensor):
        """
        Raising the third index of the weyl tensor

        Args:
            xweyl_tensor [sympy.tensor]: Given weyl tensor
        """
        return Array(einsum('ablm,cl->abcm', xweyl_tensor, self.inverse_metric_obj, optimize='optimal'))


    def raise_index3(self, xweyl_tensor):
        """
        Raising the fourth index of the weyl tensor

        Args:
            xweyl_tensor [sympy.tensor]: Given weyl tensor
        """
        return Array(einsum('abcm,md->abcd', xweyl_tensor, self.inverse_metric_obj, optimize='optimal'))


    def vary_weyltensor_type(self, xweyl_tensor, new_type):
        """
        Varying the type of the weyl tensor

        Args:
            xweyl_tensor [sympy.tensor]: Given weyl tensor
            new_type [str]: The new type of the weyl tensor. It should be given
            in terms of 'u': contravariant (upper-indices) and 'd': covariant (lower-indices)

        Returns:
            The new weyl tensor for a given type
        """
        self.weyltensor_type = new_type
        if new_type == 'dddd':
            return Simplify(self.weyltensor_obj)
        elif new_type == 'uddd':
            return Simplify(self.raise_index(xweyl_tensor))
        elif new_type == 'uudd':
            return Simplify(self.raise_index1(self.raise_index(xweyl_tensor)))
        elif new_type == 'uuud':
            return Simplify(self.raise_index2(self.raise_index1(self.raise_index(xweyl_tensor))))
        elif new_type == 'uuuu':
            return Simplify(self.raise_index3(self.raise_index2(self.raise_index1(self.raise_index(xweyl_tensor)))))
