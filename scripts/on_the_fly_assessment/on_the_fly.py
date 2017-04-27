# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13

@author: fangren

"""

import os.path
import time
import numpy as np
import random
import sys
# import modules
from image_loader import load_image
from data_reduction_smooth import data_reduction
from save_Qchi import save_Qchi
from save_1Dplot import save_1Dplot
from save_1Dcsv import save_1Dcsv
from extract_max_ave_intensity import extract_max_ave_intensity
from extract_peak_number import extract_peak_num
from add_feature_to_master import add_feature_to_master
from save_texture_plot_csv import save_texture_plot_csv
from extract_texture_extent import extract_texture_extent
from nearest_neighbor_cosine_distances import nearst_neighbor_distance
from extract_signal_to_noise_ratio import extract_SNR

def file_index(index):
    """
    formatting the index of each file to make it into a four digit string
    for example, if the index is 1, it will beoomes '0001'. If the index is 100, it will become '0100'
    """
    if len(str(index)) == 1:
        return '000' + str(index)
    elif len(str(index)) == 2:
        return '00' + str(index)
    elif len(str(index)) == 3:
        return '0' + str(index)
    elif len(str(index)) == 4:
        return str(index)


def on_the_fly(folder_path, base_filename, index, last_scan, d_in_pixel, Rotation_angle, tilt_angle, lamda,
               x0, y0, PP, num_of_smpls_per_row, extract_Imax_Iave_ratio_module, extract_texture_module,
               extract_signal_to_noise_module, extract_neighbor_distance_module, add_feature_to_csv_module,
               attribute1=[['scan#', 'Imax', 'Iave', 'Imax/Iave']],
               attribute2=[['scan#', 'texture_sum']],
               attribute3=[['scan#', 'peak_num']],
               attribute4=[['scan#', 'neighbor_distance']],
               attribute5= [['scan#', 'SNR']]):
    """
    run when starting to collect XRD images, and finish when finishing measuring the whole library
    """
    # initializing parameters  # distance from sample to detector plane along beam direction in pixel space
    Rot = (np.pi * 2 - Rotation_angle) / (2 * np.pi) * 360  # detector rotation
    tilt = tilt_angle / (2 * np.pi) * 360  # detector tilt  # wavelength

    # generate a folder to put processed files
    save_path = os.path.join(folder_path, 'Processed')
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # generate a random series of numbers, in case restart the measurement from the middle, the new master file will not overwrite the previous one
    master_index = str(int(random.random() * 100000000))
    while (index <= last_scan):
        imageFilename = base_filename + file_index(index) + '.tif'
        imageFullname = os.path.join(folder_path, imageFilename)
        print("\r")
        # wait until an image is created, and process the previous image, to avoid crashing
        print 'waiting for image', imageFullname + ' to be created...'
        print("\r")
        sleep = 0
        while not os.path.exists(imageFullname) and sleep < 1000:
            time.sleep(1)
            sleep += 1
            # print 'sleeping'
        if sleep == 1000:
            sys.exit()
        print 'processing image ' + imageFullname
        print("\r")
        while (1):
            try:
                # import image and convert it into an array
                imArray = load_image(imageFullname)

                # data_reduction to generate Q-chi and 1D spectra, Q
                Q, chi, cake, Qlist, IntAve = data_reduction(imArray, d_in_pixel, Rot, tilt, lamda, x0, y0, PP)

                # save Qchi as a plot *.png and *.mat
                save_Qchi(Q, chi, cake, imageFilename, save_path)
                # save 1D spectra as a *.csv
                save_1Dcsv(Qlist, IntAve, imageFilename, save_path)
                # extract composition information if the information is available
                # extract the number of peaks in 1D spectra as attribute3 by default
                newRow3, peaks = extract_peak_num(Qlist, IntAve, index)
                attribute3.append(newRow3)
                attributes = np.array(attribute3)

                # save 1D plot with detected peaks shown in the plot
                save_1Dplot(Qlist, IntAve, peaks, imageFilename, save_path)

                if extract_Imax_Iave_ratio_module == 'on':
                    # extract maximum/average intensity from 1D spectra as attribute1
                    newRow1 = extract_max_ave_intensity(IntAve, index)
                    attribute1.append(newRow1)
                    attributes = np.concatenate((attribute1, attributes), axis=1)

                if extract_texture_module == 'on':
                    # save 1D texture spectra as a plot (*.png) and *.csv
                    Qlist_texture, texture = save_texture_plot_csv(Q, chi, cake, imageFilename, save_path)
                    # extract texture square sum from the 1D texture spectra as attribute2
                    newRow2 = extract_texture_extent(Qlist_texture, texture, index)
                    attribute2.append(newRow2)
                    attributes = np.concatenate((attribute2, attributes), axis=1)

                if extract_neighbor_distance_module == 'on':
                    # extract neighbor distances as attribute4
                    newRow4 = nearst_neighbor_distance(index, Qlist, IntAve, folder_path, save_path, base_filename,
                                                                num_of_smpls_per_row)
                    attribute4.append(newRow4)
                    attributes = np.concatenate((attribute4, attributes), axis=1)

                if extract_signal_to_noise_module == 'on':
                    # extract signal-to-noise ratio
                    newRow5 = extract_SNR(index, IntAve)
                    attribute5.append(newRow5)
                    attributes = np.concatenate((attribute5, attributes), axis=1)

                if add_feature_to_csv_module == 'on':
                    # add features (floats) to master metadata
                    # print attributes.shape
                    add_feature_to_master(attributes, base_filename, folder_path, save_path, master_index, index)

                break
            except (OSError, IOError):
                # The image was being created but not complete yet
                print 'waiting for image', imageFullname + ' to be ready...'
                time.sleep(1)
                sleep += 1
        index += 1  # next file




