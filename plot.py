#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import math
import sys
import time


header = np.loadtxt(open("data_header.csv","r"),delimiter=", ", dtype=str)

def plotter (usage_stats, title_string):

    items = len(usage_stats)
    date_axes = [ item[0] for item in usage_stats ]
    index = np.arange(items)
    usage = [ int(item[1]) for item in usage_stats ]
    fig, ax = plt.subplots()

    plt.gca().yaxis.grid(True)
    bar_width = 0.35
    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    rects1 = plt.bar(index, usage, bar_width,
                 alpha=opacity,
                 color='b',
                 error_kw=error_config,
                 label='Monthly Usage')
    plt.xticks(index, date_axes, rotation=270)
    plt.title(title_string)
    plt.show()

def aggregate_by_year(data):
    n =0
    yearly_data = []
    length = len(data)
    while True:
        yearly = data[n*12:(n+1)*12]
        total  = sum([ int(item[1]) for item in yearly])
        yearly_data.append([ "{0}-{1}".format(yearly[0][0], yearly[-1][0]) , total ])
        n += 1
        if (n*12 > length):
            break
    return yearly_data

def plotter_5min_monthly():
    data   = np.loadtxt(open("longerThan5minsMonthly.csv","r"),delimiter=", ", dtype=str)
    plotter(data, "Swift script runs(>5 min) by month")

def plotter_unique_monthly():
    data   = np.loadtxt(open("monthlyUniqueScripts.csv","r"),delimiter=", ", dtype=str)
    plotter(data, "Unique scripts run by month")

def plotter_new_user():
    data   = np.loadtxt(open("monthlyNewUser.csv","r"),delimiter=", ", dtype=str)
    plotter(data, "New Swift users by month")


def plotter_5min_yearly():
    data   = np.loadtxt(open("longerThan5minsMonthly.csv","r"),delimiter=", ", dtype=str)
    yearly = aggregate_by_year(data)
    plotter(yearly, "Swift script runs(>5 min) by year")

def plotter_unique_yearly():
    data   = np.loadtxt(open("monthlyUniqueScripts.csv","r"),delimiter=", ", dtype=str)
    yearly = aggregate_by_year(data)
    plotter(yearly, "Unique scripts run by year")

def plotter_new_user_yearly():
    data   = np.loadtxt(open("monthlyNewUser.csv","r"),delimiter=", ", dtype=str)
    yearly = aggregate_by_year(data)
    plotter(yearly, "New Swift users by year")


#plotter_5min_monthly()
#plotter_unique_monthly()
#plotter_new_user()

plotter_5min_yearly()
plotter_unique_yearly()
plotter_new_user_yearly()


exit()
