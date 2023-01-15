# General Relativity Tensor Calculator by Graphical User Interface (GRTC-GUI)

GRTC-GUI allows you to calculate the well-known tensors in general relativity, without writing a single line of code. In addition, you can apply many operations to 6 different type of fields.

> It's tested for GNU/Linux but it should also work in Windows and Mac OS (if you encounter with a problem, feel free to create an issue).

## Current Features

### GR Tensor Objects

Either by using predefined coordinates or by defining the coordinate system yourself, you can calculate;

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

Currently, there are 6 different field objects that you can carry out operations. These fields are;

1. Scalar Field
2. Type (1,0) Vector Field
3. Type (0,1) Vector Field
4. Type (2,0) Tensor Field
5. Type (1,1) Tensor Field
6. Type (0,2) Tensor Field

#### Operations on Fields

1. Varying the type of the vector field
2. Calculating the covariant and Lie derivative of each field object (scalar, vector and tensor)
3. Check the Killing field condition for a given vector field

4D - GR TENSORS TAB          |  4D - FIELDS TAB
:-------------------------:|:-------------------------:
![](https://user-images.githubusercontent.com/45866787/212466258-6e10713a-6235-45a0-babe-010e1f0444be.png)  |  ![](https://user-images.githubusercontent.com/45866787/212466308-024668ae-c44b-46d5-a488-96efe8437e23.png)

## Installation

You can easily install GRTC-GUI by either cloning the repository:

    git clone https://github.com/seVenVo1d/grtc_gui

or via downloading as ZIP. Later on, you can simply run

    python3 -m pip install -r requirements.txt

to install the requirements.

### pyclean support (optional)

I have added an optional code block in `grtc_gui.py` that will delete all the `.pyc` files and `__pycache__` directories (these are created after the program starts and can be annoying for some people). If you want to try it, install [pyclean](https://pypi.org/project/pyclean/) via

    python3 -m pip install pyclean

and uncomment the lines in the file.

## User Guide

Please take a look at the `docs/user_guide.md` file for a summary of the GRTC-GUI. To see a more detailed usage, you can look at the `demos` directory.

## Upcoming Features

1. Raising and lowering indices for a given tensor field
2. Gradient, Divergence, Curl and Laplace operations on fields
3. Partial and Covariant derivatives of the GR Tensors (Christoffel Symbol, Riemann Tensor, etc.)
4. Including more coordinate systems
5. Adding a button that prints the equations in LaTeX form
