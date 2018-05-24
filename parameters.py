"""
	This file contains the simple constant delcarations
	for use in the PDE system. This includes machine
	parameters, length scales, global physical/math
	constants, and non-g model numbers.
"""

from input_handling import *
from scipy import constants


# ----------------- Physical Constants --------------------
pi = constants.pi
charge = constants.e							# Elementary charge
m_e = constants.m_e								# Electron mass
m_i = constants.m_p								# Ion (H) mass
epsilon_0 = constants.epsilon_0					# Permittivity of free space
mu_0 = constants.mu_0							# Permeability of free space
gamma = 5.0 / 3.0								# Adiabatic index for monoatomic


# ----------------- ASDEX-U Specifications ----------------
a_v = 0.8   									# Vertical minor radius
a_h = 0.5   									# Horizontal minor radius
a_m = ( (a_v**2 + a_h**2) / 2.0 )**(1.0/2.0)	# Mean minor radius
R = 1.65										# Major radius
I_phi = 1.6e6   								# Plasma current
B_phi = 3.1 									# Toroidal field
B_theta = mu_0 * I_phi / ( 2*pi*a_m )   		# Poloidal field
B = ( B_phi**2 + B_theta**2 )**(1.0/2.0)		# Full field


# ----------------- ITER Specifications -------------------
#a_m = 2.0									# Mean minor radius
#R = 6.2										# Major radius
#I_phi = 15.0e6								# Plasma current
#B_phi = 5.3									# Toroidal field
#B_theta = mu_0 * I_phi / ( 2*pi*a_m )			# Poloidal field
#B = ( B_phi**2 + B_theta**2 )**(1.0/2.0) 	# Full field


aspect = a_m / R								# Aspect Ratio
q = aspect * B_phi/B_theta						# q value


## PRESET parameters for quick calculation, many of which
## are chosen by Staps and Paquay


if config.taylor_model == True:
	L = 4.0										# in AU
	lambda_n = 5.0 / 4.0						# Length scales for decay at edge
	lambda_T = 3.0 / 2.0
	lambda_Z = 5.0 / 4.0
elif config.taylor_model == False:
	L = 0.05									# in m
	lambda_n = 0.01
	lambda_T = 0.0125
	lambda_Z = 0.01

mu = 1.0 / 20.0

D_max = 5.0
D_min = 2.0/5.0

epsilon = 1.0 / 25.0
zeta = 0.5

## Choose set of parameters
# If numerical_choice is not defined, not a string, or set to Paquay:
if config.numerical_choice.lower() == "paquay":
	# Paquay's numbers
	c_n = 1.1
	c_T = 0.9
	a = -1.5
	b = 1.0
	c = -1.0
	Z_S = 1.4

# Stap's numbers
elif config.numerical_choice.lower() == "staps":
	c_n = -1.1
	c_T = -0.9
	a = 3.0/2.0
	b = 2.0
	c = -1.0
	Z_S = -3.0/2.0


## For use in full flux model
alpha_an = 1.5				# Anomalous loss coefficient
alpha_cx = 1.5				# Charge exchange coefficient

