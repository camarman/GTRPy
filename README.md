## General-Relativity-Tensor-Calculations (GRTC) by Graphical User Interface (GUI)

#### 1. Calculating the Inverse Metric Tensor, Christoffel Symbol, Riemann Tensor, Ricci Tensor, Ricci Scalar, Weyl Tensor, Traceless Ricci Tensor, Einstein Tensor and, Kretschmann Scalar from the given metric 

#### 2. [Covariant Derivative](https://en.wikipedia.org/wiki/Covariant_derivative#Covariant_derivative_by_field_type) for Scalar, Vector and Tensor Fields (only in 4D)

> ## Upcoming Features
> #### **1. Covariant Derivative for Scalar, Vector and Tensor Fields in 3D**
> 
> #### **2. [Lie Derivative](https://en.wikipedia.org/wiki/Lie_derivative)**
>
> #### **3. Hawking Radiation Calculator**

#### Requirements
1. `IPython.display`, `itertools`, `numpy`, `PIL`, `PySimpleGUI`, `sympy`
2. `Latex` (To produce images)
3. You'll also need fonts such as  `Tahoma`, `Bookman`, and `Georgia.` (These are the standard fonts for Windows, but if they are missing, you can download it online or change the font manually from the `GRTC_GUI.py`.

### Getting Started

#### 1. Run the `GRTC_GUI.py` file
#### 2. Choose a suitable dimension from the given page 

You'll have two options. 

![main_page](https://user-images.githubusercontent.com/45866787/123514014-078db580-d699-11eb-82a3-4b675d5a0620.png)

If you choose four dimensions, you'll see a page in this form.

![4d](https://user-images.githubusercontent.com/45866787/123513907-7cacbb00-d698-11eb-94d9-0c639209287d.png)

and for three dimensions,

![3d](https://user-images.githubusercontent.com/45866787/123514034-29873800-d699-11eb-9f5a-3d4d124cf408.png)


#### 3. Define the coordinate system (cartesian, spherical, etc.)

![coord_sys](https://user-images.githubusercontent.com/45866787/123513964-c695a100-d698-11eb-905f-e9473cfad125.png)

These are the available/most commonly used coordinate system components. If you want to add another element, go to line `52-53` located in the `GRTC_GUI.py`.

![coordinates](https://user-images.githubusercontent.com/45866787/123514068-694e1f80-d699-11eb-8b16-3d4840b1d0b8.png)

#### 4. Define the diagonal components of the metric tensor

Here is an example 

![diag](https://user-images.githubusercontent.com/45866787/123517480-dff31900-d6a9-11eb-9616-828eed6c8896.png)

#### 5. Choose a tensor that you want to calculate.

Choose a tensor from the `Available Tensors` segment and click `Submit.`

### Getting Tensors / Tensor Types and Index Lowering/Raising

For instance, when you choose the `Metric Tensor`, you'll see a page like this.

![metric_tensor](https://user-images.githubusercontent.com/45866787/123517493-f8fbca00-d6a9-11eb-9e3b-71780a4b7eac.png)

And later on you can choose the `Christoffel Symbol` option to see

![chris_symbol](https://user-images.githubusercontent.com/45866787/123517511-1335a800-d6aa-11eb-9caa-98dcd5124a57.png)

You can change the type of the tensor and get any component from the given page.

![chris_symbol1](https://user-images.githubusercontent.com/45866787/123517557-542dbc80-d6aa-11eb-82c3-693ce8535454.png)

![chris_symbol2](https://user-images.githubusercontent.com/45866787/123517576-6c054080-d6aa-11eb-8ef1-e6ddd69def96.png)

## Covariant Derivative

There are 6 different options that you can choose to calculate the Covariant Derivative of a field. These are;

1. `Scalar Field` 
2. `Type (1,0) Vector Field` 
3. `Type (0,1) Vector Field`
4. `Type (2,0) Tensor Field`
5. `Type (1,1) Tensor Field`
6. `Type (0,2) Tensor Field`

For example, when you choose `Type (1,0) Vector Field`, you'll see a page in the form of

![cov_der](https://user-images.githubusercontent.com/45866787/123517695-22692580-d6ab-11eb-9946-88bb2629c34a.png)

From here you can form your vector field and choose the covariant derivative component that you want to calculate. 

Such as for

![cov_der](https://user-images.githubusercontent.com/45866787/123517744-62300d00-d6ab-11eb-8a6f-958dbb8f3277.png)

You'll see a page in this form

![cov_der_result](https://user-images.githubusercontent.com/45866787/123517767-84298f80-d6ab-11eb-8064-8e50acc98552.png)

## Non - GUI Version

*Those who want to run the code from the `.ipynb` file, and don't want to use GUI, can follow the steps given below.*

#### Required packages
`itertools`, `numpy`, `sympy`

### Getting Started

#### 1. Define the coordinate system (cartesian, spherical, etc.) 
#### 2. Define the diagonal components of the metric tensor

The first few lines of the code should look like this.

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

### Obtaining Tensors

After defining the diagonal components of the metric tensor, we can calculate/obtain the tensors by just assigning them into a variable and using the `get_tensorname()` method.

For instance, to obtain the Christoffel Symbol, it is sufficient to write this line of code in Jupyter Notebook.

```
# Obtaining the Christoffel Symbol
cs = ChristoffelSymbol(diag_comp, coord_sys)
chris_symbol = cs.get_christoffelsymbol()
chris_symbol
```

### Tensor Types and Index Lowering/Raising

#### 1.`(1,0)` (contravariant) type tensor will be denoted by a string `'u'` and `(0,1)` (covariant) type tensor will be denoted by `'d'`. 

#### 2. To access the type of a given tensor one can use the `get_tensorname_type()` method.

For the case above it becomes,

`cs.get_christoffelsymbol_type()`

#### 3. In order to change the type of the tensor, one can use the `vary_tensorname_type()` method.

In this case, type the desired tensor form in terms of `'u'` and `'d'`.

```
# Varying type 'udd' Christoffel Symbol to 'ddd'
chris_symbol03 = cs.vary_christoffelsymbol_type(chris_symbol, 'ddd') 
chris_symbol03
```

For instance, the code above will convert the type `(1,2)` Christoffel Symbol into type `(0,3).` 

### Some Extra Features 

To obtain the non-zero components of the Christoffel Symbol, Riemann Tensor or the Weyl Tensor type `nonzero_tensorname(xtensor)`.
For instance,

```
# Obtaining the non-zero components of the given Christoffel Symbol for type ddd
cs.nonzero_christoffelsymbol(chris_symbol03)
```

or 

```
# Obtaining the non-zero components of the Riemann Tensor for type uddd
rt.nonzero_riemanntensor(riemann_tensor)
```

will show the desired output. These and more can be found on `example.ipynb`.
