from scipy.signal import medfilt
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, *params):
    """
    create a Gaussian fitted curve according to params
    """
    y = np.zeros_like(x)
    for i in range(0, len(params), 3):
        ctr = params[i]
        amp = params[i+1]
        wid = params[i+2]
        y = y + amp * np.exp( -((x - ctr)/wid)**2)
    return y

path = 'C:\\Research_FangRen\\Publications\\on_the_fly_paper\\Sample_data\\'
file1 = path + 'amorphous.csv'
file2 = path + 'good_2.csv'
file3 = path + 'good_3.csv'
file4 = path + 'noisy_data_set.csv'


filter_window = 15

data1 = np.genfromtxt(file1, delimiter = ',')
Qlist1 = data1[196:550,0]
IntAve1 = data1[196:550,1]
IntAve_smoothed1 = medfilt(IntAve1, kernel_size= filter_window)
noise1 = IntAve1 - IntAve_smoothed1

data2 = np.genfromtxt(file2, delimiter = ',')
Qlist2 = data2[216:570,0]
IntAve2 = data2[216:570,1]/8+800
IntAve_smoothed2 = medfilt(IntAve2, kernel_size= filter_window)
noise2 = IntAve2 - IntAve_smoothed2

data3 = np.genfromtxt(file3, delimiter = ',')
Qlist3 = data3[170:500,0]
IntAve3 = data3[170:500,1]*20
IntAve_smoothed3 = medfilt(IntAve3, kernel_size= filter_window)
noise3 = IntAve3 - IntAve_smoothed3

data4 = np.genfromtxt(file4, delimiter = ',', skip_header= 1)

Qlist4 = data4[:, 1]
IntAve4 = data4[:, 2]*250000
IntAve_smoothed4 = medfilt(IntAve4, kernel_size= filter_window)
noise4 = IntAve4 - IntAve_smoothed4
noise4 = np.nan_to_num(noise4)

Qlist5 = Qlist4
IntAve5 = data4[:, 4]*250000
Qlist6 = Qlist4
IntAve6 = data4[:, 5]*250000
Qlist7 = Qlist4
IntAve7 = data4[:, 6]*250000
Qlist8 = Qlist4
IntAve8 = data4[:, 7]*250000
Qlist9 = Qlist4
IntAve9 = data4[:, 8]*250000
Qlist10 = Qlist4
IntAve10 = data4[:, 9]*250000
Qlist11 = Qlist4
IntAve11 = data4[:, 10]*250000
Qlist12 = Qlist4
IntAve12 = data4[:, 11]*250000
Qlist13 = Qlist4
IntAve13 = data4[:, 12]*250000

IntAve_sum = IntAve4+IntAve5+IntAve6+IntAve7+IntAve8+IntAve9+IntAve10+IntAve11+IntAve12+IntAve13

IntAve_smoothed_sum = medfilt(IntAve_sum, kernel_size= filter_window)
noise_sum = IntAve_sum - IntAve_smoothed_sum
noise_sum = np.nan_to_num(noise_sum)


plt.figure(1, (12,9))
ax1 = plt.subplot2grid((4,2), (0,0))
ax1.plot(Qlist1, IntAve1, label = 'good data 1')
ax1.plot(Qlist2, IntAve2, label = 'good data 2')
ax1.plot(Qlist3, IntAve3, label = 'good data 3')
ax1.plot(Qlist4, IntAve4, label = 'noisy data')
plt.ylabel('Intensity')
plt.xlim(1.7, 3.7)
plt.ylim(700, 1500)
plt.legend(fontsize = 12)

ax2 = plt.subplot2grid((4,2), (1,0))
ax2.plot(Qlist1, IntAve_smoothed1, label = 'smoothed good data 1')
ax2.plot(Qlist2, IntAve_smoothed2, label = 'smoothed good data 2')
ax2.plot(Qlist3, IntAve_smoothed3, label = 'smoothed good data 3')
ax2.plot(Qlist4, IntAve_smoothed4, label = 'smoothed noisy data')
plt.ylabel('Smoothed Intensity')
plt.xlim(1.7, 3.7)
plt.ylim(700, 1500)
# plt.legend(fontsize = 12)

