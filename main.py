"""
Created on Nov 17 2016, last updated 2/28/17
@author: Fang Ren (SSRL)
"""

import imp
run = imp.load_source("on_the_fly", "on_the_fly.py")

# input calibration parameters (make sure the correct calibration is entered)
# the current geometry is consistant with WxDiff software's tilt/rotation geometry
d_in_pixel = 2297.70054207     # distance from sample to detector plane along beam direction in pixel space
Rotation_angle = 5.22807551536  #detector rotation
tilt_angle = 0.00228744837572   # detector tilt
lamda = 0.976  # wavelength
x0 = 1536.04584107     # beam center in pixel-space
y0 = 1537.10895655    # beam center in pixel-space
PP = 0.95   # beam polarization, decided by beamline setup

low_Q_limit = 3.04
high_Q_limit = 3.11

# folder and file info
folder_path = 'P:\\bl11-3\\March2017\\NiFeW3\\db25'  # specify a folder for the software to watch
base_filename = 'db25_F1_03242111_'   # in order for the program to recognize newly created files, the file needs to
                                        # have the same basefile, but the index automatically increases by 1 evertime a new file is created.
                                        # For the current example, the first file is SampleB2_19_24x24_t30_0001, and second SampleB2_19_24x24_t30_0002...
index = 1   # starting from this scan# The program will automatically add digits to make it into four ditigs, for example, 1 will become 0001, 100 will become 0100
last_scan = 1000  # end with this scan#, if not sure, fill in a large number like 1000. the program will exit after sleeping for 1000 seconds
num_of_smpls_per_row = 25 # the number of samples in a row. It is needed if the nearest-neighbor distance module is on.


# turn on/off optional moduels, change the module status to 'on' if want to use them.
# the default module includes: create Qchi plots, Qchi.mat data file, 1D plots, 1D csv files, peak detection.
extract_Imax_Iave_ratio_module = 'off'
extract_texture_module = 'off'
extract_signal_to_noise_module = 'off'
extract_neighbor_distance_module = 'off'   #  this module requires a master file that indicate the positions of the sample in physical space
add_feature_to_csv_module = 'off'


# DO NOT CHANGE ANYTHING FROM HERE
run.on_the_fly(folder_path, base_filename, index, last_scan, d_in_pixel, Rotation_angle, tilt_angle, lamda, x0, y0, PP,
               num_of_smpls_per_row, low_Q_limit, high_Q_limit, extract_Imax_Iave_ratio_module, extract_texture_module, extract_signal_to_noise_module,
               extract_neighbor_distance_module, add_feature_to_csv_module)
