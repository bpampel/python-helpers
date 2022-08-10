#!/usr/bin/env python3
"""Small script for lineplots with matplotlib"""


import matplotlib.pyplot as plt


def plot_data(
    xvals,
    yvals,
    styles="",
    func_labels=None,
    xlabel=None,
    ylabel=None,
    legend_title=None,
    filename=None,
):
    """Simple plot function

    xvals and yvals can be either simple lists of values to plot a single function
    or they can be lists of lists with each list being a function to plot.

    If only one list of xvals is specified it is used for all yvals

    This currently doesn't check if all lengths match,
    expect errors if e.g. the "plot_labels" list is shorter than the xvals list

    param xvals: x values of functions
    param yvals: y values of functions
    param styles: specify color and other properties passed to plot for each function
    param func_labels: labels for the functions
    param ylabel: label for y axis
    param xlabel: label for x axis
    param plot_title: title of plot
    param filename: save to file, if None will try interactive mode
    """
    fig = plt.figure(figsize=(8, 4), dpi=100)
    ax = plt.axes()
    try:
        iter(yvals[0])  # check if xval is list of lists --> multiple functions
        # set default lists of right length if not specified
        try:
            iter(xvals[0])
            if len(yvals) != len(xvals):
                raise ValueError(
                    "Specify either xvals for all yvals or a single list for all"
                )
        except TypeError:  # only one specified, use same for all
            yvals = [yvals] * len(xvals)
        if not styles:
            styles = [""] * len(xvals)
        if not func_labels:
            func_labels = [None] * len(xvals)
        # plot each function
        for i, _ in enumerate(xvals):
            ax.plot(xvals[i], yvals[i], styles[i], label=func_labels[i])
    except TypeError:  # is single function? Not very safe, but works
        ax.plot(xvals, yvals, styles)
    # set other properties
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    if func_labels or legend_title:
        ax.legend(title=legend_title)
    if filename:
        fig.savefig(filename)
    else:
        plt.tight_layout()
        plt.show(block=True)
    plt.close(fig)