ax3 = plt.subplot2grid((4,2), (2,0))
ax3.plot(Qlist1, noise1, label = 'good data')
ax3.plot(Qlist2, noise2, label = 'good data 2')
ax3.plot(Qlist3, noise3, label = 'good data 3')
ax3.plot(Qlist4, noise4, label = 'noisy data')
plt.xlabel('Q')
plt.xlim(1.7, 3.7)
plt.ylabel('Noise')


ax4 = plt.subplot2grid((4,2), (3,0))
ax4.plot(Qlist4, IntAve_sum, 'r', label = '10x exposure time')
plt.ylabel('Intensity')
plt.xlabel('Q')
plt.xlim(1.7, 3.7)
plt.ylim(7000, 15000)
plt.legend(fontsize = 12)


guess = [0, 5, 10]
high = [0.5, 300, 1000]
low = [-0.5, 0, 0.1]
bins = np.arange(-100, 100, 0.5)

# the histogram of the noise
ax5 = plt.subplot2grid((4, 2), (0,1))
n1, bins1 = np.histogram(noise1, bins= bins)
# n1[200] = (n1[199]+n1[201])/2
ax5.bar(bins1[:-1], n1, color = 'black', label = 'good data 1')
plt.xlim(-10, 10)
# plt.ylim(0, 10)
popt1, pcov1 = curve_fit(func, bins1[:-1], n1, p0=guess, bounds = (low, high))
fit1 = func(bins1[:-1], *popt1)
ax5.plot(bins1[:-1], fit1, 'b--', linewidth=2)

ax6 = plt.subplot2grid((4, 2), (1,1))
n2, bins2 = np.histogram(noise2, bins= bins)
# n2[200] = (n2[199]+n2[201])/2
ax6.bar(bins2[:-1], n2, label = 'good data 2')
plt.xlim(-50, 50)
# plt.ylim(0, 10)
popt2, pcov2 = curve_fit(func, bins2[:-1], n2, p0=guess, bounds = (low, high))
fit2 = func(bins2[:-1], *popt2)
ax6.plot(bins2[:-1], fit2, 'g--', linewidth=2)

ax7 = plt.subplot2grid((4, 2), (2,1))
n3, bins3 = np.histogram(noise3, bins= bins)
# n3[200] = (n3[199]+n3[201])/2
n3 = medfilt(n3, kernel_size = 3)
ax7.bar(bins3[:-1], n3, label = 'good data 3')
plt.xlim(-50, 50)
# plt.ylim(0, 10)
popt3, pcov3 = curve_fit(func, bins3[:-1], n3, p0=guess, bounds = (low, high))
fit3 = func(bins3[:-1], *popt3)
ax7.plot(bins3[:-1], fit3, 'r--', linewidth=2)

ax8 = plt.subplot2grid((4, 2), (3,1))
n4, bins4 = np.histogram(noise4, bins= bins)
# n4[200] = (n4[199]+n4[201])/2
ax8.bar(bins4[:-1], n4, label = 'noisy data')
plt.xlim(-100, 100)
# plt.ylim(0, 10)
popt4, pcov4 = curve_fit(func, bins4[:-1], n4, p0=guess, bounds = (low, high))
fit4 = func(bins4[:-1], *popt4)
ax8.plot(bins4[:-1], fit4, 'b--', linewidth=2)
plt.xlim(-100, 100)
plt.ylim(0, 10)
plt.ylabel('Counts')
plt.xlabel('noise')


# plt.savefig(path+'figure1', dpi = 600)
#
# power_noise1 = np.sum(np.square(noise1))/len(noise1)
# power_signal1 = np.sum(np.square(IntAve1))/len(IntAve1)
# SNR1 = power_signal1/power_noise1
#
# power_noise2 = np.sum(np.square(noise2))/len(noise2)
# power_signal2 = np.sum(np.square(IntAve2))/len(IntAve2)
# SNR2 = power_signal2/power_noise2
#
# power_noise3 = np.sum(np.square(noise3))/len(noise3)
# power_signal3 = np.sum(np.square(IntAve3))/len(IntAve3)
# SNR3 = power_signal3/power_noise3
#
# power_noise_sum = np.sum(np.square(noise_sum))/len(noise_sum)
# power_signal_sum = np.sum(np.square(IntAve_sum))/len(IntAve_sum)
# SNR_sum = power_signal_sum/power_noise_sum
#
# print SNR1, SNR2, SNR3, SNR_sum
# print np.log10(SNR1)*10, np.log10(SNR2)*10, np.log10(SNR3)*10, np.log10(SNR_sum)*10