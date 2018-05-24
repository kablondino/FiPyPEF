"""
	This is an example configuration file. Read the other
	source files to see what values get defaulted.
"""

# Particle and heat flux from the core
Gamma_c = -0.8
q_c = 5.0*Gamma_c

# Number of cells
nx = 200

# Boolean, to choose either the Taylor-expanded numerical model, or
# the full flux model. Note that it sets the length of the domain
# L to be 4.0 AU in Taylor-expanded, and 0.03 m in the flux model.
taylor_model = True

res_tol = 1.0e-6

# Total time steps; should be ~ L^2 / D
total_timeSteps = 1000

# Size of the time step
timeStep = 1.0 / 375.0

# Choose the Diffusivity model, as a string (case does not matter)
# D_Zohm, D_Staps, and D_Shear are the possibilities
D_choice = "D_Flow_Shear"
# Coefficient of (Z')**beta in Stap's diffusivity
alpha_sup = 0.25
# Exponent of Z' in Stap's diffusivity
beta = 2.0

# If the D_choice is set to the flow-shear model, this would be the parameters
shear_a1, shear_a2, shear_a3 = 0.1, 0.0, 0.1

# Initial condition choice, with True representing Paquay's initial conditions,
# and False representing linear profiles.
paquay_init_conds = False

# Boolean, to choose what mode to have as initial conditions, only as
# linear profiles, from the file 'boundary_init_conds.py'
initial_H_mode = False

# Boolean, to show plots
generate_plots = True

# Choose numerical values for the Taylor-expanded Z-equation
# Currently, choices are Staps and Paquay
numerical_choice = "Staps"

# Plot details
plot_title = "$D \sim 1 / [1 + 0.1 (Z)^2 + 0.25 (Z^\prime)^{2}]$"\
		+"\n" + r"$\Gamma_c = {:.3g},\, T \,=\, {:d},\,$"\
		.format(Gamma_c, total_timeSteps)\
		+ r"$\Delta t \,=\, {:.3e}$".format(timeStep)

# Maximum x on the plots
ploty_max = 5.2

aux_plots = False

# Aux plots details
# aux_vars MUST be an list of strings
aux_vars = ['rho_pi', 1.2541, 'v_Ti']
# The second entry in all of the aux plot arrays will be deleted, due
# to bad data type.

aux_titles = ["RHO", "1.2541", "v_Ti"]
aux_ymin = [0.0, 5.0, 0.0]
aux_ymax = []
# The above are optional

# Should the results be saved to file?
save_plots = False
save_TSVs = False

save_directory = "SAVE_DIRECTORY"

