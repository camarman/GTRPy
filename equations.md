# Equations

This is the list of the all equations used in the program. Now, you can easily compare the written equations with the code (under the `objects` directory).

> Fields will be added soon!

## Metric Tensor

$$
g_{ij}={\rm diag}(-1, 1, r^2, r^2sin^2(\theta))
$$

$$
g_{ij}g^{jk} = g^{k}_{~~i}
$$

$$
g^{k}_{~~i}g^{il} = g^{kl}
$$

## Christoffel Symbol

$$
    \Gamma^{k}_{~~ij} = \frac{1}{2}g^{kl}(g_{li,j}+g_{lj,i}-g_{ij,l})
$$

$$
    \Gamma^{k}_{~~ij}g_{kl} = \Gamma_{ijl}
$$

$$
    \Gamma^{k}_{~~ij}g^{il} = \Gamma^{kl}_{~~~j}
$$

$$
    \Gamma^{kl}_{~~~j}g^{jm} = \Gamma^{klm}
$$

## Riemann Tensor

$$
    R^l_{~ijk} = \Gamma^{l}_{~ik,j} - \Gamma^{l}_{~ij,k} + \Gamma^{l}_{~mj}\Gamma^{m}_{~ik} - \Gamma^{l}_{~mk}\Gamma^{m}_{~ij}
$$

$$
    R^l_{~ijk}g_{lm} = R_{ijkm}
$$

$$
    R^l_{~ijk}g^{im} = R^{lm}_{~~~~jk}
$$

$$
    R^{lm}_{~~~~jk}g^{jn} = R^{lmn}_{~~~~~~~k}
$$

$$
    R^{lmn}_{~~~~~~~k}g^{kp} = R^{lmnp}
$$

## Weyl Tensor

$$
    C_{ijkl} = R_{ijkl} + \frac{1}{n-2}(g_{il}R_{kj}+g_{jk}R_{li}-g_{ik}R_{lj}-g_{jl}R_{ki}) + \frac{1}{(n-1)(n-2)}(g_{ik}g_{lj}-g_{il}g_{kj})R
$$

$$
C_{ijkl}g^{im} = C^{m}_{~~~jkl}
$$

$$
C^{m}_{~~~jkl}g^{jn} = C^{mn}_{~~~~~~kl}
$$

$$
C^{mn}_{~~~~~~kl}g^{kp} = C^{mnp}_{~~~~~~~~l}
$$

$$
C^{mnp}_{~~~~~~~~l}g^{lr} = C^{mnpr}
$$

## Ricci Tensor

$$
R_{ij} = R^{k}_{~~ikj}
$$

$$
R_{ij}g^{jk} = R^{k}_{~~i}
$$

$$
R^{k}_{~~i}g^{il} = R^{kl}
$$

## Traceless Ricci tensor

$$
Z_{ij} = R_{ij} - \frac{1}{n}g_{ij}R
$$

$$
Z_{ij}g^{jk} = Z^{k}_{~~i}
$$

$$
Z^{k}_{~~i}g^{il} = Z^{kl}
$$

## Ricci Scalar

$$
R = g^{ij}R_{ij}
$$

## Einstein Tensor

$$
G_{ij} = R_{ij} - \frac{1}{2}g_{ij}R
$$

$$
G_{ij}g^{jk} = G^{k}_{~~i}
$$

$$
G^{k}_{~~i}g^{il} = G^{kl}
$$

## Kretschmann Scalar

$$
K = R_{ijkl}R^{ijkl}
$$
