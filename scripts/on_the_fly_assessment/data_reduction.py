# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13

@author: fangren

"""

import pyFAI
from PIL import Image
import numpy as np


def data_reduction(imArray, d, Rot, tilt, lamda, x0, y0, PP, pixelsize):
    """
    The input is the raw file's name and calibration parameters
    return Q-chi (2D array) and a spectrum (1D array)
    """    
    s1 = int(imArray.shape[0])
    s2 = int(imArray.shape[1])

    # refer to http://pythonhosted.org/pyFAI/api/pyFAI.html for pyFAI parameters
    detector_mask = np.ones((s1,s2))*(imArray <= 0)

    p = pyFAI.AzimuthalIntegrator(wavelength=lamda)
    p.setFit2D(d, x0, y0, tilt, Rot, pixelsize, pixelsize)
    cake, Q, chi = p.integrate2d(imArray, 1000, 1000, mask=detector_mask, polarization_factor=PP)
    Q = Q * 10e8 # the pyFAI output unit for Fit2D gemoetry is not correct. Multiply by 10e8 for correction
    chi = chi + 90

    Qlist, IntAve = p.integrate1d(imArray, 1000, mask=detector_mask, polarization_factor=PP)

    Qlist = Qlist * 10e8

    return Q, chi, cake, Qlist, IntAve

