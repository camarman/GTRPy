## General-Relativity-Tensorial-Calculations (GRTC) by Graphical User Interface (GUI)

> ## Current Features
>
> #### 1. Calculating the Inverse Metric Tensor, Christoffel Symbol, Riemann Tensor, Ricci Tensor, Ricci Scalar, Weyl Tensor, Traceless Ricci Tensor, Einstein Tensor and, Kretschmann Scalar from a given metric and coordinate system (available in 3D and 4D).
>
> #### 2. Calculating [covariant derivative](https://en.wikipedia.org/wiki/Covariant_derivative#Covariant_derivative_by_field_type) for a given scalar, vector, and tensor fields (available in 3D and 4D).


> ## Upcoming Features
> 
> #### 1. [Lie Derivative Calculator](https://en.wikipedia.org/wiki/Lie_derivative) Calculator
>
> #### 2. [Hawking Radiation Calculator](https://www.vttoth.com/CMS/physics-notes/311-hawking-radiation-calculator)
>
> #### 3. Calculating [Unruh temperature](https://en.wikipedia.org/wiki/Unruh_effect#Temperature_equation)
>
> #### 4. Checking if a vector field X is a killing field
>
> #### 5. Displaying killing vector equations for a given metric tensor
>
> #### 6. Displaying Geodesic Equations
>
> #### 7. Raising and lowering indices of a given tensor


#### Requirements
1. `IPython.display`, `itertools`, `numpy`, `PIL`, `PySimpleGUI`, `sympy`
2. [`Latex`](https://www.latex-project.org/get/) (To produce images and equations)
3. You'll also need three fonts; `Tahoma`, `Bookman`, and `Georgia`(These are the standard fonts for Windows, but if they are missing, you can download them online or change the font manually from the `GRTC_GUI.py`.

### Getting Started

#### 1. Run the `GRTC_GUI.py` file
#### 2. Choose a suitable dimension from the given page 

You'll have two options

![main_page](https://user-images.githubusercontent.com/45866787/123518687-b1783c80-d6af-11eb-898d-09d40c5369cf.png)

If you choose four dimensions, you'll see a page in this form

![4d](https://user-images.githubusercontent.com/45866787/123513907-7cacbb00-d698-11eb-94d9-0c639209287d.png)

similarly, for three dimensions

![3d](https://user-images.githubusercontent.com/45866787/123635659-97139f80-d824-11eb-936f-87297f51bc46.png)

#### 3. Define the coordinate system (cartesian, spherical, etc.)

![coord_sys](https://user-images.githubusercontent.com/45866787/123513964-c695a100-d698-11eb-905f-e9473cfad125.png)

These are the available/most commonly used coordinate system components. If you want to add another element, go to line `52-53` located in the `GRTC_GUI.py`.

![coordinates](https://user-images.githubusercontent.com/45866787/123514068-694e1f80-d699-11eb-8b16-3d4840b1d0b8.png)

#### 4. Define the diagonal components of the metric tensor

Here is an example 

![diag](https://user-images.githubusercontent.com/45866787/123517480-dff31900-d6a9-11eb-9616-828eed6c8896.png)

## Tensors, Tensor Types, and Index Lowering/Raising

Choose a tensor from the `Tensors` segment and click `Submit`. For instance, when you choose the `Metric Tensor`, you'll see a page like this.

![metric_tensor](https://user-images.githubusercontent.com/45866787/123517493-f8fbca00-d6a9-11eb-9e3b-71780a4b7eac.png)

Later on, you can choose the `Christoffel Symbol` (or any other available tensor) from the `Tensors` segment.

![chris_symbol](https://user-images.githubusercontent.com/45866787/123517511-1335a800-d6aa-11eb-9caa-98dcd5124a57.png)

You can change the type of the tensor

![chris_new](https://user-images.githubusercontent.com/45866787/123637827-1e621280-d827-11eb-90dd-3695fab8168f.png)

and get any component from the given page.

![chris_symbol2](https://user-images.githubusercontent.com/45866787/123517576-6c054080-d6aa-11eb-8ef1-e6ddd69def96.png)

## Covariant Derivative by Field Type

There are 6 different options that you can choose to calculate the covariant derivative of a field. These are;

1. `Scalar Field` 
2. `Type (1,0) Vector Field` 
3. `Type (0,1) Vector Field`
4. `Type (2,0) Tensor Field`
5. `Type (1,1) Tensor Field`
6. `Type (0,2) Tensor Field`

### Scalar Fields

When you choose `Scalar Field` from the main page, you'll see a page in this form

![scalar_field](https://user-images.githubusercontent.com/45866787/123519081-d5d51880-d6b1-11eb-887a-7ffbf18f4479.png)

From here, you can form a scalar field and choose the covariant derivative component that you want to calculate. 

![scalar_field1](https://user-images.githubusercontent.com/45866787/123519090-e5ecf800-d6b1-11eb-93c0-e624d7f9d61f.png)

For this type of field, we obtain

![scalar](https://user-images.githubusercontent.com/45866787/123640662-10fa5780-d82a-11eb-8bdd-8e4ea056b132.png)


### Vector Fields

For example, when you choose `Type (1,0) Vector Field`, you'll see a page in this form

![cov_der](https://user-images.githubusercontent.com/45866787/123517695-22692580-d6ab-11eb-9946-88bb2629c34a.png)

From here, you can form a vector field and choose the covariant derivative component that you want to calculate. Such as for

![cov_der](https://user-images.githubusercontent.com/45866787/123517744-62300d00-d6ab-11eb-8a6f-958dbb8f3277.png)

You'll obtain

![cov_der_result](https://user-images.githubusercontent.com/45866787/123517767-84298f80-d6ab-11eb-8064-8e50acc98552.png)

### Tensor Fields

For example, when you choose `Type (0,2) Tensor Field` you'll see a page in this form

![type02_tensor](https://user-images.githubusercontent.com/45866787/123518927-edf86800-d6b0-11eb-9aff-9692468f839c.png)

From here, you can form a tensor field and choose the covariant derivative component that you want to calculate. 

![tensor02](https://user-images.githubusercontent.com/45866787/123519232-a96dcc00-d6b2-11eb-84f5-8ae9209bb045.png)

For this type of field, we obtain

![tensor02_result](https://user-images.githubusercontent.com/45866787/123519235-abd02600-d6b2-11eb-8829-3093b485c073.png)

## Non - GUI Version

Those who want to run the code from the `.ipynb` file, and don't want to use GUI, can follow the steps given in the `example.ipynb`.
