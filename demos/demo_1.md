# Demo 1

In this demo, we will explore the usage of the LaTeX in the GTRPy. By following this tutorial, you'll learn how to perform basic mathematical operations and define variables.

## Mathematical Operations and Greek Letters

In GRTPy, the metric tensor and field components can be written by using LaTeX rules. For instance, if you want to write

$$
\alpha^2(r_s)^3(sin^2(\theta))
$$

you can directly write it as

    alpha^2*r_s^3*sin(theta)^2

and the `sympy` will interpret it as it is. In exponential expressions, you can both use `^` and `**`. You can also write `log` as usual, such as `log(10)` etc. For instance, if you want to write

$$
\log(10)r_s^2\psi^{\eta}
$$

you can directly write it as

    log(10)^2*r_s^2*psi^(eta)

As you can see most of the greek alphabet will be converted to its corresponding LaTeX form. Here is the list of them and corresponding results in GTRPy.

$$
{\rm alpha} - \alpha \\
$$

$$
{\rm delta} - \delta \\
$$

$$
{\rm epsilon} - \epsilon \\
$$

$$
{\rm theta} -\theta \\
$$

$$
{\rm iota} - \iota \\
$$

$$
{\rm kappa} - \kappa \\
$$

$$
{\rm lamda} - \lambda \\
$$

$$
{\rm mu} - \mu \\
$$

$$
{\rm nu} - \nu \\
$$

$$
{\rm xi} - \xi \\
$$

$$
{\rm omicron} - \omicron \\
$$

$$
{\rm pi} - \pi \\
$$

$$
{\rm rho} - \rho \\
$$

$$
{\rm sigma} - \sigma \\
$$

$$
{\rm tau} - \tau \\
$$

$$
{\rm upsilon} - \upsilon \\
$$

$$
{\rm phi} - \phi \\
$$

$$
{\rm chi} - \chi \\
$$

$$
{\rm psi} - \psi \\
$$

$$
{\rm omega} - \omega \\
$$

> Note 1: For some reason, `beta` and `gamma` letters do not work in GTRPy. If your calculations involve those letters, please convert them to another letter.
>
> Note 2: You do not need to put `\` in front of the greek letters in GTRPy, as it's done in the LaTeX.
