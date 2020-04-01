#!/usr/bin/env python3

import argparse


def parse_args():
    """Get cli args"""
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', metavar="filename",
                        help="Path to the FES file to be projected")
    parser.add_argument("-T", "--temp", metavar="temp",
                        help="Temperature (in units of the FES file)",
                        required=True)
    parser.add_argument("-d", "--dim", metavar="projectdim",
                        help="Dimension on which should be projected\
                              (given as column number of the FES file)",
                        required=True)
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    # define some constants and values
    print(parse_args())
