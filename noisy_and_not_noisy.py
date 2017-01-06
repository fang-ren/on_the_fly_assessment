from scipy.signal import savgol_filter
import numpy as np
import matplotlib.pyplot as plt


path = 'C:\\Research_FangRen\\Publications\\on_the_fly_paper\\Sample_data\\'

file2 = path + 'good_2.csv'
file1 = path + 'amorphous.csv'
file3 = path + 'noisy_data_set.csv'


filter_window = 15

data1 = np.genfromtxt(file1, delimiter = ',')
Qlist1 = data1[196:550,0]
IntAve1 = data1[196:550,1]
IntAve_smoothed1 = savgol_filter(IntAve1, filter_window, 2)
noise1 = IntAve1 - IntAvesmoothed1

data2 = np.genfromtxt(file2, delimiter = ',')
Qlist2 = data2[170:500,0]
IntAve2 = data2[170:500,1]*20
IntAve_smoothed2 = savgol_filter(IntAve2, filter_window, 2)
noise2 = IntAve2 - IntAve_smoothed2

data3 = np.genfromtxt(file3, delimiter = ',', skip_header= 1)

Qlist3 = data3[:, 1]
IntAve3 = data3[:, 2]*250000
IntAve_smoothed3 = savgol_filter(IntAve3, filter_window, 2)
noise3 = IntAve3 - IntAve_smoothed3
noise3 = np.nan_to_num(noise3)

Qlist4 = Qlist3
IntAve4 = data3[:, 3]*250000
Qlist5 = Qlist3
IntAve5 = data3[:, 4]*250000
Qlist6 = Qlist3
IntAve6 = data3[:, 5]*250000
Qlist7 = Qlist3
IntAve7 = data3[:, 6]*250000
Qlist8 = Qlist3
IntAve8 = data3[:, 7]*250000
Qlist9 = Qlist3
IntAve9 = data3[:, 8]*250000
Qlist10 = Qlist3
IntAve10 = data3[:, 9]*250000
Qlist11 = Qlist3
IntAve11 = data3[:, 10]*250000
Qlist12 = Qlist3
IntAve12 = data3[:, 11]*250000

IntAve_sum = IntAve3+IntAve4+IntAve5+IntAve6+IntAve7+IntAve8+IntAve9+IntAve10+IntAve11+IntAve12

IntAve_smoothed_sum = savgol_filter(IntAve_sum, filter_window, 2)
noise_sum = IntAve_sum - IntAve_smoothed_sum
noise_sum = np.nan_to_num(noise_sum)

plt.figure(1, (7,9))

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=2)
ax1.plot(Qlist1, IntAve1, label = 'good data')
ax1.plot(Qlist2, IntAve2, label = 'good data 2')
ax1.plot(Qlist3, IntAve3, 'r', label = 'noisy data')
plt.ylabel('Intensity')
plt.xlim(1.7, 3.7)
plt.ylim(700, 1500)
plt.legend(fontsize = 12)

# ax2 = plt.subplot2grid((6,1), (2,0), rowspan=2)
# ax2.plot(Qlist1, IntAve_smoothed1, label = 'smoothed good data')
# ax2.plot(Qlist2, IntAve_smoothed2, label = 'smoothed good data 2')
# ax2.plot(Qlist3, IntAve_smoothed3, label = 'smoothed noisy data')
# plt.ylabel('Smoothed Intensity')
# plt.xlim(1.7, 3.7)
# plt.ylim(700, 1500)
# # plt.legend(fontsize = 12)


ax2 = plt.subplot2grid((6,1), (4,0), rowspan=2)
ax2.plot(Qlist3, IntAve_sum, 'r', label = '10x exposure time')
plt.ylabel('Intensity')
plt.xlabel('Q')
plt.xlim(1.7, 3.7)
plt.ylim(7000, 15000)
plt.legend(fontsize = 12)

ax5 = plt.subplot2grid((6,1), (2,0), rowspan=2)
ax5.plot(Qlist1, noise1, label = 'good data')
ax5.plot(Qlist2, noise2, 'g', label = 'good data 2')
ax5.plot(Qlist3, noise3, 'r', label = 'noisy data')
plt.ylabel('Noise')

# plt.yscale('log')
# plt.legend(fontsize = 12)
plt.xlim(1.7, 3.7)
plt.ylim(-200, 200)

# ax3 = plt.subplot2grid((5,1), (3,0))
# ax3.plot(Qlist1, noise1, label = 'good data')
# plt.ylabel('Noise')
# plt.xlabel('Q')
# plt.legend(fontsize = 12)
# plt.xlim(1.7, 3.7)
# plt.ylim(-200, 200)
#
# ax4 = plt.subplot2grid((5,1), (4,0))
# ax4.plot(Qlist2, noise2, 'g', label = 'good data 2')
# plt.ylabel('Noise')
# plt.xlabel('Q')
# plt.legend(fontsize = 12)
# plt.xlim(1.7, 3.7)
# plt.ylim(-200, 200)

plt.savefig(path+'figure1', dpi = 600)

power_noise1 = np.sum(np.square(noise1))/len(noise1)
power_signal1 = np.sum(np.square(IntAve1))/len(IntAve1)
SNR1 = power_signal1/power_noise1

power_noise2 = np.sum(np.square(noise2))/len(noise2)
power_signal2 = np.sum(np.square(IntAve2))/len(IntAve2)
SNR2 = power_signal2/power_noise2

power_noise3 = np.sum(np.square(noise3))/len(noise3)
power_signal3 = np.sum(np.square(IntAve3))/len(IntAve3)
SNR3 = power_signal3/power_noise3

power_noise_sum = np.sum(np.square(noise_sum))/len(noise_sum)
power_signal_sum = np.sum(np.square(IntAve_sum))/len(IntAve_sum)
SNR_sum = power_signal_sum/power_noise_sum

print SNR1, SNR2, SNR3, SNR_sum
print np.log10(SNR1)*10, np.log10(SNR2)*10, np.log10(SNR3)*10, np.log10(SNR_sum)*10