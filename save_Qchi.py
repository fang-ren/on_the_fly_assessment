# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13

@author: fangren

"""

import matplotlib.pyplot as plt
import numpy as np
import scipy
import os.path
import scipy.io


def save_Qchi(Q, chi, cake, imageFilename, save_path, low, high):
    Q, chi = np.meshgrid(Q, chi)
    keep = (Q >= low) * (Q <= high)

    Q = Q[keep]
    chi = chi[keep]
    cake = cake[keep]
    length = Q.size
    cake = cake.reshape(2880, length / 2880)
    Q = Q.reshape(2880, length / 2880)
    chi = chi.reshape(2880, length / 2880)

    scipy.io.savemat(os.path.join(save_path, imageFilename[:-4] + '_Qchi.mat'), {'Q': Q, 'chi': chi, 'cake': cake})

    # print Q.shape, chi.shape, cake.shape
    plt.figure(1)
    plt.title('Q-chi polarization corrected_log scale')
    plt.imshow(np.log(cake))
    plt.clim((0, np.log(np.nanmax(cake))))
    plt.xlabel("Q")
    plt.ylabel("chi")
    # the next two lines contributed by S. Suram (JCAP)
    inds = np.nonzero(cake)
    plt.clim(scipy.stats.scoreatpercentile(np.log(cake[inds]), 5),
             scipy.stats.scoreatpercentile(np.log(cake[inds]), 95))
    plt.colorbar()
    plt.savefig(os.path.join(save_path, imageFilename[:-4] + '_Qchi'))

    plt.close()

