This code is for data reduction and feature extraction for XRD data collected by an area detector.
To use this code, please cite the author (Fang Ren, Apurva Mehta, Ron Pandolfi) in your source code, or the recent paper submitted to ACS Combinatorial Science.


In main.py:

1. specify 'folder_path' and 'base_filename'. For example, if the filename is 'Sample1_24x24_t30_0441.tif',
the base_filename is 'Sample1_24x24_t30_'. The code will start with a 'index' that can be specified in mian.py, 1 by default,
and always look for the next index number. For example, if the analysis starts from 'Sample1_24x24_t30_0001.tif', for which the index is 1,
after finish processing this file, the program will look for 'Sample1_24x24_t30_0002.tif'.
To change the index format, change the 'file_index function' in 'on_the_fly.py'

Fill in calibration parameters. The calibration parameters used here is the same with WxDiff
turn off/on feature extraction modules

Run main.py to start the analysis



