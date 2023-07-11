import pickle
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np

file_input_dm = './data/input/cat_id_0_dm_coords_snap_90'
file_input_star = './data/input/cat_id_0_star_coords_snap_90'

with open(file_input_dm, 'rb') as f:
    coords_dm = pickle.load(f)
with open(file_input_star, 'rb') as f:
    coords_star = pickle.load(f)

def cal_density(coords_ptl, coords_ctr, r_bins = np.arange(0, 1000, 10)):

    del_coords = coords_ptl - coords_ctr

    rs = np.sqrt(np.sum((del_coords)**2, axis = 1))
    
    hist, _ = np.histogram(rs, r_bins)
    
    r_density = hist / ( 4/3 * np.pi * (r_bins[1:]**3 - r_bins[:-1]**3) ) 

    return r_bins[:-1], r_density

coords_dm = coords_dm
coords_star = coords_star

coords_ctr =  np.average(coords_dm, axis = 0)


r_bins, dm_density = cal_density(coords_dm, coords_ctr)
_ , star_density = cal_density(coords_star, coords_ctr)


fig, ax = plt.subplots(figsize = (8, 6))

ax.scatter(r_bins, dm_density)
ax.scatter(r_bins, star_density)

fig.savefig('temp.png')