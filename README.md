# General-Relativity-Tensor-Calculations (GRTC) by Graphical User Interface (GUI)

Calculating the Inverse Metric Tensor, Christoffel Symbol, Riemann Tensor, Ricci Tensor, Ricci Scalar, Weyl Tensor, Traceless Ricci Tensor, Einstein Tensor and, Kretschmann Scalar from the given metric by using GUI.

### Required packages
`IPython.display`, `itertools`, `numpy`, `PIL`, `PySimpleGUI`, `sympy`

## Getting Started

### 0. Download the GRTC Main Folder
### 1. Run the GRTC_GUI.py file
### 2. Chose a suitable dimension from the given page. You'll have two options.

![Intro_dim](https://user-images.githubusercontent.com/45866787/118868040-66b71800-b8ec-11eb-98a2-69ad0918c1fd.png)

If you chose four dimensions, you'd see a page in this form.

![Intro_dim](https://user-images.githubusercontent.com/45866787/118868107-76cef780-b8ec-11eb-9f52-8b0490b1dc2e.png)

### 2. Define the coordinate system (cartesian, spherical, etc.)

![Intro_dim](https://user-images.githubusercontent.com/45866787/118868153-85b5aa00-b8ec-11eb-9dd2-3d3ae734b646.png)

These are the available/most commonly used coordinate system components. If you want to add another element, go to line 42-43 
located in the `GRTC_GUI.py` file.

![image](https://user-images.githubusercontent.com/45866787/118860344-f1474980-b8e3-11eb-8114-cc9e9a1d6d24.png)


### 3. Define the diagonal components of the metric tensor

While defining the components of the tensor, write the expressions as you are writing them in python (i.e., use **, not ^). I have also defined most of the most common physics symbols, but if you think I am missing something, you can add it through 15-17 from the GRTC_GUI.py.

Here is an example of the `Schwarzschild Metric` where `r_s = 2GM/c^2`

![Intro_dim](https://user-images.githubusercontent.com/45866787/118871096-ea263880-b8ef-11eb-936e-461a229c4761.png)


### 4. Chose a tensor that you want to calculate.

Chose a tensor from the `Available Tensors` segment and click `Submit.`

## Getting Tensors / Tensor Types and Index Lowering/Raising

For instance, when you chose the `Christoffel Symbols,` you'll see a page like this.

![Intro_dim](https://user-images.githubusercontent.com/45866787/118871537-5739ce00-b8f0-11eb-810f-b3abf166db13.png)

You can change the type of the tensor and get any component from the given page.

![Intro_dim](https://user-images.githubusercontent.com/45866787/118871697-79335080-b8f0-11eb-9b42-0cbae91cac34.png)


# Non - GUI Version

### *Those who want to run the code from the .ipynb file, and don't want to use GUI, can follow the steps given below.*

### Required packages
sympy, numpy, itertools

## Getting Started

#### 0. Download the GRTC Main Folder (.ipynb files should run from that directory)
#### 1. Define the coordinate system (cartesian, spherical, etc.) 
#### 2. Define the diagonal components of the metric tensor

The first few lines of the code should look like this.

```
from GRTC import *
from sympy import symbols, sin, init_printing

init_printing()

# Defining the symbols in the coordinate system
t, r, theta, phi = symbols('t, r, theta, phi')

#Defining the coordinate system as a list
coord_sys = [t, r, theta, phi]

# Defining some extra symbols
G, m, a = symbols('G, m, a')

# Defining the diagonal components of the metric tensor
diag_comp = [-1, a**(-1), a**2, a * sin(theta)**2]

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

#### 1.`(1,0)` (contravariant) type tensor will be denoted by a string `'u'` and `(0,1)` (covariant) type tensor will be denoted by `'d'`. 

#### 2. To access the type of a given tensor one can use the `get_tensorname_type()` method.

For the case above it becomes,

`cs.get_christoffelsymbol_type()`

#### 3. In order to change the type of the tensor, one can use the `vary_tensorname_type()` method.

In this case, type the desired form in terms of `'u'` and `'d'`.

`chris_symbol03 = cs.vary_christoffelsymbol_type(chris_symbol, 'ddd')`

For instance, the code above will convert the type `(1,2)` Christoffel Symbol into type `(0,3).` 

## Some Extra Features 

#### To obtain the non-zero components of the Christoffel Symbol, Riemann Tensor or the Weyl Tensor type `nonzero_tensorname(xtensor).`

For instance,

`cs.nonzero_christoffelsymbol(chris_symbol)` 

or 

`rt.nonzero_riemanntensor(riemann_tensor)`

will show the desired output

## Notes 

#### 1. You can further study these examples on `example.ipynb`
#### 2. It is recommended to use Jupyter Notebook to see a better output (If you are working on .ipynb file)
#### 3. PySimpleGUI does not work on Jupyter Notebook.
#### 4. For some metrics, the [`nsimplify`](https://docs.sympy.org/latest/modules/simplify/simplify.html#nsimplify) method may not be working properly. In this case, you may try to adjust the Simplify function.
