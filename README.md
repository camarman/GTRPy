# General Relativity Tensorial Calculations by Graphical User Interface (GRTC-GUI)

GRTC-GUI allows you to calculate the well-known tensors in general relativity, without writing a single line of code. In addition, you can apply many operations to 6 different fields. New features will be available in the following weeks.

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
> #### 2.1 Operations on Fields
>
> 2.1.1 You can calculate the Covariant derivative and Lie derivative by using these fields
>
> 2.1.2 You can check for a given type (1,0) or type (0,1) vector field satisfies the >killing field condition or not
>

## User Guide

### 1. Run the `grtcgui.py` file

### 2. Choose a suitable dimension from the given page

You'll have two options

![ndim](https://user-images.githubusercontent.com/45866787/126603724-a918ccd6-5628-49b0-8a05-5d2c8d44037e.png)

If you choose four dimensions, you'll see a page in this form

![4d](https://user-images.githubusercontent.com/45866787/126603740-8cc88079-4003-462c-a36e-a8c23ec151de.png)

similarly, for three dimensions

![3d](https://user-images.githubusercontent.com/45866787/126603750-c0e58333-c4c9-4c05-a0d5-aedfd22caaee.png)

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

![sch](https://user-images.githubusercontent.com/45866787/126603788-2bed9de3-45d6-4801-9885-d84760f9f3bc.png)

## Tensors, Tensor Types, and Index Lowering/Raising

Just click one of the tensor buttons, which will lead you to the default page of the choosen tensor.

![chris](https://user-images.githubusercontent.com/45866787/126603809-1cc76f5c-3ce9-46ff-b275-204bc0d974a1.png)

Later on, you can change the type of the tensor and get any component from the given page.

![chris2](https://user-images.githubusercontent.com/45866787/126603815-ec26d2e7-974f-41ff-83e3-8e8b0c53364f.png)

## Fields

If you click on the Fields tab you'll see the 6 available fields.

![fieldstab](https://user-images.githubusercontent.com/45866787/126603828-5627b713-858b-41fc-b154-a95f52b68920.png)

From there, you can pick the field that you want to calculate, the Lie derivative or Covariant derivative.
For instance, if you choose `Type (1,0) Tensor Field`, you'll see a page in this format.

![vectorfield](https://user-images.githubusercontent.com/45866787/126834943-766261e5-4bf3-49bb-a355-d57dc12021d1.png)

From there, after typing your field, you can perform any available operation.

> ## Upcoming Features
>
> 1. Displaying killing vector equations for a given metric tensor
>
> 2. Displaying geodesic equations
>
> 3. Raising and lowering indices of a given vector and tensor fields
>
> 4. Gradient, Divergence, Curl and Laplace operations on fields
>
> 5. Partial and Covariant derivatives of the GR Tensors (Christoffel Symbol, Riemann Tensor, Ricci Tensor, Einstein Tensor etc.)
>
> 6. Including more coordinate systems for both 3D and 4D
