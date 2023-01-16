# GRPy

GRPy is a python package that allows you to calculate the well-known tensors in general relativity, without *writing a single line of code*. In addition, you can apply many operations to 6 different type of fields, *in both 4D and 3D*.

> It's tested for GNU/Linux, however it should also work in Windows and Mac. If you ever encounter with a problem, feel free to create an issue.

## Current Features

### GR Tensor Objects

Either by using predefined coordinates, or by defining the coordinate system yourself, you can calculate:

1. Inverse Metric Tensor
2. Christoffel Symbol
3. Riemann Tensor
4. Ricci Tensor
5. Ricci Scalar
6. Weyl Tensor
7. Traceless Ricci Tensor
8. Einstein Tensor
9. Kretschmann Scalar

### Field Objects

Currently, there are 6 different field objects that you can carry out operations. These are:

1. Scalar Field
2. Type (1,0) Vector Field
3. Type (0,1) Vector Field
4. Type (2,0) Tensor Field
5. Type (1,1) Tensor Field
6. Type (0,2) Tensor Field

#### Operations on Fields

1. Varying the type of a given vector field
2. Calculating covariant and Lie derivatives for each field object (scalar, vector and tensor)
3. Checking the Killing field condition for a given vector field

## Overview

4D/Main Page          |  3D/Main Page
:-------------------------:|:-------------------------:
![4d_main](https://user-images.githubusercontent.com/45866787/212769611-8ac8d136-fba6-4e17-a5df-a737a19d1fb9.png) | ![3d_main](https://user-images.githubusercontent.com/45866787/212769627-15069c8a-bba2-41d8-a98e-5de8e7624931.png)

4D/Scalar Field Operations        |  4D/Vector Field Operations       | 4D/Tensor Field Operations
:-------------------------:|:-------------------------:|:-------------------------:
![4d_scalar](https://user-images.githubusercontent.com/45866787/212769650-d55d3001-db4e-4c79-ada5-cfcc1d40efb3.png) | ![4d_vector](https://user-images.githubusercontent.com/45866787/212769667-082904c3-6e77-48ab-b787-8dda0aa7e0a8.png) | ![4d_tensor](https://user-images.githubusercontent.com/45866787/212769682-1225764c-88ee-4092-9ac6-312de9608c27.png)

3D/Scalar Field Operations        |  3D/Vector Field Operations       | 3D/Tensor Field Operations
:-------------------------:|:-------------------------:|:-------------------------:
![3d_scalar](https://user-images.githubusercontent.com/45866787/212769736-171c0a1f-63a2-44f4-96ab-b86bf6eeef8f.png) |![3d_vector](https://user-images.githubusercontent.com/45866787/212769750-de725b69-0a9f-460f-b451-5e03ecd758c5.png) | ![3d_tensor](https://user-images.githubusercontent.com/45866787/212769770-1679b3c4-1b11-48c8-805e-0e51bb4a177b.png)

## Installation

You can easily install GRPy by either cloning the repository

    git clone https://github.com/seVenVo1d/grpy.git

or via downloading as ZIP. Later on, you can simply run

    python3 -m pip install -r requirements.txt

to install the requirements.

### pyclean support (optional)

I have added an optional code block in `grpy.py`, that will delete all the `.pyc` files and `__pycache__` directories. These are created after the program starts and can be annoying for some people. If you want to try it, install [pyclean](https://pypi.org/project/pyclean/) via

    python3 -m pip install pyclean

and uncomment the lines in the file.

## User Guide

Please take a look at the `docs/user_guide.md` for a summary of the GRPy. To see more detailed examples, you can look at the `demos` directory.

## Upcoming Features

1. Raising and lowering indices for a given tensor field
2. Gradient, Divergence, Curl and Laplace operations on fields
3. Partial and Covariant derivatives of the GR Tensors (Christoffel Symbol, Riemann Tensor, etc.)
4. Including more coordinate systems
5. Adding a button that prints the equations in LaTeX form
