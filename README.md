# General Relativity Tensor Calculator by Graphical User Interface (GRTC-GUI)

GRTC-GUI allows you to calculate the well-known tensors in general relativity, without *writing a single line of code*. In addition, you can apply many operations to 6 different type of fields, *in both 4D and 3D*.

> It's tested for GNU/Linux. However, it should also work in Windows and Mac OS. If you ever encounter with a problem, feel free to create an issue.

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
![4d_main_page](https://user-images.githubusercontent.com/45866787/212466258-6e10713a-6235-45a0-babe-010e1f0444be.png)  |  ![3d_main_page](https://user-images.githubusercontent.com/45866787/212466276-ced0e2eb-ce5e-4f3a-966a-f5f286252e72.png)

4D/Scalar Field Operations        |  4D/Vector Field Operations       | 4D/Tensor Field Operations
:-------------------------:|:-------------------------:|:-------------------------:
![4d_scalar](https://user-images.githubusercontent.com/45866787/212466315-315a6269-d84f-4bd3-92a1-e0d64e21742e.png)  |  ![4d_vector](https://user-images.githubusercontent.com/45866787/212466320-5d5e31a0-8c1d-49d6-a928-f844c7cf04c1.png)   |  ![4d_tensor](https://user-images.githubusercontent.com/45866787/212466322-8f25f5a5-8345-4b71-98ef-721c7eaa0c92.png)

3D/Scalar Field Operations        |  3D/Vector Field Operations       | 3D/Tensor Field Operations
:-------------------------:|:-------------------------:|:-------------------------:
![3d_scalar](https://user-images.githubusercontent.com/45866787/212533742-ed8e4dba-4274-4fe0-8006-3394c81df32f.png) | ![3d_vector](https://user-images.githubusercontent.com/45866787/212533751-feb4b063-5923-4536-bcc1-708a9a6b22be.png) | ![3d_tensor](https://user-images.githubusercontent.com/45866787/212533758-36e05917-8753-4aa0-931f-9a66c8c7f6f5.png)

## Installation

You can easily install GRTC-GUI by either cloning the repository

    git clone https://github.com/seVenVo1d/grtc_gui

or via downloading as ZIP. Later on, you can simply run

    python3 -m pip install -r requirements.txt

to install the requirements.

### pyclean support (optional)

I have added an optional code block in `grtc_gui.py`, that will delete all the `.pyc` files and `__pycache__` directories. These are created after the program starts and can be annoying for some people. If you want to try it, install [pyclean](https://pypi.org/project/pyclean/) via

    python3 -m pip install pyclean

and uncomment the lines in the file.

## User Guide

Please take a look at the `docs/user_guide.md` for a summary of the GRTC-GUI. To see more detailed examples, you can look at the `demos` directory.

## Upcoming Features

1. Raising and lowering indices for a given tensor field
2. Gradient, Divergence, Curl and Laplace operations on fields
3. Partial and Covariant derivatives of the GR Tensors (Christoffel Symbol, Riemann Tensor, etc.)
4. Including more coordinate systems
5. Adding a button that prints the equations in LaTeX form
