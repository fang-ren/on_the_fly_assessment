# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13

@author: fangren

"""

import matplotlib.pyplot as plt
import numpy as np
import scipy

def save_Qchi(Q, chi, cake, imageFilename, save_path):
    Q, chi = np.meshgrid(Q, chi)
    plt.figure(1)
    plt.title('Q-chi polarization corrected_log scale')
    plt.pcolormesh(Q, chi, np.log(cake))
    plt.xlabel('Q')
    plt.ylabel('chi')
    plt.xlim((0.7, 6.8))
    plt.ylim((-56, 56))
    plt.clim((0, np.log(np.nanmax(cake))))
    # the next two lines contributed by S. Suram (JCAP)
    inds = np.nonzero(cake)
    plt.clim(scipy.stats.scoreatpercentile(np.log(cake[inds]), 5),
             scipy.stats.scoreatpercentile(np.log(cake[inds]), 95))
    plt.colorbar()
    plt.savefig(save_path + imageFilename[:-4]+'_Qchi')
    
    plt.close()

