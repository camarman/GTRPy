# Equations

This is the list of the all equations used by the GTRPy.

## Tensors

### Metric Tensor

$$
g^{k}_{~~i} = g_{ij}g^{jk}
$$

$$
g^{kl} = g^{k}_{~~i}g^{il}
$$

### Christoffel Symbol

$$
    \Gamma^{k}_{~~ij} := \frac{1}{2}g^{kl}(g_{li,j}+g_{lj,i}-g_{ij,l})
$$

$$
    \Gamma_{ijl} = \Gamma^{k}_{~~ij}g_{kl}
$$

$$
    \Gamma^{kl}_{~~~j}=\Gamma^{k}_{~~ij}g^{il}
$$

$$
    \Gamma^{klm} = \Gamma^{kl}_{~~~j}g^{jm}
$$

### Riemann Tensor

$$
    R^l_{~ijk} := \Gamma^{l}_{~ik,j} - \Gamma^{l}_{~ij,k} + \Gamma^{l}_{~mj}\Gamma^{m}_{~ik} - \Gamma^{l}_{~mk}\Gamma^{m}_{~ij}
$$

$$
    R_{ijkm}=R^l_{~ijk}g_{lm}
$$

$$
    R^{lm}_{~~~~jk}=R^l_{~ijk}g^{im}
$$

$$
    R^{lmn}_{~~~~~~~k}=R^{lm}_{~~~~jk}g^{jn}
$$

$$
    R^{lmnp}=R^{lmn}_{~~~~~~~k}g^{kp}
$$

### Weyl Tensor

$$
    C_{ijkl} := R_{ijkl} + \frac{1}{n-2}(g_{il}R_{kj}+g_{jk}R_{li}-g_{ik}R_{lj}-g_{jl}R_{ki}) + \frac{1}{(n-1)(n-2)}(g_{ik}g_{lj}-g_{il}g_{kj})R
$$

$$
C^{m}_{~~~jkl} = C_{ijkl}g^{im}
$$

$$
C^{mn}_{~~~~~~kl} = C^{m}_{~~~jkl}g^{jn}
$$

$$
C^{mnp}_{~~~~~~~~l} = C^{mn}_{~~~~~~kl}g^{kp}
$$

$$
C^{mnpr} = C^{mnp}_{~~~~~~~~l}g^{lr}
$$

### Ricci Tensor

$$
R_{ij} := R^{k}_{~~ikj}
$$

$$
R^{k}_{~~i} = R_{ij}g^{jk}
$$

$$
R^{kl} = R^{k}_{~~i}g^{il}
$$

### Traceless Ricci tensor

$$
Z_{ij} := R_{ij} - \frac{1}{n}g_{ij}R
$$

$$
Z^{k}_{~~i} = Z_{ij}g^{jk}
$$

$$
Z^{kl} = Z^{k}_{~~i}g^{il}
$$

### Ricci Scalar

$$
R := g^{ij}R_{ij}
$$

### Einstein Tensor

$$
G_{ij} := R_{ij} - \frac{1}{2}g_{ij}R
$$

$$
G^{k}_{~~i} = G_{ij}g^{jk}
$$

$$
G^{kl} = G^{k}_{~~i}g^{il}
$$

### Kretschmann Scalar

$$
K := R_{ijkl}R^{ijkl}
$$

## Fields

### Scalar Field

$$
\nabla_i \phi := \partial_i\phi
$$

$$
L_i\phi := X^i\partial_i\phi
$$

### Vector Field

$$
\nabla_kV^i := \partial_kV^i + \Gamma^i_{~~jk}V^j
$$

$$
\nabla_kV_i := \partial_kV_i - \Gamma^{j}_{~~ik}V_j
$$

$$
\mathcal{L}_XV^i := X^j\partial_jV^i - V^j\partial_jX^i
$$

$$
\mathcal{L}_XV_i := X^j\partial_jV_i + V_j\partial_iX^j
$$

$$
V_j = V^ig_{ij}
$$

$$
V^j = V_ig^{ij}
$$

$$
\mathcal{L}_Vg = 0
$$

> Note: Type (0,1) vector field is converted to type (1,0) during the calculation of the Killing field condition.

### Tensor Field

$$
\nabla_{k}T^{ij} := T^{ij}_{~~,k}+T^{lj}\Gamma^{i}_{~~lk}+T^{il}\Gamma^{j}_{~~lk}
$$

$$
\nabla_{k}T^{i}_{~j} := T^{i}_{~j,k}+T^{l}_{~j}\Gamma^{i}_{~~lk}-T^{i}_{~l}\Gamma^{l}_{~~jk}
$$

$$
\nabla_{k}T_{ij} := T_{ij,k}-T_{lj}\Gamma^{l}_{~~ik}-T_{il}\Gamma^{l}_{~~jk}
$$

$$
\mathcal{L}_XT^{ij} := X^{k}\partial_kT^{ij}-T^{ik}\partial_{k}X^j-T^{kj}\partial_kX^i
$$

$$
\mathcal{L}_XT^{i}_{~~j} := X^k\partial_kT^{i}_{~~j}-T^{k}_{~~j}\partial_kX^i+T^{i}_{~~k}\partial_jX^k
$$

$$
\mathcal{L}_XT_{ij} := X^k\partial_kT_{ij}+T_{kj}\partial_iX^k+T_{ik}\partial_jX^k
$$

#### Varying Type (0,2) Tensor Field

$$
T^{k}_{~~i} = T_{ij}g^{jk}
$$

$$
T^{kl} = T_{ij}g^{jk}g^{il}
$$

#### Varying Type (1,1) Tensor Field

$$
T^{ik} = T^{i}_{~~j}g^{jk}
$$

$$
T_{jk} = T^{i}_{~~j}g_{ik}
$$

#### Varying Type (2,0) Tensor Field

$$
T^{i}_{~~k} = T^{ij}g_{jk}
$$

$$
T_{kl} = T^{ij}g_{jk}g_{il}
$$
