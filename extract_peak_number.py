# -*- coding: utf-8 -*-
"""
Created on Wed Aug 03 15:00:51 2016

@author: fangren
"""

from scipy.signal import find_peaks_cwt
import numpy as np


def extract_peak_num(Qlist, IntAve, index, a1 = 1, a2 = 30):
    """
    extract the peak numbers from 1D spectra
    """
    peaks = find_peaks_cwt(IntAve, np.arange(a1, a2, 0.05))
    peaks = peaks[1:-1]

    newRow = [index, len(peaks)]
    return newRow, peaks