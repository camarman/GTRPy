# GTRPy

GTRPy is a python package, that allows you to calculate the well-known tensors in General Theory of Relativity without *writing a single line of code*. Furthermore, you can apply many operations to 6 different type of fields, *in both 3D and 4D*.

> It's tested for GNU/Linux, however it should also work in macOS. If you ever encounter with a problem, feel free to create an issue.

## Installation

You can easily install the GTRPy via

    python3 -m pip install gtrpy

or, you can directly clone the repository

    git clone https://github.com/seVenVo1d/GTRPy.git

## Requirements

Install the requirements by running

    python3 -m pip install numpy Pillow pysimplegui sympy

Additionally, you will also need `tkinter` and `LaTeX` to run the GTRPy. In Fedora Linux, these can be easily installed by running

    sudo dnf install python3-tkinter
    sudo dnf install texlive-scheme-full

You can look for your distributions package manager and search for an equivalent installation method.

## User Guide

To start GTRPy, simply run

    python3 -m gtrpy.run

from the terminal (it does not matter what directory you are in, *if* you installed it via `pip`). The program will create the `logs` directory, under your current directory, which will contain the outputs of the performed operations.

> Please take a look at the `docs/user_guide.md` for a summary of the GTRPy. To see more detailed examples, you can look at the `demos` directory.

## Current Features

### GTR Tensors

Either by using predefined coordinates or by defining the coordinate system yourself, you can calculate:

1. Inverse Metric Tensor
2. Christoffel Symbol
3. Riemann Tensor
4. Ricci Tensor
5. Ricci Scalar
6. Weyl Tensor
7. Traceless Ricci Tensor
8. Einstein Tensor
9. Kretschmann Scalar

### Fields

Currently, there are 6 different type of fields that you can carry out operations. These are:

1. Scalar Field
2. Type (1,0) Vector Field
3. Type (0,1) Vector Field
4. Type (2,0) Tensor Field
5. Type (1,1) Tensor Field
6. Type (0,2) Tensor Field

### Available Operations in GTRPy

1. Print out the equations obtained from each operation by clicking a single button
2. Checking the Killing field condition for a given vector field
3. Varying the type of a given vector and tensor field
4. Calculating Covariant and Lie derivatives for scalar, vector and tensor fields

## Overview

4D/Main Page          |  3D/Main Page
:-------------------------:|:-------------------------:
![4d_main](https://user-images.githubusercontent.com/45866787/213305163-b6470289-e167-4ffd-ab18-d592ae19011e.png) | ![3d_main](https://user-images.githubusercontent.com/45866787/213305193-9efe501f-0347-4166-a487-2cbdee3fe24c.png)

4D/Scalar Field        |  4D/Vector Field       | 4D/Tensor Field
:-------------------------:|:-------------------------:|:-------------------------:
![4d_scalar](https://user-images.githubusercontent.com/45866787/212769650-d55d3001-db4e-4c79-ada5-cfcc1d40efb3.png) | ![4d_vector](https://user-images.githubusercontent.com/45866787/212769667-082904c3-6e77-48ab-b787-8dda0aa7e0a8.png) | ![4d-tensor](https://user-images.githubusercontent.com/45866787/215287844-45bb7c97-3369-43b8-a4de-96e712216acb.png)

3D/Scalar Field        |  3D/Vector Field       | 3D/Tensor Field
:-------------------------:|:-------------------------:|:-------------------------:
![3d_scalar](https://user-images.githubusercontent.com/45866787/212769736-171c0a1f-63a2-44f4-96ab-b86bf6eeef8f.png) |![3d_vector](https://user-images.githubusercontent.com/45866787/212769750-de725b69-0a9f-460f-b451-5e03ecd758c5.png) | ![Screenshot from 2023-01-28 22-47-14](https://user-images.githubusercontent.com/45866787/215287851-73694819-fb9e-4d14-88c8-36718a5e1f1d.png)

## Upcoming Features

1. Gradient, Divergence, Curl and Laplace operations on fields
2. Partial and Covariant derivatives of the GTR tensors
3. Including more coordinate systems

## Contributing

I am looking for developers who would like to contribute to the project. If you are interested, feel free to create an issue by stating how would you like to contribute. Any help or idea is welcomed. For more information you can also look at the `CONTRIBUTING.md`.
