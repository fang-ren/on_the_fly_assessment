# -*- coding: utf-8 -*-
"""
Created on Nov 17 2016

@author: Fang Ren
"""

import imp
run = imp.load_source("on_the_fly", "on_the_fly.py")

# input calibration parameters (make sure the correct calibration is entered)
d_in_pixel = 2309.54007395     # distance from sample to detector plane along beam direction in pixel space
Rotation_angle = 4.72973064797  #detector rotation
tilt_angle = 0.531406930485   # detector tilt
lamda = 0.9762  # wavelength
x0 = 1034.81496248     # beam center in pixel-space
y0 = 2309.54007395    # beam center in pixel-space
PP = 0.95   # beam polarization, decided by beamline setup

# user input
folder_path = 'C:\Research_FangRen\Data\Metallic_glasses_data\CoZrFe_ternary\Sample1'
base_filename = 'Sample1_24x24_t30_'
index = 2   # starting from this scan#
last_scan = 441  # end with this scan#
num_of_smpls_per_row = 25 # the number of samples in a row

run.on_the_fly(folder_path, base_filename, index, last_scan, d_in_pixel, Rotation_angle, tilt_angle, lamda, x0, y0, PP, num_of_smpls_per_row)
