# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 14:48:10 2016

@author: fangren
"""

import numpy as np
from numpy import genfromtxt
import os.path

def add_feature_to_master(feature, base_filename, folder_path, save_path, master_index):
    """
    add a feature 'feature' to master meta data, feature is in the form of a ziped row
    """
    feature = np.array(feature)
    master_file = os.path.join(folder_path, base_filename +'scan1.csv')
    master_data = genfromtxt(master_file, delimiter=',', skip_header = 1)
    master_data = np.nan_to_num(master_data)
    dimension = np.min((master_data.shape[0], feature.shape[0]))
    #print dimension, master_data[:dimension:].shape, feature[:dimension:].shape
    master_data = np.concatenate((master_data[:dimension:], feature[:dimension:]), axis = 1)
    np.savetxt(os.path.join(save_path, base_filename + master_index + 'master_metadata.csv'), master_data, \
    delimiter=",", header="register#,plate_x,plate_y,Seconds,i0,i1,mon,bstop,Omron,CH6,\
    CH7,TEMP,marccd,ICRxT,OCRxT,ROI1,ROI2,ROI3,ROI4,ROI5,ROI6,ROI7,ROI8,ROI9,\
    ROI10,RIO11,ROI12,ROI13,SWX,CCD1,CTEMP,Timer,pd1,pd2,pd3,pd4,pd5,pd6,pd7,\
    pd8,pd9,pd10,pd11,pd12,pd13,pd14,pd15,pd16,scan#,Imax,Iave,ratio,scan#,texture,scan#,peak_num,scan#, neighbor_distance")