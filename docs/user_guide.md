# User Guide

## Starting the GTRPy

You can start the program by typing

    python3 -m gtrpy.run

in the terminal.

## Welcome Page and Choosing # of Dimensions

After you start the program, the first page will look like this:

![greetings](https://user-images.githubusercontent.com/45866787/213306039-51dd652a-d99e-41b5-9ca9-6fe6a4f7aa35.png)

From there, you can choose a suitable dimension. If you choose *three dimensions*, you'll see a page in this form:

![3d-main](https://user-images.githubusercontent.com/45866787/215293214-763a46a9-5e25-42ff-acb3-3dbc51e3f9bb.png)

and in *four dimensions*:

![4d-main](https://user-images.githubusercontent.com/45866787/215288897-5f1e528d-539e-4237-b200-f126d9618037.png)

## GTRPy in 4D

In this guide, let us focus on the 4D case as an example.

### Defining the Coordinate System

In GTRPy, you can define the coordinate system yourself. While doing so, you can choose from the given coordinate system symbols

    t, x, y, z, r, v, r, theta, phi, rho, sigma, psi, eta, tau, xi, T, X

or you can simply choose one of the *predefined coordinate systems*. Currently predefined coordinates in 3D are:

1. Cartesian Coordinates
2. Cylindrical Coordinates
3. Spherical Coordinates

and in 4D:

1. Cartesian Coordinates
2. Cylindrical Coordinates
3. Spherical Coordinates
4. Conform-Compactified Coordinates
5. Rindler Coordinates
6. Schwarzschild Coordinates
7. Eddington-Finkelstein Coordinates

After choosing the coordinate system, just click on the **Change Coordinate System** button to activate the transformation.

> See `demos/demo_6.md` to learn how to add more coordinate system symbols

### Defining the Metric Tensor

To define the metric tensor, just fill the fields in the **Metric Tensor** frame. In this guide, let us study the *Schwarzschild Coordinate System* as an example.

![sch](https://user-images.githubusercontent.com/45866787/213306169-1fa3f7fd-20ee-408f-b840-9ad27f26a495.png)

> See `demos/demo_1.md` for more information about how to define/type math variables in GTRPy.

### GTR Tensors

As we can see, there are many different tensors that we can calculate in GTRPy. Let us calculate the *Christoffel Symbol* as an example.

First click on the **Christoffel Symbol** button to start the calculation.

![chris](https://user-images.githubusercontent.com/45866787/215287954-af722d40-3d3f-44e9-9fcb-8232becabe4c.png)

Later on, you can change the type of the *Christoffel Symbol* and/or get any component from the given page

![chris_up](https://user-images.githubusercontent.com/45866787/215287959-cc4fb77c-43d4-4671-b3b4-2220e806ab9e.png)

If you click on the **Get LaTeX** button, the program will produce the LaTeX equation of the *Christoffel Symbol* and save it under the `logs` directory.

## Fields

If you click on the **Fields** tab you'll see 6 different type of fields

![fields-tab](https://user-images.githubusercontent.com/45866787/215289114-da348b6b-2fd3-4c2d-aeea-11ff3d6d648a.png)

From there, you can pick one of them and perform any available operation. As an example, let us study *Type (1,0) Vector Field*, under the *Schwarzschild Coordinate System*.

First, let us create a random vector field:

![random vector-field](https://user-images.githubusercontent.com/45866787/215289322-482a05b8-92c9-4531-a7e3-e56745866799.png)

By clicking on the **Calculate** button under the **Vary Type** frame, you can easily change the type of the vector field and obtain the LaTeX equation.

![vary-type](https://user-images.githubusercontent.com/45866787/215289327-ea31e0a3-52cc-4ee1-89f3-7ad0469e708c.png)

Later on you can calculate the *Covariant derivative* for any component

![cov-2](https://user-images.githubusercontent.com/45866787/215289347-ab72ac84-ed88-4ed1-89dd-fb8bf076abbe.png)

or by providing the *X* vector field, you can calculate the *Lie Derivative*

![X-vector](https://user-images.githubusercontent.com/45866787/215289383-a2f208f6-8059-49fa-ab51-248b83add299.png)

![lie-derivative](https://user-images.githubusercontent.com/45866787/215289391-0fcda443-30fd-42d2-8e99-3860d3ff562e.png)

and finally you can check if the given vector field is *Killing Field* or not

![killing-field](https://user-images.githubusercontent.com/45866787/215289404-bd8919a5-044b-42ee-974f-cd5c17d0e905.png)
