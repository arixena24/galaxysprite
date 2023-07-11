#!/usr/bin/env python
# coding: utf-8

# In[9]:


get_ipython().run_line_magic('run', 'main.py')


# In[11]:


galactic_radius = 20  ##galactic radius is fixed in kpc
    
def mass_density_plot(radius, density_catalog, z, title = "Mass Density"): 
        
        "takes in radius and density catalog and plots the mass density" 
        
        for z in density_catalog: 
            masses = density_catalog[z]
            
            x = masses
            y = radius 
            
        plt.plot(x,y) 
        plt.title(title)


# In[ ]:




