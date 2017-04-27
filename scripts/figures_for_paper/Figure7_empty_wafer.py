# -*- coding: utf-8 -*-
"""
Created on Wed July 13 2016

@author: fangren
"""


import numpy as np
import matplotlib.pyplot as plt
import glob
import os
from os.path import basename
import imp


path = '..\\..\\data\\'
filename = path + 'Figure8_phase_change.csv'
save_path = '..\\..\\figures\\'

data = np.genfromtxt(filename, delimiter=',', skip_header = 1)
plate_x = data[:,1]
plate_y = data[:,2]
color_intensity = [0.8]*len(plate_x)

area = 115

plt.figure(1, figsize = (6, 4.5))
# plt.title('crystallinity analysis')
plt.scatter(plate_y, plate_x, c = color_intensity, s = area, marker = 's', linewidths=.5, edgecolors= 'k', cmap = 'jet')
plt.xlim((-36, 36))
plt.ylim((-36, 36))
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.clim((0.2, 1.4))
plt.savefig(save_path+'Figure7', dpi = 600)

