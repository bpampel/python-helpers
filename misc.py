#!/usr/bin/env/python3
import glob
import os


def get_filenames(basedir):
    """
    Returns all numbered folders and fes files sorted by time

    Arguments
    ---------
    basedir : base directory of the search

    Returns
    -------
    A tuple of three elements
    folders : a list of all numbered directories
    files   : a list of all filenames sorted by increasing time
    times   : a list of the respective times of the files
    """
    tmp_folders = glob.glob(basedir + os.path.sep + "[0-9]*" + os.path.sep)
    tmp_files = [os.path.basename(f) for f in glob.glob(tmp_folders[0] + "fes.b1.iter*")]
    tmp_times = [extract_time(f) for f in tmp_files]
    tmp_files = [i for _, i in sorted(zip(tmp_times, tmp_files))]
    tmp_times = sorted(tmp_times)
    return (tmp_folders, tmp_files, tmp_times)


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
