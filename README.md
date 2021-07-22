# General Relativity Tensorial Calculations by Graphical User Interface (GRTC-GUI)

GRTC-GUI allows you to calculate the well-known tensors in general relativity, without writing a single line of code. It also has built-in features that will enable you to calculate the Covariant derivative and Lie derivative for 6 different types of fields. New features will be available in the following weeks.

> ## Current Features
>
> ### 1. GR Tensor Objects
>
> Either by using predefined coordinates or by defining the coordinate system yourself, you can calculate the Inverse Metric Tensor, Christoffel Symbol, Riemann Tensor, Ricci Tensor, Ricci Scalar, Weyl Tensor, Traceless Ricci Tensor, Einstein Tensor and, Kretschmann Scalar.
>
> ### 2. Field Objects
>
> Currently, there are 6 different field objects that you can carry out operations. These fields are;
>
> 1. `Scalar Field`
>
> 2. `Type (1,0) Vector Field`
>
> 3. `Type (0,1) Vector Field`
>
> 4. `Type (2,0) Tensor Field`
>
> 5. `Type (1,1) Tensor Field`
>
> 6. `Type (0,2) Tensor Field`
>
> You can calculate the Covariant derivative and Lie derivative by using these fields.

## User Guide

### 1. Run the `grtcgui.py` file

### 2. Choose a suitable dimension from the given page

You'll have two options

If you choose four dimensions, you'll see a page in this form

similarly, for three dimensions

### 3. Define the coordinate system (cartesian, spherical, etc.)

You can either choose a predefined coordinate system or type your own metric tensor

#### Currently Predefined Coordinates

1. Cartesian Coordinates
2. Cylindrical Coordinates
3. Spherical Coordinates
4. Conform-Compactified Coordinates
5. Rindler Coordinates
6. Schwarzschild Coordinates
7. Eddington-Finkelstein Coordinates

Let us study the Schwarzschild Coordinates as an example.

## Tensors, Tensor Types, and Index Lowering/Raising

Just click one of the tensor buttons, which will lead you to the default page of the choosen tensor.

Later on, you can change the type of the tensor and get any component from the given page.

## Fields

If you click on the Fields tab you'll see the 6 available fields.

From there, you can pick the field that you want to calculate, the Lie derivative or Covariant derivative.
For instance, if you choose `Type (0,2) Tensor Field`, you'll see a page in this format.

From there, after typing your field, you can perform any available operation.

> ## Upcoming Features
>
> ### 1. Checking if a vector field, X, is a killing field
>
> ### 2. Displaying killing vector equations for a given metric tensor
>
> ### 3. Displaying geodesic equations
>
> ### 4. Raising and lowering indices of a given vector and tensor fields
>
> ### 5. Gradient, Divergence, Curl and Laplace operations on fields
>
> ### 6. Partial and Covariant derivatives of the GR Tensors (Christoffel Symbol, Riemann Tensor, Ricci Tensor, Einstein Tensor etc.)
>
> ### 7. Including more coordinate systems for both 3D and 4D
