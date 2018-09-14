"""
    This file generates the 1D mesh and the 4 cell
    state variables needed for the model (including Diffusivity).

    **It may be that Diffusivity should be declared as a FaceVariable.
    It must be adjusted to the correct size when using it to calculate
    different values.**
"""

from fipy import Grid1D, CellVariable
from fipy.tools import numerix, dump

from parameters import *


# ----------------- Mesh Generation -----------------------
mesh = Grid1D(nx=config.nx, Lx=L)

x = mesh.cellCenters[0]  # Cell position
X = mesh.faceCenters[0]  # Face position, if needed


# -------------- State Variable Declarations --------------
density = CellVariable(name=r"$n$", mesh=mesh, hasOld=True)

temperature = CellVariable(name=r"$T$", mesh=mesh, hasOld=True)

U = CellVariable(name=r"$U$", mesh=mesh, hasOld=True)

Z = CellVariable(name=r"$Z$", mesh=mesh, hasOld=True)

Diffusivity = CellVariable(name=r"$D$", mesh=mesh, hasOld=True)

U.setValue(density*temperature / (gamma - 1.0))


# -------------- Other Variable Declarations --------------
# Thermal velocities (most probable)
v_Ti = CellVariable(name=r"$v_{th,i}$", mesh=mesh)
v_Te = CellVariable(name=r"$v_{th,e}$", mesh=mesh)

# Neutrals density in use for CX friction
n_0 = CellVariable(name=r"$n_0$", mesh=mesh)

# Poloidal gyro-(Larmor) radii
rho_pi = CellVariable(name=r"$\rho_{\theta i}$", mesh=mesh)
rho_pe = CellVariable(name=r"$\rho_{\theta e}$", mesh=mesh)

# Banana orbit bounce frequencies
omega_bi = CellVariable(name=r"$\omega_{bi}$", mesh=mesh)
omega_be = CellVariable(name=r"$\omega_{be}$", mesh=mesh)

# Banana width
w_bi = CellVariable(name=r"$w_{bi}$", mesh=mesh)

# Transit frequency
omega_t = CellVariable(name=r"$\omega_t$", mesh=mesh)

# Collision Frequencies
nu_ei = CellVariable(name=r"$\nu_{ei}$", mesh=mesh)
nu_ii = CellVariable(name=r"$\nu_{ii}$", mesh=mesh)

# Collisionalities
nu_ai = CellVariable(name=r"$\nu_{*i}$", mesh=mesh)
nu_ae = CellVariable(name=r"$\nu_{*e}$", mesh=mesh)

# Electron Anomalous Diffusion
D_an = CellVariable(name=r"$D_{an}$", mesh=mesh)
g_n_an = CellVariable(name=r"$g_n^{an}$", mesh=mesh)
g_T_an = CellVariable(name=r"$g_T^{an}$", mesh=mesh)
g_Z_an = CellVariable(name=r"$g_Z^{an}$", mesh=mesh)
Gamma_an = CellVariable(name=r"$\Gamma_e^{an}$", mesh=mesh)

# Charge Exchange Friction
ionization_rate = CellVariable(name=r"$\langle\sigma_{ion} v\rangle$",
                               mesh=mesh)
cx_rate = CellVariable(name=r"$\langle\sigma_{cx} v\rangle$",
                       mesh=mesh)
g_n_cx = CellVariable(name=r"$g_n^{cx}$", mesh=mesh)
g_T_cx = CellVariable(name=r"$g_T^{cx}$", mesh=mesh)
g_Z_cx = CellVariable(name=r"$g_Z^{cx}$", mesh=mesh)
Gamma_cx = CellVariable(name=r"$\Gamma_i^{cx}$", mesh=mesh)

# Ion Bulk (Parallel) Viscosity
plasma_disp = CellVariable(name=r"$X$", mesh=mesh)
D_bulk = CellVariable(name=r"$D_{\pi\parallel}$", mesh=mesh)
Gamma_bulk = CellVariable(name=r"$\Gamma_i^{\pi\parallel}$", mesh=mesh)

# Ion Orbit Loss
g_ol = CellVariable(name=r"$g^{ol}$", mesh=mesh)
Gamma_ol = CellVariable(name=r"$\Gamma_i^{ol}$", mesh=mesh)


variable_dictionary = {
        'x': x, 'density': density, 'temperature': temperature, 'Z': Z,
        'Diffusivity': Diffusivity, 'n_0': n_0, 'v_Ti': v_Ti, 'v_Te': v_Te,
        'rho_pi': rho_pi, 'rho_pe': rho_pe, 'omega_bi': omega_bi,
        'omega_be': omega_be, 'w_bi': w_bi, 'omega_t': omega_t, 'nu_ei': nu_ei,
        'nu_ii': nu_ii, 'nu_ai': nu_ai, 'nu_ae': nu_ae,
        'ionization_rate': ionization_rate, 'cx_rate': cx_rate,
        'D_an': D_an, 'g_n_an': g_n_an, 'g_T_an': g_T_an, 'g_Z_an': g_Z_an,
        'Gamma_an': Gamma_an, 'g_n_cx': g_n_cx, 'g_T_cx': g_T_cx,
        'g_Z_cx': g_Z_cx, 'Gamma_cx': Gamma_cx, 'g_ol': g_ol,
        'Gamma_ol': Gamma_ol, 'D_bulk': D_bulk, 'Gamma_bulk': Gamma_bulk,
        'plasma_disp': plasma_disp
    }


# Remove entire entry in aux plot details arrays if aux_vars is not a string
k = 0
while k < len(config.aux_vars) and config.aux_plots is True:
    if config.aux_vars[k] in variable_dictionary:
        k = k + 1
    elif config.aux_vars[k] not in variable_dictionary:
        del config.aux_vars[k]
        del config.aux_titles[k]
        del config.aux_ymin[k]
        del config.aux_ymax[k]

del k  # Cleanup


# Auxiliary function to print out any variable
def print_variables(*args):
    for v in args:
        print "\n--------------------\t" + str(v.name) + \
              "\t--------------------"
        print v.inBaseUnits()
