# User Guide

## Starting the Program

You can start the program by typing

    python3 -m gtrpy.run

in the terminal.

## Welcome Page and Choosing Dimension

![greetings](https://user-images.githubusercontent.com/45866787/213306039-51dd652a-d99e-41b5-9ca9-6fe6a4f7aa35.png)

Later on choose a suitable dimension from the GUI. If you choose 4D, you'll see a page in this form:

![4d-main](https://user-images.githubusercontent.com/45866787/215288897-5f1e528d-539e-4237-b200-f126d9618037.png)

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

To change the coordinate system you can choose from the available coordinate systems and later on just click on the `Change Coordinate System` button.

In this guide, let us study the *Schwarzschild Coordinate System* as an example.

![sch](https://user-images.githubusercontent.com/45866787/213306169-1fa3f7fd-20ee-408f-b840-9ad27f26a495.png)

> See `demos/demo_6.md` to learn how to add more coordinate system symbols

### Defining the Metric Tensor

As we know the metric tensor is the key element in the General Theory of Relativity. By only defining the metric tensor one can calculate many of the important GR tensors.

To define the metric tensor you can just fill the empty fields in the **Metric Tensor** Frame.

> See `demos/demo_1.md` for more information about how to type math variables in GTRPy.

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

![fields-tab](https://user-images.githubusercontent.com/45866787/215289114-da348b6b-2fd3-4c2d-aeea-11ff3d6d648a.png)

From there, you can pick any field that you want to calculate. After typing your field component, you can perform any available operation.

### Operations on Fields

As an example let us study the `Type (1,0) Vector Field` under the *Schwarzschild Coordinate System*.

![vector-field](https://user-images.githubusercontent.com/45866787/215289122-0b35f931-4e3c-4cbc-97b4-7f09820c70f7.png)

First, let us create a random vector field:

![random vector-field](https://user-images.githubusercontent.com/45866787/215289322-482a05b8-92c9-4531-a7e3-e56745866799.png)

By clicking on the *Calculate* button under the **Vary Type** frame, you can easily change the type of the vector field and obtain the LaTeX equation.

![vary-type](https://user-images.githubusercontent.com/45866787/215289327-ea31e0a3-52cc-4ee1-89f3-7ad0469e708c.png)

Later on you can calculate the Covariant derivative for any component

![cov-1](https://user-images.githubusercontent.com/45866787/215289336-f96cdf0e-a3bb-4f66-99d3-fc3eea53d54b.png)

![cov-2](https://user-images.githubusercontent.com/45866787/215289347-ab72ac84-ed88-4ed1-89dd-fb8bf076abbe.png)

or by providing the `X` vector field, you can calculate the Lie Derivative

![X-vector](https://user-images.githubusercontent.com/45866787/215289383-a2f208f6-8059-49fa-ab51-248b83add299.png)

![lie-derivative](https://user-images.githubusercontent.com/45866787/215289391-0fcda443-30fd-42d2-8e99-3860d3ff562e.png)

and finally you can check if the given vector field is Killing Field or not

![killing-field](https://user-images.githubusercontent.com/45866787/215289404-bd8919a5-044b-42ee-974f-cd5c17d0e905.png)
