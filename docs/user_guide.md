# User Guide

To run the program type

    python3 grtc_gui.py

![greeting_page](https://user-images.githubusercontent.com/45866787/198973226-3cb1b794-15ca-4926-9b5f-55743dac78bd.png)

Later on choose a suitable dimension from the GUI. If you choose four dimensions, you'll see a page in this form

![4d](https://user-images.githubusercontent.com/45866787/198973300-ac36cd0f-1b01-4530-80c3-7c6d0da3ccf8.png)

similarly, for three dimensions

![3d](https://user-images.githubusercontent.com/45866787/198973467-1391e0ba-be1f-438c-a5bf-40a4d7494978.png)

Later on you can define the coordinate system and create your own metric tensor. While defining the coordinate system you can choose from the given coordinate system symbols

    t, x, y, z, r, v, r, theta, phi, rho, sigma, psi, eta, tau, xi, T, X

Or you can simply choose one of the predefined coordinate systems. Currently predefined coordinates in 4D are;

    1) Cartesian Coordinates
    2) Cylindrical Coordinates
    3) Spherical Coordinates
    4) Conform-Compactified Coordinates
    5) Rindler Coordinates
    6) Schwarzschild Coordinates
    7) Eddington-Finkelstein Coordinates

and in 3D;

    1) Cartesian Coordinates
    2) Cylindrical Coordinates
    3) Spherical Coordinates

Let us study the Schwarzschild Coordinates as an example.

> For more detailed usage with examples, take a look at the `demos` directory.

## Tensors, Tensor Types, Index Lowering and Raising

Just click one of the tensor buttons, which will lead you to the default page of the choosen tensor.

![chris_1](https://user-images.githubusercontent.com/45866787/198973666-7b8e5607-0591-449a-8244-cdcac9bbca58.png)

Later on, you can change the type of the tensor and get any component from the given page.

![chris_2](https://user-images.githubusercontent.com/45866787/198973890-22bed6aa-c5fa-4238-89bb-72a29ea82e85.png)

## Fields

If you click on the Fields tab you'll see the 6 available fields.

![fields_tab](https://user-images.githubusercontent.com/45866787/198974014-29cd448d-9a8c-4c3c-ae4e-1de98e862a86.png)

From there, you can pick the field that you want to calculate. After typing your field, you can perform any available operation.

![scalar](https://user-images.githubusercontent.com/45866787/198974191-763724b2-22cb-4196-b39e-87b52f509f52.png)

![vector](https://user-images.githubusercontent.com/45866787/200797025-53bd0b2f-eed2-435a-a05c-9722f153579b.png)

![tensor](https://user-images.githubusercontent.com/45866787/198974166-7b9e7941-582f-485b-911a-1b7a8a01194e.png)
