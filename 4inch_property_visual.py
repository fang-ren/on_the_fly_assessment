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

plotTernary = imp.load_source("plt_ternary_save", "plotTernary.py")

path = 'C:\\Research_FangRen\\Python codes\\on_the_fly_module_windows\\test\\'


def twoD_visualize(path):
    """
    create three lists for plotting: plate_x, plate_y, ROI1, ROI2, ROI3...
    """
    for filename in glob.glob(os.path.join(path, '*.csv')):
        if basename(filename)[-5] == 'a':
                data = np.genfromtxt(filename, delimiter=',', skip_header = 1)
                plate_x = data[:,1]
                plate_y = data[:,2]
                ROI1 = data[:,15]
                ROI2 = data[:,16]
                ROI3 = data[:,17]
                ROI5 = data[:,19]
                crystallinity = data[:,51]
                texture_sqrSum = data[:,53]
                metal1 = data[:,54]
                metal2 = data[:,55]
                metal3 = data[:,56]
    return plate_x, plate_y, ROI1, ROI2, ROI3, ROI5, crystallinity, texture_sqrSum, \
    metal1, metal2, metal3

plate_x, plate_y, ROI1, ROI2, ROI3, ROI5, crystallinity, texture_sqrSum, metal1,\
 metal2, metal3 = twoD_visualize(path)
 
area = [360]*len(plate_x)

plate_x = np.array(plate_x)



plt.figure(1, figsize = (12, 10))
plt.title('Nickel alpha')
plt.scatter(-plate_x, plate_y, c = ROI1, s = area, marker = 's')
plt.colorbar()
plt.xlim((-44, 44))
plt.ylim((-44, 44))
plt.xlabel('Bottom(flat) -plate_x')
plt.ylabel('Left plate_y')
plt.savefig(path+'Nickel alpha.png')

plt.figure(2, figsize = (12, 10))
plt.title('Nickel beta')
plt.scatter(-plate_x, plate_y, c = ROI5, s = area, marker = 's')
plt.colorbar()
plt.xlim((-44, 44))
plt.ylim((-44, 44))
plt.xlabel('Bottom(flat) -plate_x')
plt.ylabel('Left plate_y')
plt.savefig(path+'Nickel beta.png')

plt.figure(5, figsize = (12, 10))
plt.title('crystallinity analysis')
plt.scatter(-plate_x, plate_y, c = np.log(crystallinity), s = area, marker = 's')
plt.xlim((-44, 44))
plt.ylim((-44, 44))
plt.colorbar()
plt.xlabel('Bottom(flat) -plate_x')
plt.ylabel('Left plate_y')
plt.clim((0.2, 1.4))
plt.savefig(path+'crystallinity analysis')

plt.figure(6, figsize = (12, 10))
plt.title('texture analysis')
plt.scatter(-plate_x, plate_y, c = np.log(texture_sqrSum), s = area, marker = 's')
plt.xlim((-44, 44))
plt.ylim((-44, 44))
plt.colorbar()
plt.xlabel('Bottom(flat) -plate_x')
plt.ylabel('Left plate_y')
#plt.clim((-11, -9))
plt.savefig(path+'texture analysis')


ternary_data = np.concatenate(([metal1],[metal2],[metal3],[crystallinity]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Zr','V'), scale=100,
                       sv=True, svpth=path, svflnm='ternary',
                       cbl='Scale', vmin=1, vmax=5, cmap='jet', cb=True, style='h')
                       
plt.close("all")