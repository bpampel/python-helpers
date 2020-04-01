#!/usr/bin/env/python3
from multiprocessing import Pool
import glob
import os
import numpy as np

def get_fesfiles(directory):
    """
    Returns the names of all fes files sorted by time and the respective times

    Arguments
    ---------
    directory : base directory of the files

    Returns
    -------
    A tuple of two elements
    files   : a list of all filenames sorted by increasing time
    times   : a list of the respective times of the files
    """
    files = [os.path.basename(f) for f in glob.glob(directory + "fes.b1.iter*")]
    times = [extract_time(f) for f in files]
    files = [i for _, i in sorted(zip(times, files))]
    times = sorted(times)
    return (files, times)

def extract_time(x):
    """
    Get time from filename of fes file

    Arguments
    ---------
    x : name of fes file

    Returns
    -------
    time : int
    """
    return int(''.join(i for i in x if i.isdigit())[1:])

def do_stuff(filename):
    fes = np.genfromtxt(filename)
    return np.average(fes)

avg = np.ndarray(shape=(21))
directory = "/home/benjamin/Downloads/testdata/1/"
filenames, _ = get_fesfiles(directory)
filenames = [directory + f for f in filenames]
pool = Pool(processes=3)
avg = pool.map(do_stuff,filenames)
print(avg)
