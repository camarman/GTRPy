# User Guide

You can run the program by simply typing

    python3 grpy.py

![greetings](https://user-images.githubusercontent.com/45866787/212770215-87e7f60e-54cd-4dcd-b625-31a13ab2ded0.png)

Later on choose a suitable dimension from the GUI. If you choose four dimensions, you'll see a page in this form

![4d_main](https://user-images.githubusercontent.com/45866787/212770239-3229dd1f-2ba9-4549-a230-7682a702127f.png)

similarly, for three dimensions

![3d_main](https://user-images.githubusercontent.com/45866787/212770264-54d0455c-54b9-4a07-ba9b-fe1cd6e3efa9.png)

Later on you can define the coordinate system and create your own metric tensor. While defining the coordinate system you can choose from the given coordinate system symbols

    t, x, y, z, r, v, r, theta, phi, rho, sigma, psi, eta, tau, xi, T, X

Or you can simply choose one of the predefined coordinate systems. Currently predefined coordinates in 4D are:

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

> For more detailed usage with examples, take a look at the `demos` directory.

## Tensors, Tensor Types, Index Lowering and Raising

Let us study the Schwarzschild Coordinates as an example.

![sch](https://user-images.githubusercontent.com/45866787/212770513-d3462d10-504e-44fd-88dd-746dc4a847a1.png)

Just click one of the tensor buttons, which will lead you to the default page of the choosen tensor.

![chris](https://user-images.githubusercontent.com/45866787/212770634-f5c2c0b1-3da1-45ea-8358-6c4f0686ca31.png)

Later on, you can change the type of the tensor and get any component from the given page.

![chris_up](https://user-images.githubusercontent.com/45866787/212770640-f51587e7-ad06-487b-89a1-03edf70209bd.png)

## Fields

If you click on the Fields tab you'll see the 6 available fields.

![fields_tab](https://user-images.githubusercontent.com/45866787/212770355-8acf8252-ba73-43c0-9de8-5e81e2495cd7.png)

From there, you can pick the field that you want to calculate. After typing your field, you can perform any available operation.

![4d_scalar](https://user-images.githubusercontent.com/45866787/212770367-d406ed7b-8e1d-43b1-b6fd-61ec167b15a1.png)

![4d_vector](https://user-images.githubusercontent.com/45866787/212770377-e4cb3a62-87de-4ca3-85f7-4a6afb69ac8c.png)

![4d_tensor](https://user-images.githubusercontent.com/45866787/212770390-8cff92d8-5db4-4b7b-8965-5a5ef5ac20a1.png)
