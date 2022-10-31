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

Later on choose a suitable dimension from the gui. If you choose four dimensions, you'll see a page in this form

similarly, for three dimensions

2) Define the coordinate system (cartesian, spherical, etc.). You can either choose a predefined coordinate system or type your own metric tensor. Currently predefined coordinates;

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

Later on, you can change the type of the tensor and get any component from the given page.

## Fields

If you click on the Fields tab you'll see the 6 available fields.

From there, you can pick the field that you want to calculate. From there, after typing your field, you can perform any available operation.

## Upcoming Features

1) Displaying killing vector equations for a given metric tensor
2) Displaying geodesic equations
3) Raising and lowering indices of a given vector and tensor fields
4) Gradient, Divergence, Curl and Laplace operations on fields
5) Partial and Covariant derivatives of the GR Tensors (Christoffel Symbol, Riemann Tensor, Ricci Tensor, Einstein Tensor etc.)
6) Including more coordinate systems for both 3D and 4D
