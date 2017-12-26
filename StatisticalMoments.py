# Calculate the first four moments of a random variable, stored in an iterable data type or Pandas data frame
# Also calculate the mean, variance, standard deviation, skewness, and kurtosis of the data set

# Created by Joel Pozin on August 1, 2017

import scipy.stats as stats
from math import sqrt

def moments(rv):
    first = stats.moment(rv, moment=1)
    second = stats.moment(rv, moment=2)
    third = stats.moment(rv, moment=3)
    fourth = stats.moment(rv, moment=4)
    return [first, second, third, fourth]

def mean(rv):
    """Return the mean of the random variable"""
    return moments(rv)[0]

def var(rv):
    """Return the variance of the random variable"""
    mean = mean(rv)
    return moments(rv)[1] - mean**2

def sd(rv):
    """Return the standard deviation of the random variable"""
    return sqrt(var(data))

def skew(rv):
    """Return the skewness of the random variable"""
    moments = moments(rv)
    mean = moments[0]
    sd = sqrt(moments[1] - moments[0]**2)
    third = moments(rv)[2]
    return (third - 3*mean*sd**2 - mean**3) / sd**3

def kurt(rv):
    """Return the kurtosis of the random variable"""
    moments = moments(rv)
    mean = moments[0]
    sd = sqrt(moments[1] - moments[0]**2)
    third = moments[2]
    fourth = moments[3]
    return (fourth - 4*mean*third + 6*mean**2*sd**2 + 3*mean**4) / sd**4
