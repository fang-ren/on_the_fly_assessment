
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13

@author: fangren

"""

import matplotlib.pyplot as plt
import os.path
import numpy as np


def save_noise_spectrum(Q, chi, cake, save_path, imageFilename, low, high):
    Q_mesh, chi_mesh = np.meshgrid(Q, chi)
    keep = (Q_mesh >= low) * (Q_mesh <= high)

    # print Q_mesh.shape, cake.shape, chi_mesh.shape, keep.shape

    cake = cake[keep]
    length = cake.size
    cake = cake.reshape(2880, length / 2880)

    cake_chi_sum = np.sum(cake, 1)

    # print cake.shape, cake_chi_sum.shape, chi.shape

    plt.figure(12)

    # changed by Tim Furnish 3/16/17
    # plt.title('Noise spectrum')
    plt.title('I vs. chi data')

    # plt.plot(Qlist[peaks], IntAve[peaks], linestyle = 'None', c = 'r', marker = 'o')
    plt.plot(chi, cake_chi_sum)
    plt.xlabel('chi')
    plt.ylabel('Intensity')

    # changed by Tim Furnish 3/16/17
    # plt.savefig(os.path.join(save_path, imageFilename[:-4]+'_noise'))
    plt.savefig(os.path.join(save_path, imageFilename[:-4] + '_chiI'))
    plt.close()