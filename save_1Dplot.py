# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13

@author: fangren

"""

import matplotlib.pyplot as plt


def save_1Dplot(Qlist, IntAve, peaks, imageFilename, save_path):
    # generate a column average image
    plt.figure(2)
    plt.title('Column average')
    plt.plot(Qlist[peaks], IntAve[peaks], linestyle = 'None', c = 'r', marker = 'o')
    plt.plot(Qlist, IntAve)
    plt.xlabel('Q')
    plt.ylabel('Intensity')
    plt.xlim((0.7, 6.4))

    plt.savefig(save_path + imageFilename[:-4]+'_1D')
    
    plt.close()