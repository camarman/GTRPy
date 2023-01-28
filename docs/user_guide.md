# User Guide

## Starting the Program

You can start the program by typing

    python3 -m gtrpy.run

in the terminal.

## Welcome Page and Choosing Dimension

![greetings](https://user-images.githubusercontent.com/45866787/213306039-51dd652a-d99e-41b5-9ca9-6fe6a4f7aa35.png)

Later on choose a suitable dimension from the GUI. If you choose four dimensions, you'll see a page in this form

## GTRPy in 4D

### Defining Coordinate System

In GTRPy, you can define the coordinate system yourself. While defining the coordinate system, you can choose from the given coordinate system symbols

    t, x, y, z, r, v, r, theta, phi, rho, sigma, psi, eta, tau, xi, T, X

or you can simply choose one of the predefined coordinate systems. Currently predefined coordinates in 4D are:

    1. Cartesian Coordinates
    2. Cylindrical Coordinates
    3. Spherical Coordinates
    4. Conform-Compactified Coordinates
    5. Rindler Coordinates
    6. Schwarzschild Coordinates
    7. Eddington-Finkelstein Coordinates

and in 3D:

    1. Cartesian Coordinates
    2. Cylindrical Coordinates
    3. Spherical Coordinates

To change the coordinate system you can choose from the available coordinate systems and later on just click on the `Change Coordinate System` button. In this guide, let us study the *Schwarzschild Coordinate System* as an example.

![sch](https://user-images.githubusercontent.com/45866787/213306169-1fa3f7fd-20ee-408f-b840-9ad27f26a495.png)

> See `demos/demo_6.md` to learn how to add more coordinate system symbols

### Defining the Metric Tensor

As we know the metric tensor is the key element in the GTR theory. By only defining the metric tensor one can calculate many of the important GTR tensors.

To define the metric tensor you can just type any metric tensor you want. See `demos/demo_1.md` for more information about how to type math variables in GTRPy.

### GTR Tensors

![4d_main](https://user-images.githubusercontent.com/45866787/213306076-9153466c-6aeb-4776-9208-10c953a80e4a.png)

As we can see there are many defined GTR tensors in GTRPy. Let us study the Christoffel Symbol as an example

## Operations on GTR Tensors

First click on the `Christoffel Symbol` button

![chris](https://user-images.githubusercontent.com/45866787/215287954-af722d40-3d3f-44e9-9fcb-8232becabe4c.png)

Later on, you can change the type of the `Christoffel Symbol` and get any component from the given page

![chris_up](https://user-images.githubusercontent.com/45866787/215287959-cc4fb77c-43d4-4671-b3b4-2220e806ab9e.png)

If you click on the `Get LaTeX` button, the program will produce the LaTeX equation of the `Christoffel Symbol` and save it under the `logs` directory.

## Fields

If you click on the Fields tab you'll see the 6 available fields.

![fields_tab](https://user-images.githubusercontent.com/45866787/213306249-d90a9635-e07a-42db-8098-6a3d24000986.png)

From there, you can pick any field that you want to calculate. After typing your field component, you can perform any available operation.

### Operations on Fields

As an example let us study the `Type (1,0) Vector Field` under the *Schwarzschild Coordinate System*.

First, let us create a random vector field:


By clicking on the `Calculate` button under the `Vary Type` frame, you can easily change the type of the vector field and get its LaTeX equation.


Later on you can calculate the Covariant derivative


or by providing the `X` vector field, you can calculate the Lie Derivative


and Finally you can check if the given vector field is Killing Field or not.