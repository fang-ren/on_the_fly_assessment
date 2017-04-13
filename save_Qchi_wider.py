"""
author: Fang Ren (SSRL)

4/13/2017
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13

@author: fangren

"""

import numpy as np
import scipy
import os.path
import scipy.io


def save_Qchi_wider(Q, chi, cake, imageFilename, save_path, low, high):
    Q, chi = np.meshgrid(Q, chi)
    keep = (Q >= low) * (Q <= high)

    Q = Q[keep]
    chi = chi[keep]
    cake = cake[keep]
    length = Q.size
    cake = cake.reshape(2880, length / 2880)
    Q = Q.reshape(2880, length / 2880)
    chi = chi.reshape(2880, length / 2880)

    # print Q.shape, chi.shape, cake.shape

    scipy.io.savemat(os.path.join(save_path, imageFilename[:-4] + '_Qchi_wider.mat'),
                     {'Q': Q, 'chi': chi, 'cake': cake})

