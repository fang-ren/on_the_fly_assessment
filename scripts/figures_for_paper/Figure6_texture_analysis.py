# -*- coding: utf-8 -*-
"""
Created on Mon May 23

@author: fangren

"""

import pyFAI
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# open MARCCD tiff image
path = '..\\..\\data\\'
im = Image.open(path + 'Figure6_textured.tif')
save_path = '..\\..\\figures\\'

# change image object into an array
imArray = np.array(im)
s = int(imArray.shape[0])
im.close()

detector_mask = np.ones((s,s))*(imArray <= 0)

# parameters I originally used.
d_in_pixel = 2462.69726489     # distance from sample to detector plane along beam direction in pixel space
Rot = (np.pi*2-4.69729438873)/(2*np.pi)*360  #detector rotation
tilt = 0.503226642865/(2*np.pi)*360   # detector tilt
lamda = 0.97621599151  # wavelength
x0 = 969.878684978     # beam center in pixel-space
y0 = 2237.93277884    # beam center in pixel-space
PP = 0.95   # beam polarization, decided by beamline setup


pixelsize = 79    # measured in microns
d = d_in_pixel*pixelsize*0.001  # measured in milimeters

p = pyFAI.AzimuthalIntegrator(wavelength=lamda)
p.setFit2D(d,x0,y0,tilt,Rot,pixelsize,pixelsize)
cake,Q,chi = p.integrate2d(imArray,1000, 1000, mask = detector_mask, polarization_factor = PP)
Q = Q * 10e8
chi = chi+90
Qlist, IntAve = p.integrate1d(imArray, 1000, mask=detector_mask, polarization_factor=PP)
Qlist = Qlist * 10e8


# generate a  Q-gamma image with polar correction
Q, chi = np.meshgrid(Q, chi)
plt.figure(2, (5,4))
# plt.title('Q-$\Psi$')
plt.pcolormesh(Q, chi, cake, cmap = 'jet')
#plt.imshow(cake)
plt.ylabel('$\gamma$')
plt.xlabel('Q')
plt.xlim((0.6, 5.87))
plt.ylim((-58, 63))
plt.colorbar()
plt.clim(0, 9000)
plt.tight_layout()
plt.savefig(save_path+ 'Figure6(a)', dpi = 600)



# generate a column average image
plt.figure(3, (5,4))
# plt.title('Column sum')
Qlist, IntAve = p.integrate1d(imArray, 1000, mask = detector_mask, polarization_factor = PP)
Qlist = Qlist * 10e8
plt.plot(Qlist, IntAve)
plt.xlabel('Q')
plt.ylabel('Intensity')
plt.xlim((0.6, 5.87))
plt.tight_layout()
plt.savefig(save_path+ 'Figure6(b)', dpi = 600)


# generate a texture image
plt.figure(4, (5,4))

keep = np.where(cake != 0)
chi = chi*np.pi/180

IntSum = np.bincount((Q[keep].ravel()*100).astype(int), cake[keep].ravel().astype(int))
count = np.bincount((Q[keep].ravel()*100).astype(int), np.ones((s,s))[keep].ravel().astype(int))
IntAve = list(np.array(IntSum)/np.array(count))

textureSum = np.bincount((Q[keep].ravel()*100).astype(int), (cake[keep]*np.cos(chi[keep])).ravel())
chiCount = np.bincount((Q[keep].ravel()*100).astype(int), (np.cos(chi[keep])).ravel())

texture = list(np.array(textureSum)/np.array(IntAve)/np.array(chiCount)-1)

step = 0.01
Qlen = len(textureSum)
Qlist_texture = [i*step for i in range(Qlen)]

plt.plot(Qlist_texture, texture)
plt.xlabel('Q')
plt.ylabel('Texture')
plt.xlim((0.6, 5.87))
plt.tight_layout()
plt.savefig(save_path+ 'Figure6(c)', dpi = 600)