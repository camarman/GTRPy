# User Guide

You can run the program by simply typing

    python3 grtc_gui.py

in the terminal from the grtc_gui directory

![greetings_page](https://user-images.githubusercontent.com/45866787/212466253-fb0e42e4-dc88-4550-bf19-b901b5008a25.png)

Later on choose a suitable dimension from the GUI. If you choose four dimensions, you'll see a page in this form

![4d_main_grt](https://user-images.githubusercontent.com/45866787/212466258-6e10713a-6235-45a0-babe-010e1f0444be.png)

similarly, for three dimensions

![3d_main](https://user-images.githubusercontent.com/45866787/212466276-ced0e2eb-ce5e-4f3a-966a-f5f286252e72.png)

Later on you can define the coordinate system and create your own metric tensor. While defining the coordinate system you can choose from the given coordinate system symbols

    t, x, y, z, r, v, r, theta, phi, rho, sigma, psi, eta, tau, xi, T, X

Or you can simply choose one of the predefined coordinate systems. Currently predefined coordinates in 4D are;

    1. Cartesian Coordinates
    2. Cylindrical Coordinates
    3. Spherical Coordinates
    4. Conform-Compactified Coordinates
    5. Rindler Coordinates
    6. Schwarzschild Coordinates
    7. Eddington-Finkelstein Coordinates

and in 3D;

    1. Cartesian Coordinates
    2. Cylindrical Coordinates
    3. Spherical Coordinates


> For more detailed usage with examples, take a look at the `demos` directory.

## Tensors, Tensor Types, Index Lowering and Raising

Let us study the Schwarzschild Coordinates as an example.

![4d_sch](https://user-images.githubusercontent.com/45866787/212466334-b20ba860-9463-4bba-91de-5ee8e1898e53.png)

Just click one of the tensor buttons, which will lead you to the default page of the choosen tensor.

![chris_def](https://user-images.githubusercontent.com/45866787/212466296-99805e6a-92b7-47d0-a21d-602cbdb75dce.png)

Later on, you can change the type of the tensor and get any component from the given page.

![chris_upper](https://user-images.githubusercontent.com/45866787/212466303-581df35a-3b44-4349-92f1-a02ed282f57b.png)

## Fields

If you click on the Fields tab you'll see the 6 available fields.

![4d_main_fields](https://user-images.githubusercontent.com/45866787/212466308-024668ae-c44b-46d5-a488-96efe8437e23.png)

From there, you can pick the field that you want to calculate. After typing your field, you can perform any available operation.

![scalar_field](https://user-images.githubusercontent.com/45866787/212466315-315a6269-d84f-4bd3-92a1-e0d64e21742e.png)

![vector_field](https://user-images.githubusercontent.com/45866787/212466320-5d5e31a0-8c1d-49d6-a928-f844c7cf04c1.png)

![tensor_field](https://user-images.githubusercontent.com/45866787/212466322-8f25f5a5-8345-4b71-98ef-721c7eaa0c92.png)


