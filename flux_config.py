Gamma_c = -1.0e22
q_c = 5.0e2 * Gamma_c

nx = 100

taylor_model = False

res_tol = 1.0e14

# Total time steps; should be ~ L^2 / D
total_timeSteps = 2000

timeStep = 5.0e-6

D_choice = "D_flow_shear"
alpha_sup = 1.0e-3
beta = 2.0
shear_a1, shear_a2, shear_a3 = 1.0e-3, 0.0, 5.0e-4

paquay_init_conds = False
initial_H_mode = False
generate_plots = True

# Plot details
ploty_max = None

aux_plots = True

aux_vars = ['Gamma_ol', 'Gamma_an', 'Gamma_bulk', 'Gamma_cx']
# aux_ymin = ['',0.0,0.0,'']

save_plots = False
# save_TSVs = False

save_directory = "Short_Plots"
