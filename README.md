# General-Relativity-Tensor-Calculations (GRTC) by Graphical User Interface (GUI)

#### Calculating the Inverse Metric Tensor, Christoffel Symbol, Riemann Tensor, Ricci Tensor, Ricci Scalar, Weyl Tensor, Traceless Ricci Tensor, Einstein Tensor and, Kretschmann Scalar from the given metric by using GUI.

### Required packages
`IPython.display`, `itertools`, `numpy`, `PIL`, `PySimpleGUI`, `sympy`

## Getting Started

### 0. Download the GRTC Main Folder
### 1. Run the `GRTC_GUI.py` file
### 2. Chose a suitable dimension from the given page. You'll have two options.

![main_page](https://user-images.githubusercontent.com/45866787/122600966-3e504400-d079-11eb-82f0-102a3743db5b.png)

#### If you chose four dimensions, you'll see a page in this form.

![welcoming page](https://user-images.githubusercontent.com/45866787/122601117-7e172b80-d079-11eb-876e-276e483f7884.png)

### 3. Define the coordinate system (cartesian, spherical, etc.)

![choosing_coordinate](https://user-images.githubusercontent.com/45866787/122601160-8ff8ce80-d079-11eb-92cb-b4634f1feb14.png)

#### These are the available/most commonly used coordinate system components. If you want to add another element, go to line `39-40` located in the `GRTC_GUI.py` file.

![coord_names](https://user-images.githubusercontent.com/45866787/122601717-642a1880-d07a-11eb-8c44-0808c6984b62.png)

### 4. Define the diagonal components of the metric tensor

#### While defining the components of the tensor, write the expressions as you are writing them in python (i.e., use `**`, not `^`). I have also defined most of the most common physics symbols, but if you think I am missing something, you can add it through `12-15` from the `GRTC_GUI.py`.

![variable_names](https://user-images.githubusercontent.com/45866787/122601959-bc611a80-d07a-11eb-898f-1809cdf101eb.png)

#### Here is an example 

![choosing_components](https://user-images.githubusercontent.com/45866787/122602136-fb8f6b80-d07a-11eb-9b7c-ac7a7ebd9336.png)

### 5. Chose a tensor that you want to calculate.

#### Chose a tensor from the `Available Tensors` segment and click `Submit.`

## Getting Tensors / Tensor Types and Index Lowering/Raising

#### For instance, when you chose the `Metric Tensor`, you'll see a page like this.

![metric_tensor](https://user-images.githubusercontent.com/45866787/122602173-0d710e80-d07b-11eb-9839-cf0ef32932a6.png)

#### And later on you can choose the `Christoffel Symbol` option to see

![chris_symbol](https://user-images.githubusercontent.com/45866787/122602231-2679bf80-d07b-11eb-9c4e-8a0f859661cb.png)

#### You can change the type of the tensor and get any component from the given page.

![chris_symbol_upper](https://user-images.githubusercontent.com/45866787/122602251-2ed1fa80-d07b-11eb-89e7-c1582633524c.png)


# Non - GUI Version

### *Those who want to run the code from the `.ipynb` file, and don't want to use GUI, can follow the steps given below.*

### Required packages
`itertools`, `numpy`, `sympy`

## Getting Started

#### 0. Download the GRTC Main Folder (`.ipynb` files should run from that directory)
#### 1. Define the coordinate system (cartesian, spherical, etc.) 
#### 2. Define the diagonal components of the metric tensor

##### The first few lines of the code should look like this.

```
from GRTC import *
from sympy import symbols, sin, init_printing

init_printing()

# Defining the symbols in the coordinate system
t, r, theta, phi = symbols('t, r, theta, phi')  

# Defining some extra symbols
M, alpha = symbols('M, alpha')

# Defining the coordinate system
coord_sys = [t, r, theta, phi]

# Defining the diagonal components of the metric tensor
diag_comp = [-1, 1/alpha, M*alpha**2, M*sin(theta)**2]
```

#### 3. To add a different symbol, use [symbols](https://docs.sympy.org/latest/tutorial/basic_operations.html)

## Getting Tensors

##### After defining the diagonal components of the metric tensor, we can calculate/obtain the tensors by just assigning them into a variable and using the `get_tensorname()` method.

##### For instance, to obtain the Christoffel Symbol, it is sufficient to write this line of code in Jupyter Notebook.

```
# Obtaining the Christoffel Symbol
cs = ChristoffelSymbol(diag_comp, coord_sys)
chris_symbol = cs.get_christoffelsymbol()
chris_symbol
```

##  Tensor Types and Index Lowering/Raising

#### 1.`(1,0)` (contravariant) type tensor will be denoted by a string `'u'` and `(0,1)` (covariant) type tensor will be denoted by `'d'`. 

#### 2. To access the type of a given tensor one can use the `get_tensorname_type()` method.

##### For the case above it becomes,

`cs.get_christoffelsymbol_type()`

#### 3. In order to change the type of the tensor, one can use the `vary_tensorname_type()` method.

##### In this case, type the desired tensor form in terms of `'u'` and `'d'`.

```
# Varying type 'udd' Christoffel Symbol to 'ddd'
chris_symbol03 = cs.vary_christoffelsymbol_type(chris_symbol, 'ddd') 
chris_symbol03
```

##### For instance, the code above will convert the type `(1,2)` Christoffel Symbol into type `(0,3).` 

## Some Extra Features 

##### To obtain the non-zero components of the Christoffel Symbol, Riemann Tensor or the Weyl Tensor type `nonzero_tensorname(xtensor)`.

##### For instance,

```
# Obtaining the non-zero components of the given Christoffel Symbol for type ddd
cs.nonzero_christoffelsymbol(chris_symbol03)
```

##### or 

```
# Obtaining the non-zero components of the Riemann Tensor for type uddd
rt.nonzero_riemanntensor(riemann_tensor)
```

##### will show the desired output

##### You can further study these examples on `example.ipynb`
