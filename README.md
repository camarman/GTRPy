# General Relativity Tensorial Calculations by Graphical User Interface (GRTC-GUI)

> ## Current Features
>
> ### 1. Calculating the Inverse Metric Tensor, Christoffel Symbol, Riemann Tensor, Ricci Tensor, Ricci Scalar, Weyl Tensor, Traceless Ricci Tensor, Einstein Tensor and, Kretschmann Scalar from a given metric and coordinate system (available in 3D and 4D)
>
> ### 2. Calculating [covariant derivative](https://en.wikipedia.org/wiki/Covariant_derivative#Covariant_derivative_by_field_type) for a given scalar, vector, and tensor fields (available in 3D and 4D)
>
> ### 3. Calculating [Lie Derivative](https://en.wikipedia.org/wiki/Lie_derivative) for a given scalar, vector, and tensor fields (available in 3D and 4D)

In this update, I have improved the simplification process and adjusted GUI page size for better visuals

> ## Upcoming Features
>
> ### 1. [Hawking Radiation Calculator](https://www.vttoth.com/CMS/physics-notes/311-hawking-radiation-calculator)
>
> ### 2. Calculating [Unruh temperature](https://en.wikipedia.org/wiki/Unruh_effect#Temperature_equation)
>
> ### 3. Checking if a vector field X is a killing field
>
> ### 4. Displaying killing vector equations for a given metric tensor
>
> ### 5. Displaying Geodesic Equations
>
> ### 6. Raising and lowering indices of a given tensor

## Requirements

