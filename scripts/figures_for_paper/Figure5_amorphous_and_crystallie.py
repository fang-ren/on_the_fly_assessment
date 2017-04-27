"""
Created on Feb 7 2017

@author: Fang Ren
"""
import numpy as np
import matplotlib.pyplot as plt

path = '..\\..\\data\\'
file1 = path + 'Figure5_amorphous.csv'
file2 = path + 'Figure5_crystalline.csv'

save_path = '..\\..\\figures\\'

data1 = np.genfromtxt(file1, delimiter = ',')
data2 = np.genfromtxt(file2, delimiter = ',')

plt.figure(1, (5,4))
plt.plot(data1[:,0], data1[:,1], label = 'amorphous')
plt.plot(data2[:,0], data2[:,1], label = 'crystalline')
plt.xlim(0.64, 5.9)
plt.ylim(500, 7000)
plt.legend()
plt.xlabel('Q')
plt.ylabel('Intensity')
plt.savefig(save_path+'Figure5', dpi = 600)