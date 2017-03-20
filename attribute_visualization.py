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


path = 'C:\\Research_FangRen\\Publications\\on_the_fly_paper\\Sample_data\\'
filename = path + 'phase_change.csv'

data = np.genfromtxt(filename, delimiter=',', skip_header = 1)
plate_x = data[:,1]
plate_y = data[:,2]
ROI1 = data[:,15]
ROI2 = data[:,16]
ROI3 = data[:,17]
ROI5 = data[:,19]
crystallinity = data[:,51]
texture = data[:,53]
metal1 = data[:,54]
metal2 = data[:,55]
metal3 = data[:,56]
peak_num = data[:,55]
neighbor_distance = data[:,57]
SNR = data[:,58]

area = 115

plt.figure(1, figsize = (6, 4.5))
# plt.title('crystallinity analysis')
plt.scatter(plate_y, plate_x, c = np.log(crystallinity), s = area, marker = 's', linewidths=.5, edgecolors= 'k', cmap = 'jet')
plt.xlim((-36, 36))
plt.ylim((-36, 36))
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.clim((0.2, 1.4))
plt.savefig(path+'crystallinity analysis', dpi = 600)

plt.figure(2, figsize = (6, 4.5))
# plt.title('texture analysis')
plt.scatter(plate_y, plate_x, c = np.log(texture), s = area, marker = 's', linewidths=.5, edgecolors= 'k',cmap = 'jet')
plt.xlim((-36, 36))
plt.ylim((-36, 36))
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.clim((-11.1, -10.3))
plt.savefig(path+'texture analysis', dpi = 600)


plt.figure(5, figsize = (6, 4.5))
plt.scatter(plate_y, plate_x, c = np.log(neighbor_distance), s = area, marker = 's',linewidths=.5, edgecolors= 'k', cmap = 'jet')
plt.xlim((-36, 36))
plt.ylim((-36, 36))
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.clim(-10.4, -5.6)
plt.savefig(path+'neighbor_distance', dpi = 600)


plt.figure(6, figsize = (6, 4.5))
plt.scatter(plate_y, plate_x, c = peak_num, s = area, marker = 's',linewidths=.5, edgecolors= 'k', cmap = 'jet')
plt.xlim((-36, 36))
plt.ylim((-36, 36))
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.clim(1, 8)
plt.savefig(path+'peak_num', dpi = 600)
#
#
#
# plt.figure(7, figsize = (6, 4.5))
# plt.scatter(plate_y, plate_x, c = 10*np.log(SNR), s = area, marker = 's')
# plt.xlim((-36, 36))
# plt.ylim((-36, 36))
# plt.colorbar()
# plt.xlabel('x')
# plt.ylabel('y')
# plt.clim(150, 156)
# plt.savefig(path+'SNR_2', dpi = 600)
#
