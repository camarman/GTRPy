# User Guide

You can run the program by simply typing

    python3 grpy.py

![greetings](https://user-images.githubusercontent.com/45866787/212614821-2523d6c3-cd96-4b38-adbd-c406cf5708b9.png)

Later on choose a suitable dimension from the GUI. If you choose four dimensions, you'll see a page in this form

![4d_main](https://user-images.githubusercontent.com/45866787/212614841-2d541989-f21c-4de6-820b-ca7ee08b75c6.png)

similarly, for three dimensions

![3d_main](https://user-images.githubusercontent.com/45866787/212614862-2424dd1c-7f4f-409a-9bf4-8153002b460d.png)

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

![4d_sch](https://user-images.githubusercontent.com/45866787/212614878-170f3623-0802-4a33-9b7d-475c473c82d5.png)

Just click one of the tensor buttons, which will lead you to the default page of the choosen tensor.

![chris](https://user-images.githubusercontent.com/45866787/212614905-cab05894-1c04-407f-9edd-4da4ae06d4d4.png)

Later on, you can change the type of the tensor and get any component from the given page.

![chris_upper](https://user-images.githubusercontent.com/45866787/212614942-277dc99c-6978-4814-9f28-7b2e3cabf832.png)

## Fields

If you click on the Fields tab you'll see the 6 available fields.

![4d_field](https://user-images.githubusercontent.com/45866787/212614966-59cc5614-d454-47b0-89c7-0b3738c620d1.png)

From there, you can pick the field that you want to calculate. After typing your field, you can perform any available operation.

![scalar_field](https://user-images.githubusercontent.com/45866787/212466315-315a6269-d84f-4bd3-92a1-e0d64e21742e.png)

![vector_field](https://user-images.githubusercontent.com/45866787/212466320-5d5e31a0-8c1d-49d6-a928-f844c7cf04c1.png)

![tensor_field](https://user-images.githubusercontent.com/45866787/212466322-8f25f5a5-8345-4b71-98ef-721c7eaa0c92.png)
