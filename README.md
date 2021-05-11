# General-Relativity-Tensor-Calculations

Calculating the Christoffel Symbol, Riemann Tensor, Ricci Tensor, Ricci Scalar, Weyl Tensor, Traceless Ricci Tensor, and Einstein Tensor from the given metric

### Required packages
sympy, numpy, itertools

## Getting Started

#### 0. Download the GR Tensor Folder (.ipynb files should run from that directory)
#### 1. Define the coordinate system (cartesian, spherical, etc.) 
#### 2. Define the diagonal components of the metric tensor

The first few lines of the code should look like this.

```
from GR_full_curv import *
from sympy import symbols, sin, init_printing

init_printing()

# Coordinate system that we will work on
coord_sys = symbols('t r theta phi')  

# Defining some extra symbols
G, m, a = symbols('G, m, a') 

# Defining the diagonal components of the metric tensor
diag_comp = [-1, a**(-1), a**2, a * sin(coord_sys[2])**2]
```

#### 3. To add a different symbol, use [symbols](https://docs.sympy.org/latest/tutorial/basic_operations.html)

## Getting Tensors

After defining the diagonal components of the metric tensor, we can calculate/obtain the tensors by just assigning them into a variable and using the `get_tensorname()` method.

For instance, to obtain the Christoffel Symbol, it is sufficient to write this line of code in Jupyter Notebook.

```
cs = ChristoffelSymbol(diag_comp, coord_sys)
chris_symbol = cs.get_christoffelsymbol()
chris_symbol
```

##  Tensor Types and Index Lowering/Raising

#### 1.`(1,0)` (Contravariant) type tensor will be denoted by a string `'u'` and `(0,1)` covariant type tensor will be denoted by `'d'`. 

#### 2. To access the type of a given tensor one can use the `get_tensorname_type()` method.

For the case above it becomes,

`cs.get_christoffelsymbol_type()`

#### 3. In order to change the type of the tensor, one can use the `vary_tensorname_type()` method.

In this case, just type the desired form in terms of `'u'` and `'d'`.

`cs.vary_type(chris_symbol, 'ddd')`

For instance, the code above will convert the type `(1,2)` Christoffel Symbol into type `(0,3)`

## Some Extra Features 

#### 1. In order to obtain the non-zero components of the Christoffel Symbols just type

`cs.nonzero_christoffelsymbol(chris_symbol)`

## Notes 

#### 1. These examples can be further studied on `example.ipynb`
#### 2. It is recommended to use Jupyter Notebook to see a better output.
#### 3. For some metrics the [`nsimplify`](https://docs.sympy.org/latest/modules/simplify/simplify.html#nsimplify) method may not be working properly. In this case remove that function from the the source code.
