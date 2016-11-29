import PySide
import pyqtgraph as pg
import glob
import numpy as np
from scipy import signal
# import peakutils
# import peakdetect

wavelet = signal.ricker # wavelet of choice
widths = np.arange(1, 20) # range of widths of the ricker wavelet to search/evaluate
max_distances = widths / 8. # ridgeline connectivity threshold; smaller values gives more peaks; larger values considers overlapping peaks as one
gap_thresh = 4 # threshold number of rows for ridgeline connectivity; smaller values gives more peaks
min_length = 3 # minimum ridgeline length; smaller values gives more peaks
min_snr = 2 # Minimum SNR
noise_perc = 10 # percentile of points below which to consider noise
h = 15 # number of points skipped in finite differences
truncationlow = 10 # low q truncation for zeros
truncationhigh = 50 # high q truncation for zeros


def loaddata(path='C:\Research_FangRen\Data\July2016\Sample1\\Processed_old\\'):
    files = path + 'Sample1_24x24_t30_0001_1D.csv'
    data = [np.loadtxt(f,delimiter=',') for f in files]
    return data

def truncate(x,y):
    return x[truncationlow:-truncationhigh],y[truncationlow:-truncationhigh]

def findpeaksCWT(spectra):
    return signal.find_peaks_cwt(spectra,widths,wavelet,max_distances,gap_thresh,min_length,min_snr,noise_perc)

def findpeaksUTILS(spectra):
    return peakutils.indexes(spectra,thres=.001/max(spectra),min_dist=100)

def findpeaksMATLAB(spectra):
    return map(int,peakdetect.peakdet(spectra,max(spectra)/1000)[0][:,0])



def filterpeaks(peaks,spectra,window=h):
    newpeaks=[]
    for peak in peaks:


        filter = np.nan_to_num(np.sqrt(-(spectra[2*h:]-2*spectra[h:-h]+spectra[0:-2*h])))
        filterwindow = filter[max(peak-h - window, 0):min(peak-h + window, len(filter))]
        spectrawindow = spectra[max(peak - window, h):min(peak + window, len(filter))]


        try:
            if np.any(filterwindow>spectrawindow/200): # np.percentile(filter,85) is also a good threshold
                newpeaks.append(peak)
        except ValueError:
            continue

    return newpeaks

def filtersavgol(spectra):
    return signal.savgol_filter(spectra,11,2)

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filtfilt(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = signal.filtfilt(b, a, data)
    return y

if __name__ == '__main__':
    data = loaddata()
    verbose = False

    for d in data:
        x,y=truncate(*d.T)

        if verbose: p = pg.plot()
        if verbose: p.plot(x,y)
        peaks = findpeaksCWT(y)
        if verbose: p.plot(x[peaks],y[peaks],symbol='s',pen=None)

        # p = pg.plot()
        # p.plot(x,y)
        # peaks = findpeaksUTILS(y)
        # p.plot(x[peaks], y[peaks], symbol='s', pen=None, symbolBrush=pg.mkBrush(color='r'))
        #
        # p = pg.plot()
        # p.plot(x,y)
        # peaks = findpeaksMATLAB(y)
        # print peaks
        # p.plot(x[peaks], y[peaks], symbol='s', pen=None, symbolBrush=pg.mkBrush(color='g'))
        #
        # p = pg.plot()
        # p.plot(x, y)

        # p.plot(x[h:-h],200*np.nan_to_num(np.sqrt(-(y[2*h:]-2*y[h:-h]+y[0:-2*h]))),pen=pg.mkPen(color='r'))

        peaks = findpeaksCWT(y)
        peaks = filterpeaks(peaks,y)
        if verbose: p.plot(x[peaks], y[peaks], symbol='s', pen=None, symbolBrush=pg.mkBrush(color='w'))

        # filteredy = butter_lowpass_filtfilt(y,1500,50000)

        filteredy = filtersavgol(y)
        peaks = filterpeaks(peaks, filteredy)
        print peaks
        if verbose: p.plot(x[peaks], y[peaks], symbol='s', pen=None, symbolBrush=pg.mkBrush(color='g'))
        if verbose: p.plot(x,filteredy,pen=pg.mkPen('r'))

    PySide.QtGui.QApplication.instance().exec_()