"""
Created on Nov 17 2016, last updated 2/28/17
@author: Fang Ren (SSRL)
"""

from on_the_fly import on_the_fly

PP = 0.95   # beam polarization, according to beamline setup. Contact beamline scientist for this number
pixelSize = 79  # detector pixel size, measured in microns

# folder and file info
calibration_file = 'sample_data\\LaB6.calib' # specify the file path for the WxDiff calibration file
folder_path = 'sample_data\\'  # specify a folder for the software to watch
base_filename = 'SampleB2_19_24x24_t30_'   # in order for the program to recognize newly created files, the file needs to
                                        # have the same basefile, but the index automatically increases by 1 evertime a new file is created.
                                        # For the current example, the first file is SampleB2_19_24x24_t30_0001, and second SampleB2_19_24x24_t30_0002...
index = 1   # starting from this scan# The program will automatically add digits to make it into four ditigs, for example, 1 will become 0001, 100 will become 0100
last_scan = 3  # end with this scan#, if not sure, fill in a large number like 1000. the program will exit after sleeping for 1000 seconds
num_of_smpls_per_row = 25 # the number of samples in a row. It is needed if the nearest-neighbor distance module is on.

# turn on/off optional moduels, change the module status to 'on' if want to use them.
extract_Imax_Iave_ratio_module = 'on'      # extract maximum intensity divided by average intensity from each spectrum as a feature
extract_texture_module = 'on'              # extract texture_sum from each spectrum as a feature, and output texture spectra
extract_signal_to_noise_module = 'on'      # extract signal to noise ratio from each spectrum as a feature
extract_neighbor_distance_module = 'off'   #  this module requires a master file that indicate the positions of the sample in physical space, it needs the input "num_of_smpls_per_row"
add_feature_to_csv_module = 'on'  # if there is a master file, the feature will be added to the master file, otherwise, it will write a new file


# DO NOT CHANGE ANYTHING FROM HERE
on_the_fly(folder_path, base_filename, index, last_scan, calibration_file, PP, pixelSize,
               num_of_smpls_per_row, extract_Imax_Iave_ratio_module, extract_texture_module, extract_signal_to_noise_module,
               extract_neighbor_distance_module, add_feature_to_csv_module)
