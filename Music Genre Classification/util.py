'''It has function to extract centroid given an array adn its spread.'''
import numpy as np


def centroid(X,bins):
    N=len(X)
    sum=0
    normal=0
    for i in range(N):
        sum+=bins[i]*X[i]
        normal+=X[i]
    return float(sum)/float(normal)


def spread(X,bins,centroid=None):
    if(centroid==None):
        centroid=centroid(X,bins)
    N=len(X)
    var=0
    normal=0
    for i in range(N):
        diff=(bins[i]-centroid)**2
        var+=diff*X[i]
        normal+=X[i]
    return float(var)/normal

