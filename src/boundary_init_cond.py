"""
    Declares the initial conditions, including whether it starts in L-- or
    H--mode. The ones not by Paquay are entire estimated by hand. If one
    changes the size of the domain (L), these potentially may need to be
    recalculated.

    This file also declares the boundary conditions, as a python function.
    The edge boundary for Z may need consideration.
"""

from src.variable_decl import *


# ---------------- Set Initial Conditions -----------------

# THE FOLLOWING ARE ONLY LINEAR PROFILES, estimated by hand.
# ---------------- Taylor-expanded Model ------------------
if config.taylor_model is True:
    # L--mode
    if config.initial_H_mode is False:
        density.setValue(1.5 * x / L + 0.5)        # in AU
        temperature.setValue(x / L + 1.2)
        Z.setValue(0.0)

    # H--mode
    elif config.initial_H_mode is True:
        density.setValue((0.5 / 1.5) * x + 0.5, where=x <= 1.5)
        density.setValue(3.0 * x - 3.5, where=(x > 1.5) & (x < 2.0))
        density.setValue((0.5 / 1.5) * x + (11.0 / 6.0), where=x >= 2.0)

        temperature.setValue((0.2 * x + 1.2), where=x <= 1.5)
        temperature.setValue((1.8 * x - 1.2), where=(x > 1.5) & (x < 2.0))
        temperature.setValue((0.2 * x + 2.0), where=x >= 2.0)

        Z.setValue(-3.0 / (1.0 + numerix.exp(12.0 * (x - 1.75))))


# ----------------- Flux Model ----------------------------
if config.taylor_model is False:
    # L--mode
    if config.initial_H_mode is False:
        density.setValue(((8.0e18 - 3.0e18) / 0.05) * x + 3.0e18)   # in m^-3
        temperature.setValue(((300.0 - 100.0) / 0.05) * x + 100.0)  # in eV!
        Z.setValue(0.0)

    # H--mode
    elif config.initial_H_mode is True:
        density.setValue((1.25e20 * x + 0.05e20), where=x < 0.01)
        density.setValue((7.5e20 * x - 0.0125e20),
                         where=(x > 0.01) & (x < 0.015))
        density.setValue((1.25e20 * x + 0.08125e20), where=x > 0.015)

        temperature.setValue((3.0e3 * x + 100.0), where=x < 0.01)
        temperature.setValue((18.0e3 * x - 50.0),
                             where=(x > 0.01) & (x < 0.015))
        temperature.setValue((3.0e3 * x + 175.0), where=x > 0.015)

        Z.setValue(3.0 / (1.0 + numerix.exp(1.5e3 * (x - 0.015))))


# ----------------- Set Diffusivity Model -----------------
# It defaults to Stap's version
# Itohs'/Zohm's model
if config.D_choice.lower() == "d_zohm" or config.D_choice.lower() == "zohm":
    D_choice_local = (D_max + D_min) / 2.0 \
        + ((D_max - D_min) * numerix.tanh(Z)) / 2.0

# Stap's Model
elif (config.D_choice.lower() == "d_staps" or
        config.D_choice.lower() == "staps"):
    D_choice_local = D_min + (D_max - D_min) \
        / (1.0 + config.alpha_sup * numerix.sign(Z.grad[0])
           * (abs(Z.grad[0]))**config.beta)

# Flow-Shear Model
elif (config.D_choice.lower() == "d_shear" or config.D_choice.lower()
        == "d_flow_shear" or config.D_choice.lower() == "d_flow-shear" or
        config.D_choice.lower() == "flow_shear" or config.D_choice.lower()
        == "flow-shear" or config.D_choice.lower() == "shear"):
    D_choice_local = D_min + (D_max - D_min) / \
        (1.0 + config.shear_a1 * (Z)**2
         + config.shear_a2 * Z * Z.grad[0]
         + config.shear_a3 * numerix.dot(Z.grad, Z.grad))

# Weymiens L--mode
elif (config.D_choice.lower() == "d_weymiens_l" or config.D_choice.lower()
        == "weymiens_l" or config.D_choice.lower() == "weymiens"):
    D_choice_local = D_min + (D_max - D_min) \
        * (1 - config.alpha_sup * numerix.dot(Z.grad, Z.grad))

else:
    print("Something went horribly wrong in choosing the Diffusivity model.")

Diffusivity.setValue(D_choice_local)
print("The diffusivity is set to " + str(config.D_choice))

# ---------------------------------------------------------
# The old initial conditions by Paquay 2012. It requires the Diffusivity
# to already be set.
if config.paquay_init_conds is True:
    density.setValue(-(config.Gamma_c * lambda_n / Diffusivity)
                     * (1.0 + x / lambda_n))
    temperature.setValue(config.q_c * ((gamma - 1.0) / config.Gamma_c)
                         * (1.0 - lambda_n / (zeta * lambda_T + lambda_n)
                         * (1.0 + x / lambda_n)**-zeta))


# ----------------- Boundary Conditions -------------------
def set_boundary_values(AGamma_c, Aq_c):
    """
        Density Boundary Conditions:
        d/dx(n(0)) == n / lambda_n
        d/dx(n(L)) == -Gamma_c / Diffusivity
    """
    density.faceGrad.constrain(density.faceValue / lambda_n,
                               mesh.facesLeft)
    density.faceGrad.constrain(-AGamma_c / Diffusivity.faceValue,
                               mesh.facesRight)

    """
        Temperature Boundary Conditions:
        d/dx(T(0)) = T / lambda_T
        d/dx(T(L)) = zeta*(Gamma_c*T - q_c*(gamma - 1)) / (Diffusivity * n)
    """
    temperature.faceGrad.constrain(temperature.faceValue / lambda_T,
                                   mesh.facesLeft)
    temperature.faceGrad.constrain(
        (zeta * (AGamma_c * temperature.faceValue - Aq_c * (gamma - 1.0)))
        / (Diffusivity.faceValue * density.faceValue),
        mesh.facesRight)

    """
        Paquay considered these Z Boundary Conditions at the edge:
        Z(0) = const.
        d/dx(Z(0)) == 0
        d/dx(Z(0)) == Z / lambda_Z
        d^2/dx^2(Z(0)) == 0        <- This one is default in the FVM

        Mandatory core boundary condition:
        d/dx(Z(L)) == 0
    """
    Z.faceGrad.constrain(Z.faceValue / lambda_Z, mesh.facesLeft)
#    Z.faceGrad.constrain(0.0, mesh.facesLeft)
    Z.faceGrad.constrain(0.0, mesh.facesRight)


# Set the boundary values now
set_boundary_values(config.Gamma_c, config.q_c)
