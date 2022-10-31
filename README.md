# General Relativity Tensor Calculator by Graphical User Interface (GRTC-GUI)

GRTC-GUI allows you to calculate the well-known tensors in general relativity, without writing a single line of code. In addition, you can apply many operations to 6 different fields. It works in Linux, Mac OS and Windows.

## Current Features

### GR Tensor Objects

Either by using predefined coordinates or by defining the coordinate system yourself, you can calculate the Inverse Metric Tensor, Christoffel Symbol, Riemann Tensor, Ricci Tensor, Ricci Scalar, Weyl Tensor, Traceless Ricci Tensor, Einstein Tensor and, Kretschmann Scalar.

### Field Objects

Currently, there are 6 different field objects that you can carry out operations. These fields are;

1) Scalar Field
2) Type (1,0) Vector Field
3) Type (0,1) Vector Field
4) Type (2,0) Tensor Field
5) Type (1,1) Tensor Field
6) Type (0,2) Tensor Field

#### Operations on Fields

1) You can calculate the Covariant derivative and Lie derivative by using these fields
2) You can check for a given type (1,0) or type (0,1) vector field satisfies the 
killing field condition or not

## Installation

You can easily install GRTC-GUI via

    git clone https://github.com/seVenVo1d/grtc_gui

Later on run

    python3 -m pip install -r requirements.txt

to install the requirements

## User Guide

1) To run the program type

        python3 grtc_gui.py

![greeting_page](https://user-images.githubusercontent.com/45866787/198973226-3cb1b794-15ca-4926-9b5f-55743dac78bd.png)

Later on choose a suitable dimension from the gui. If you choose four dimensions, you'll see a page in this form

![4d](https://user-images.githubusercontent.com/45866787/198973300-ac36cd0f-1b01-4530-80c3-7c6d0da3ccf8.png)

similarly, for three dimensions

![3d](https://user-images.githubusercontent.com/45866787/198973467-1391e0ba-be1f-438c-a5bf-40a4d7494978.png)

2) Define the coordinate system (cartesian, spherical, etc.). You can either choose a predefined coordinate system or type your own metric tensor. Currently predefined coordinates for 4D;

    1) Cartesian Coordinates
    2) Cylindrical Coordinates
    3) Spherical Coordinates
    4) Conform-Compactified Coordinates
    5) Rindler Coordinates
    6) Schwarzschild Coordinates
    7) Eddington-Finkelstein Coordinates

Let us study the Schwarzschild Coordinates as an example.

## Tensors, Tensor Types, and Index Lowering/Raising

Just click one of the tensor buttons, which will lead you to the default page of the choosen tensor.

![chris_1](https://user-images.githubusercontent.com/45866787/198973666-7b8e5607-0591-449a-8244-cdcac9bbca58.png)

Later on, you can change the type of the tensor and get any component from the given page.

![chris_2](https://user-images.githubusercontent.com/45866787/198973890-22bed6aa-c5fa-4238-89bb-72a29ea82e85.png)

## Fields

If you click on the Fields tab you'll see the 6 available fields.

![fields_tab](https://user-images.githubusercontent.com/45866787/198974014-29cd448d-9a8c-4c3c-ae4e-1de98e862a86.png)

From there, you can pick the field that you want to calculate. From there, after typing your field, you can perform any available operation.

![scalar](https://user-images.githubusercontent.com/45866787/198974191-763724b2-22cb-4196-b39e-87b52f509f52.png)

![vector](https://user-images.githubusercontent.com/45866787/198974154-9478f0a5-b556-47c6-9496-f6f933a29a58.png)

![tensor](https://user-images.githubusercontent.com/45866787/198974166-7b9e7941-582f-485b-911a-1b7a8a01194e.png)

## Upcoming Features

1) Displaying killing vector equations for a given metric tensor
2) Displaying geodesic equations
3) Raising and lowering indices of a given vector and tensor fields
4) Gradient, Divergence, Curl and Laplace operations on fields
5) Partial and Covariant derivatives of the GR Tensors (Christoffel Symbol, Riemann Tensor, Ricci Tensor, Einstein Tensor etc.)
6) Including more coordinate systems for both 3D and 4D
