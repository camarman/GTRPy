# User Guide

You can run the program by simply typing

    python3 -m gtrpy.run

from the terminal

![greetings](https://user-images.githubusercontent.com/45866787/213306039-51dd652a-d99e-41b5-9ca9-6fe6a4f7aa35.png)

Later on choose a suitable dimension from the GUI. If you choose four dimensions, you'll see a page in this form

![4d_main](https://user-images.githubusercontent.com/45866787/213306076-9153466c-6aeb-4776-9208-10c953a80e4a.png)

similarly, for three dimensions

![3d_main](https://user-images.githubusercontent.com/45866787/213306145-6212f979-c4fc-45c1-8bf4-d2d4ecf96758.png)

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

Let us study the **Schwarzschild Coordinate System** as an example.

![sch](https://user-images.githubusercontent.com/45866787/213306169-1fa3f7fd-20ee-408f-b840-9ad27f26a495.png)

Just click one of the tensor buttons, which will lead you to the default page of the choosen tensor.

![chris](https://user-images.githubusercontent.com/45866787/213306212-08e35f80-14ea-48fc-8600-a940de20cb89.png)

Later on, you can change the type of the tensor and get any component from the given page.

![chris_up](https://user-images.githubusercontent.com/45866787/213306230-b9501d32-92a7-4129-8a87-a1b0ed366c05.png)

## Fields

If you click on the Fields tab you'll see the 6 available fields.

![fields_tab](https://user-images.githubusercontent.com/45866787/213306249-d90a9635-e07a-42db-8098-6a3d24000986.png)

From there, you can pick the field that you want to calculate. After typing your field, you can perform any available operation.

![4d_scalar](https://user-images.githubusercontent.com/45866787/212770367-d406ed7b-8e1d-43b1-b6fd-61ec167b15a1.png)

![4d_vector](https://user-images.githubusercontent.com/45866787/212770377-e4cb3a62-87de-4ca3-85f7-4a6afb69ac8c.png)

![4d_tensor](https://user-images.githubusercontent.com/45866787/212770390-8cff92d8-5db4-4b7b-8965-5a5ef5ac20a1.png)
