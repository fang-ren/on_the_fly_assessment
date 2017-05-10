"""
author: Fang Ren (SSRL)

4/27/2017
"""

import numpy as np


def load_image(imageFullname):
    # open MARCCD tiff image
    data = np.fromfile(imageFullname, dtype=np.int32)
    imArray = data.reshape(195, 1475)
    return imArray