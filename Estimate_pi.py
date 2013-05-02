#!/usr/bin/env python
from __future__ import division
from random import random
"""
Script to simulate rain in a square field. Counting the number of rain drops in the inscribed circle of radius equal to the length of the field. The ratio of the number of drops in the circle to the total number of drops gives $\pi$.
"""


def rain_drop(length_of_field=1):
    """
    Simulate a random rain drop
    """
    return [(.5 - random()) * length_of_field, (.5 - random()) * length_of_field]


def is_point_in_circle(point, length_of_field=1):
    """
    Return True if point is in inscribed circle
    """
    return (point[0]) ** 2 + (point[1]) ** 2 <= length_of_field / 2


def rain(number_of_drops=1000, length_of_field=2, plot=True, format='pdf'):
    """
    Function to throw darts.
    """
    number_of_drops_in_circle = 0
    drops_in_circle = []
    drops_out_of_circle = []
    for k in range(number_of_drops):
        d = (rain_drop(length_of_field))
        if is_point_in_circle(d, length_of_field):
            drops_in_circle.append(d)
            number_of_drops_in_circle += 1
        else:
            drops_out_of_circle.append(d)
    if plot:
        # If the plot option is passed and matplotlib is installed this plots
        import matplotlib.pyplot as plt
        plt.figure()
        plt.xlim(-length_of_field / 2, length_of_field / 2)
        plt.ylim(-length_of_field / 2, length_of_field / 2)
        plt.scatter([e[0] for e in drops_in_circle], [e[1] for e in drops_in_circle], color='blue', label="Drops in circle")
        plt.scatter([e[0] for e in drops_out_of_circle], [e[1] for e in drops_out_of_circle], color='black', label="Drops out of circle")
        plt.legend(loc="center")
        plt.title("%s darts thrown: %s landed in circle, estimating $\pi$ as %s." % (number_of_darts, number_of_drops_in_circle, 4 * number_of_drops_in_circle / number_of_darts))
        plt.savefig("%s_darts.%s" % (number_of_darts, format))

    return [number_of_drops_in_circle, number_of_drops]


if __name__ == "__main__":
    from sys import argv
    number_of_darts = 100
    if len(argv) > 1:
        number_of_darts = eval(argv[1])
    r = rain(number_of_darts, plot=True, format='png')
    # Print to screen:
    print "----------------------"
    print "%s darts thrown" % number_of_darts
    print "pi estimated as:"
    print "\t%s" % (4 * r[0] / r[1])
    print "----------------------"
