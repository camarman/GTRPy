# General Relativity Tensor Calculator by Graphical User Interface (GRTC-GUI)

GRTC-GUI allows you to calculate the well-known tensors in general relativity, without writing a single line of code. In addition, you can apply many operations to 6 different type of fields. It's tested for GNU/Linux but it should also work in Windows and Mac (if you encounter with a problem, feel free to create an issue).

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

1) You vary the type of the vector field from (1,0) to (0,1) or vice versa
2) You can calculate the Covariant derivative and Lie derivative by using these fields
3) You can check for a given type (1,0) or type (0,1) vector field satisfies the
killing field condition or not

## Installation

You can easily install GRTC-GUI via

    git clone https://github.com/seVenVo1d/grtc_gui

Later on run

    python3 -m pip install -r requirements.txt

to install the requirements.

## User Guide

Please take a look at `docs/user_guide.md` for a summary of the GRTC-GUI. To see more examples you can look at `demos` directory.

## Upcoming Features

1) Raising and lowering indices for a given tensor field
2) Gradient, Divergence, Curl and Laplace operations on fields
3) Partial and Covariant derivatives of the GR Tensors (Christoffel Symbol, Riemann Tensor, Ricci Tensor, Einstein Tensor etc.)
4) Including more coordinate systems for both 3D and 4D
5) Adding a button that also prints the LaTeX version of the equations
