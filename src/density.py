import pickle
from re import L
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np
from scipy.optimize import curve_fit

file_input_dm = './data/input/cat_id_0_dm_coords_snap_90'
file_input_star = './data/input/cat_id_0_stars_coords_snap_90'

with open(file_input_dm, 'rb') as f:
    coords_dm = pickle.load(f)
with open(file_input_star, 'rb') as f:
    coords_star = pickle.load(f)

def cal_density(coords_ptl, coords_ctr, r_bins = np.arange(0, 5000, 50)):

    del_coords = coords_ptl - coords_ctr

    rs = np.sqrt(np.sum((del_coords)**2, axis = 1))
    
    hist, _ = np.histogram(rs, r_bins)
    
    r_density = hist / ( 4/3 * np.pi * (r_bins[1:]**3 - r_bins[:-1]**3) ) 

    return r_bins[:-1], r_density

# pseudo-isothermal profile
def fit_isoT(rr, rho0, rc):
    rdensity = rho0 * (1 + (rr/rc)**2)**(-1)
    return rdensity

# Navarro–Frenk–White profile
def fit_NFW(rr, rho0, Rs):
    rdensity = rho0 / (rr/Rs) / (1 + rr/Rs)**2
    return rdensity

# Einasto profile
def fit_Ein(rr, rho0, dn, n, re):
    rdensity = rho0 * np.exp(-dn * (rr/re**(1/n) - 1) )
    return rdensity

# def cal_ylims(xs, ys):



coords_ctr =  np.average(coords_dm, axis = 0)


r_bins, dm_density = cal_density(coords_dm, coords_ctr)
r_bins, star_density = cal_density(coords_star, coords_ctr)

fig, ax = plt.subplots(figsize = (8, 6))

ax.scatter(r_bins, dm_density, label = 'DM')
ax.scatter(r_bins, star_density, label = 'Star')

popt, pcov = curve_fit(fit_NFW, r_bins, dm_density)
ax.plot(r_bins, fit_NFW(r_bins, *popt), linestyle = '--', label = 'NFW profile')

# popt, pcov = curve_fit(fit_Ein, r_bins, dm_density)
# ax.plot(r_bins, fit_Ein(r_bins, *popt), linestyle = '--', label = 'Einasto profile')

popt, pcov = curve_fit(fit_isoT, r_bins, dm_density)
ax.plot(r_bins, fit_isoT(r_bins, *popt), linestyle = '--', label = 'Isothermal profile')


ax.legend(fontsize = 15)

ax.set_yscale('log')
ax.set_xlabel('distance from center [kpc]', fontsize = 15)
ax.set_ylabel('density []', fontsize = 15)

fig.savefig('temp.png')
