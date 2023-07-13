import pickle
from re import I
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np
from scipy.optimize import curve_fit


class Density(object):

    def __init__(self, coords_star, coords_dm, coords_ctr, r_bins = np.arange(0, 5000, 50)):
        """_summary_

        Args:
            coords_star (_type_): _description_
            coords_dm (_type_): _description_
            coords_ctr (_type_): _description_
        """

        self.coords_star = coords_star
        self.coords_dm = coords_dm
        self.coords_ctr = coords_ctr
        self.r_bins = r_bins



    def cal_density(self, coords_ptl, coords_ctr):

        """This calculates the mass density

        Args:
            coords_ptl (nx3 array): coordinates of particles
            coords_ctr (1x3 array): coordinate at center
            r_bins (array): radial distance 

        Returns:
            _type_: _description_
        """

        del_coords = coords_ptl - coords_ctr

        rs = np.sqrt(np.sum((del_coords)**2, axis = 1))
        
        hist, _ = np.histogram(rs, r_bins)
        
        r_density = hist / ( 4/3 * np.pi * (r_bins[1:]**3 - r_bins[:-1]**3) ) 

        return r_density

    # pseudo-isothermal profile
    def profile_isoT(self, rr, rho0, rc):
        """_summary_

        Args:
            rr (_type_): _description_
            rho0 (_type_): _description_
            rc (_type_): _description_

        Returns:
            _type_: _description_
        """
        rdensity = rho0 * (1 + (rr/rc)**2)**(-1)
        return rdensity

    # Navarro–Frenk–White profile
    def profile_NFW(self, rr, rho0, Rs):
        """_summary_

        Args:
            rr (_type_): _description_
            rho0 (_type_): _description_
            Rs (_type_): _description_

        Returns:
            _type_: _description_
        """
        rdensity = rho0 / (rr/Rs) / (1 + rr/Rs)**2
        return rdensity

    # Einasto profile
    def profile_Ein(self, rr, rho0, dn, n, re):
        """_summary_

        Args:
            rr (_type_): _description_
            rho0 (_type_): _description_
            dn (_type_): _description_
            n (_type_): _description_
            re (_type_): _description_

        Returns:
            _type_: _description_
        """

        rdensity = rho0 * np.exp(-dn * (rr/re**(1/n) - 1) )
        return rdensity

    def fit_profile(self, func):

        popt, pcov = curve_fit(func, self.r_bins, self.dm_density)

        result = func(self.r_bins, *popt)
        return result

    def plot_density(self, draw_isoT = True, draw_Ein = True, draw_NFW = True):

        fig, ax = plt.subplots(figsize = (8, 6))

    _, dm_density = cal_density(self.coords_dm, self.coords_ctr)
    _, star_density = cal_density(self.coords_star, self.coords_ctr)

        ax.scatter(self.r_bins[:-1], dm_density, label = 'DM')
        ax.scatter(self.r_bins[:-1], star_density, label = 'Star')

        if draw_isoT:
            result_fit = self.fit_NFW(r_bins, *popt)
            ax.plot(self.r_bins[:,-1], result_fit, linestyle = '--', label = 'Isothermal profile')
    
        if draw_Ein:
            result_fit = self.fit_Ein(r_bins, *popt)
            ax.plot(self.r_bins[:,-1], result_fit, linestyle = '--', label = 'Einasto profile')
    
        if draw_NWF:
            result_fit = self.fit_NWF(r_bins, *popt)
            ax.plot(self.r_bins[:,-1], result_fit, linestyle = '--', label = 'NFW profile')
    

        return fig, ax


file_input_dm = './data/input/cat_id_0_dm_coords_snap_90'
file_input_star = './data/input/cat_id_0_stars_coords_snap_90'

with open(file_input_dm, 'rb') as f:
    coords_dm = pickle.load(f)
with open(file_input_star, 'rb') as f:
    coords_star = pickle.load(f)

coords_ctr =  np.average(coords_dm, axis = 0)


ax.legend(fontsize = 15)

ax.set_yscale('log')
ax.set_xlabel('distance from center [kpc]', fontsize = 15)
ax.set_ylabel('density []', fontsize = 15)
