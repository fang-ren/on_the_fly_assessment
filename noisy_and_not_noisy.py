from scipy.signal import savgol_filter
import numpy as np
import matplotlib.pyplot as plt


path = 'C:\\Research_FangRen\\Publications\\on_the_fly_paper\\Sample_data\\'

file2 = path + 'good_2.csv'
file1 = path + 'amorphous.csv'
file3 = path + 'noisy.csv'

filter_window = 15

data1 = np.genfromtxt(file1, delimiter = ',')
Qlist1 = data1[63:940,0]
IntAve1 = data1[63:940,1]
IntAve_smoothed1 = savgol_filter(IntAve1, filter_window, 2)
noise1 = IntAve1 - IntAve_smoothed1

data2 = np.genfromtxt(file2, delimiter = ',')
Qlist2 = data2[63:940,0]
IntAve2 = data2[63:940,1]*20
IntAve_smoothed2 = savgol_filter(IntAve2, filter_window, 2)
noise2 = IntAve2 - IntAve_smoothed2

data3 = np.genfromtxt(file3, delimiter = ',')
twoTheta3 = data3[:11100,0]
Qlist3 = 4 * np.pi * np.sin(twoTheta3/2/180*np.pi)/1.0781
IntAve3 = data3[:11100,1]*6
IntAve_smoothed3 = savgol_filter(IntAve3, filter_window, 2)
noise3 = IntAve3 - IntAve_smoothed3

plt.figure(1, (7,9))

ax1 = plt.subplot2grid((5,1), (0,0), rowspan=2)
ax1.plot(Qlist3, IntAve3, 'r', label = 'noisy data')
ax1.plot(Qlist1, IntAve1, label = 'good data')
ax1.plot(Qlist2, IntAve2, label = 'good data 2')

plt.ylabel('Intensity')
plt.xlim(1, 6)
plt.legend(fontsize = 12)

# plt.subplot(512)
# plt.plot(Qlist1, IntAve_smoothed1, label = 'smoothed good data')
# plt.plot(Qlist2, IntAve_smoothed2, label = 'smoothed good data 2')
# plt.plot(Qlist3, IntAve_smoothed3, label = 'smoothed noisy data')
# plt.ylabel('Intensity')
# plt.xlim(1, 6)
# plt.legend(fontsize = 12)

ax5 = plt.subplot2grid((5,1), (2,0))
ax5.plot(Qlist3, noise3, 'r', label = 'noisy data')
plt.ylabel('Noise')
plt.xlabel('Q')
plt.legend(fontsize = 12)
plt.xlim(1, 6)
plt.ylim(-80, 80)

ax3 = plt.subplot2grid((5,1), (3,0))
ax3.plot(Qlist1, noise1, label = 'good data')
plt.ylabel('Noise')
plt.xlabel('Q')
plt.legend(fontsize = 12)
plt.xlim(1, 6)
plt.ylim(-80, 80)

ax4 = plt.subplot2grid((5,1), (4,0))
ax4.plot(Qlist2, noise2, 'g', label = 'good data 2')
plt.ylabel('Noise')
plt.xlabel('Q')
plt.legend(fontsize = 12)
plt.xlim(1, 6)
plt.ylim(-80, 80)

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

print SNR1, SNR2, SNR3
print np.log10(SNR1)*10, np.log10(SNR2)*10, np.log10(SNR3)*10