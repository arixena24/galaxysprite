import numpy as np
import matplotlib.pyplot as plt
import astropy 
import math 
import os
import pandas as pd

class Dionysus():

    def __init__(self, path_input, path_output):
        
        self.path_input = path_input
        self.path_output = path_output


    def generate_img(self, x_dim, y_dim, n_dim):

        #White Noise as a random function multiplied by the amplitude of the noise, set to 1 as default
        gen = np.random.randn(x_dim, y_dim, n_dim) 

        #could chose add in the atmosphere noise

        # print(gen)
        # plt.imshow()
        # plt.colorbar()
        # return np.abs(WNoise)
        
    
    def stack(arrays, N, figname = ""):
        
        "This functon takes in the data given and returns every given N number of plots" 
        
        for N in range(arrays):
            figs = arrays[N]
            
            plt.imshow(fig)
            plt.colorbar()
            plt.title(figname)
            plt.savefig(figname) 
            
            
            
    def DEC_RA(plot, dec, ra, radtype ='radian', figname = "Cutout"): 
       
        "function to cut out a slice of an object given a particular dec and ra" 
       
        #makes sure that ra and dec are in radian
        if radtype == 'radian': 
            ras = ra
            decs = dec
         
        else: 
            ras = np.deg2rad(ra)
            decs = np.deg2rad(dec)
        
        coordinates = (ras, decs)
        
        
        #set up the size of the box
        ras_start = max(ras - N //2, 0)
        ras_end = min(ras + N // 2)
        dec_start = max(decs - N // 2)
        dec_end = min(decs + N // 2 + 1)
        
        ras_region = ras[ras_start:ras_end]
        dec_region = dec[dec_start:dec_end]

        # Cut out the region from the imshow array
        region = imshow_array[dec_region, ras_region]

        #plots the cutout
        plt.imshow(region)
        plt.title(figname)
        plt.colorbar()
        
          

    # array to video

