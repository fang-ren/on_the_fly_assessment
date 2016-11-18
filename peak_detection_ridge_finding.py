# -*- coding: utf-8 -*-
"""
Created on Nov 17 2016

@author: Fang Ren
"""


from scipy.signal import cwt, ricker, find_peaks_cwt
import matplotlib.pyplot as plt
import numpy as np


path = 'C:\\Research_FangRen\\Data\\July2016\\Sample1\\Processed\\'

file = path + 'Sample1_24x24_t30_0441_1D.csv'
data = np.genfromtxt(file, delimiter = ',')
Qlist = data[:,0]
IntAve = data[:,1]


widths = np.arange(1, 64, 2)
cwt_coefficient = cwt(IntAve, ricker, widths)
a1 = 1
a2 = 30
peaks = find_peaks_cwt(IntAve, np.arange(a1, a2, 0.05))

plt.subplot((211))
plt.pcolormesh(Qlist, widths, cwt_coefficient)
plt.plot(Qlist, [a1]* len(Qlist), 'r--')
plt.plot(Qlist, [a2]* len(Qlist), 'r--')
plt.xlim(0.65, 6.45)
plt.ylim(1, 63)
# plt.clim(np.nanmin(np.log(cwt_coefficient)), np.nanmax(np.log(cwt_coefficient)))

plt.subplot((212))
plt.plot(Qlist, IntAve)
plt.plot(Qlist[peaks], IntAve[peaks], 'o')
plt.xlim(0.65, 6.45)