1. `IPython.display`, `itertools`, `numpy`, `PIL`, `PySimpleGUI`, `sympy`
2. [`Latex`](https://www.latex-project.org/get/) (To produce images and equations)
3. (**OPTIONAL**) You'll also need three fonts; `Tahoma`, `Verdana`, and `Georgia`(These are the standard fonts for Windows, but if they are missing, you can download them online or change the font manually from the `GRTC_GUI.py`). It seems that when one of the font is missing, the PySimpleGUI runs with the default font, without giving error.

## Getting Started

### 0. Open the `GRTC Main` directory

### 1. Run the `GRTC_GUI.py` file

### 2. Choose a suitable dimension from the given page

You'll have two options

![main page](https://user-images.githubusercontent.com/45866787/124366100-d2afce80-dc55-11eb-908e-f949522ae51e.png)

If you choose four dimensions, you'll see a page in this form

![4d](https://user-images.githubusercontent.com/45866787/124366154-39cd8300-dc56-11eb-92d5-8d484fec8e57.png)

similarly, for three dimensions

![3d](https://user-images.githubusercontent.com/45866787/124366156-3d610a00-dc56-11eb-9b09-46e46f003a30.png)

### 3. Define the coordinate system (cartesian, spherical, etc.)

![coord_sys](https://user-images.githubusercontent.com/45866787/124366173-65506d80-dc56-11eb-829a-3fbef8e2b9c0.png)

These are the available/most commonly used coordinate system components. If you want to add another symbol, go to line `41-42` located in the `GRTC_GUI.py`.

![coordinate_symbols](https://user-images.githubusercontent.com/45866787/124366202-9af55680-dc56-11eb-9cd3-03cb15db5aa6.png)

### 4. Define the diagonal components of the metric tensor

Let us study the Schwarzschild metric for an example.

![schw_metric](https://user-images.githubusercontent.com/45866787/124366233-dbed6b00-dc56-11eb-96fd-361f666b492e.png)

## Tensors, Tensor Types, and Index Lowering/Raising

Choose a tensor from the `Tensors` segment and click `Submit`. For instance, when you choose the `Metric Tensor`, you'll see a page like this.

![metric_tensor](https://user-images.githubusercontent.com/45866787/124366247-f3c4ef00-dc56-11eb-854a-cc44ead5e390.png)

Later on, you can choose the `Christoffel Symbol` (or any other available tensor) from the `Tensors` segment.

![chris_symbol](https://user-images.githubusercontent.com/45866787/124366269-2a026e80-dc57-11eb-97cf-eb35e1e45b6f.png)

You can change the type of the tensor

![chris_1](https://user-images.githubusercontent.com/45866787/124366310-751c8180-dc57-11eb-936e-d82d5d478929.png)

and get any component from the given page.

![chris_2](https://user-images.githubusercontent.com/45866787/124366311-76e64500-dc57-11eb-97e5-da7be0aaf648.png)

## Covariant Derivative by Field Type

There are 6 different options that you can choose to calculate the covariant derivative of a field. These are;

1. ### `Scalar Field`

2. ### `Type (1,0) Vector Field`

3. ### `Type (0,1) Vector Field`

4. ### `Type (2,0) Tensor Field`

5. ### `Type (1,1) Tensor Field`

6. ### `Type (0,2) Tensor Field`

#### Scalar Fields

When you choose `Scalar Field` from the main page, you'll see a page in this form

![scalar_field](https://user-images.githubusercontent.com/45866787/124366363-f3792380-dc57-11eb-992d-b8a6dc35f043.png)

From here, you can form a scalar field and choose the covariant derivative component that you want to calculate.

![scalar_1](https://user-images.githubusercontent.com/45866787/124366365-f6741400-dc57-11eb-8a3c-7d5b650140db.png)

For this type of field, we obtain

![scalar_2](https://user-images.githubusercontent.com/45866787/124366367-f8d66e00-dc57-11eb-9c7f-7201b51ca20b.png)

#### Vector Fields

For example, when you choose `Type (1,0) Vector Field`, you'll see a page in this form

![vector_field](https://user-images.githubusercontent.com/45866787/124366388-363afb80-dc58-11eb-918d-ca0251222593.png)

From here, you can form a vector field and choose the covariant derivative component that you want to calculate. Such as for

![vector_field_2](https://user-images.githubusercontent.com/45866787/124366391-3935ec00-dc58-11eb-83f1-8fcfa42e032a.png)

You'll obtain

![vector_field_3](https://user-images.githubusercontent.com/45866787/124366393-3cc97300-dc58-11eb-8aca-e5d2f1e3672f.png)

#### Tensor Fields

For example, when you choose `Type (0,2) Tensor Field` you'll see a page in this form

![tensor_field](https://user-images.githubusercontent.com/45866787/124366466-c5e0aa00-dc58-11eb-89cb-6b2ca05a0be7.png)

From here, you can form a tensor field and choose the covariant derivative component that you want to calculate.

![tensor_field_1](https://user-images.githubusercontent.com/45866787/124366468-ca0cc780-dc58-11eb-8123-2fc0a2b0c47f.png)

For this type of field, we obtain

![tensor_field_2](https://user-images.githubusercontent.com/45866787/124366469-cc6f2180-dc58-11eb-82b3-8f6c2742bce8.png)

## Lie Derivative by Field Type

There are 6 different options that you can choose to calculate the lie derivative of a field with respect to vector field X. Similar to the covariant derivative case
you'll have 6 different field options. These are;

1. ### `Scalar Field`

2. ### `Type (1,0) Vector Field`

3. ### `Type (0,1) Vector Field`

4. ### `Type (2,0) Tensor Field`

5. ### `Type (1,1) Tensor Field`

6. ### `Type (0,2) Tensor Field`

For this case let us consider `Type (1,1) tensor field`.

![lie_derivative](https://user-images.githubusercontent.com/45866787/124366553-50290e00-dc59-11eb-974e-634c673f50b7.png)

From here you can fill the `Type (1,1) tensor field` and also the vector field `X`

![lie_der_1](https://user-images.githubusercontent.com/45866787/124366566-63d47480-dc59-11eb-97c4-f773053d5303.png)

For instance, this type of field will give us

![lie_der_2](https://user-images.githubusercontent.com/45866787/124366576-7353bd80-dc59-11eb-9bef-1163b1a05934.png)

## Non - GUI Version

Those who want to run the code from the `.ipynb` file, and don't want to use GUI, can follow the steps given in the `example.ipynb`.
