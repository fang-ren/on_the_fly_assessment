from scipy.signal import savgol_filter
import numpy as np
import matplotlib.pyplot as plt


path = 'C:\\Research_FangRen\\Publications\\on_the_fly_paper\\Sample_data\\'

file2 = path + 'noisy.csv'
file1 = path + 'amorphous.csv'

data1 = np.genfromtxt(file1, delimiter = ',')
Qlist1 = data1[6:940,0]
IntAve1 = data1[6:940,1]
IntAve_smoothed1 = savgol_filter(IntAve1, 15, 2)
noise1 = IntAve1 - IntAve_smoothed1

data2 = np.genfromtxt(file2, delimiter = ',')
Qlist2 = data2[6:940,0]
IntAve2 = data2[6:940,1]*20
IntAve_smoothed2 = savgol_filter(IntAve2, 15, 2)
noise2 = IntAve2 - IntAve_smoothed2

plt.figure(1, (7,7.5))
plt.subplot(411)
plt.plot(Qlist1, IntAve1, label = 'good data')
plt.plot(Qlist2, IntAve2, label = 'noisy data')
plt.ylabel('Intensity')
plt.xlim(0.5, 6)
plt.legend(fontsize = 12)

plt.subplot(412)
plt.plot(Qlist1, IntAve_smoothed1, label = 'smoothed good data')
plt.plot(Qlist2, IntAve_smoothed2, label = 'smoothed noisy data')
plt.ylabel('Intensity')
plt.xlim(0.5, 6)
plt.legend(fontsize = 12)

plt.subplot(413)
plt.plot(Qlist1, noise1, label = 'good data')
plt.ylabel('Noise')
plt.xlabel('Q')
plt.legend(fontsize = 12)
plt.xlim(0.5, 6)

plt.subplot(414)
plt.plot(Qlist2, noise2, 'g', label = 'noisy data')
plt.ylabel('Noise')
plt.xlabel('Q')
plt.legend(fontsize = 12)
plt.xlim(0.5, 6)
plt.savefig(path+'figure1', dpi = 600)

power_noise1 = np.sum(np.square(noise1))/len(noise1)
power_signal1 = np.sum(np.square(IntAve1))/len(IntAve1)
SNR1 = power_signal1/power_noise1

power_noise2 = np.sum(np.square(noise2))/len(noise2)
power_signal2 = np.sum(np.square(IntAve2))/len(IntAve2)
SNR2 = power_signal2/power_noise2

print SNR1, SNR2
print SNR1/SNR2
print np.log10(SNR1)*10, np.log10(SNR2)*10