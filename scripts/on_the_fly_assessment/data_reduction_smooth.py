# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13

@author: fangren

"""

import pyFAI
from PIL import Image
import numpy as np
from scipy import signal

def data_reduction(imArray, d_in_pixel, Rot, tilt, lamda, x0, y0, PP):
    s1 = int(imArray.shape[0])
    s2 = int(imArray.shape[1])
    imArray = signal.medfilt(imArray, kernel_size = 5)
    # refer to http://pythonhosted.org/pyFAI/api/pyFAI.html for pyFAI parameters
    detector_mask = np.ones((s1,s2))*(imArray <= 0)
    pixelsize = 79    # measured in microns
    d = d_in_pixel*pixelsize*0.001  # measured in milimeters

    p = pyFAI.AzimuthalIntegrator(wavelength=lamda)
    p.setFit2D(d,x0,y0,tilt,Rot,pixelsize,pixelsize)
    cake,Q,chi = p.integrate2d(imArray,1000, 1000, mask = detector_mask, polarization_factor = PP)
    # the output unit for Q is angstrom-1
    Q = Q * 10e8  # the pyFAI output unit for Fit2D gemoetry is not correct. Multiply by 10e8 for correction
    chi = chi+90

    Qlist, IntAve = p.integrate1d(imArray, 1000, mask = detector_mask, polarization_factor = PP)

    # the output unit for Q is angstrom-1
    Qlist = Qlist * 10e8
    return Q, chi, cake, Qlist, IntAve

