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

x
    # image confirmation
    
    # img to arrary

    # array to video

