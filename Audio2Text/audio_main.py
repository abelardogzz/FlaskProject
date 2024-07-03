import os
import numpy as np


fname = "audio.m4a"

with open(fname) as file:
    print(file.name)
    np_arr = np.frombuffer(file.buffer)
