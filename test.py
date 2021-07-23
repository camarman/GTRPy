from sympy import sin, symbols
from objects.fields.vectorfield import VectorField

# Defining the symbols in the coordinate system
t, r, theta, phi = symbols('t, r, theta, phi')

# Defining some extra symbols
r_s = symbols('r_s')

# Defining the diagonal components of the metric tensor
metric_tensor = [
                            [-(1-r_s/r), 0, 0, 0],
                            [0, (1-r_s/r)**(-1), 0, 0],
                            [0, 0, r**2, 0],
                            [0, 0, 0, r**2*sin(theta)**2]
                        ]

#Defining the coordinate system
coord_sys = [t, r, theta, phi]

K = [-(1-r_s/r), 0, 0, 0]

vf = VectorField(metric_tensor, coord_sys, K, 'd')
vector_field = vf.get_vectorfield()
vector_field_up = vf.vary_vectorfield_type(vector_field, 'u')
print(vf.isKillingField(vector_field_up))