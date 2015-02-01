#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import math
import sys
import time

data   = np.loadtxt(open("all_usagedata.csv","r"),delimiter=", ", dtype=str)
header = np.loadtxt(open("data_header.csv","r"),delimiter=", ", dtype=str)

def plotter_all (usage_stats):

    items = len(usage_stats)

    date_axes = [ item[0] for item in usage_stats ]
    index = np.arange(items)
    usage = [ item[1] for item in usage_stats ]
    fig, ax = plt.subplots()

    bar_width = 0.35
    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    rects1 = plt.bar(index, usage, bar_width,
                 alpha=opacity,
                 color='b',
                 error_kw=error_config,
                 label='Monthly Usage')
    plt.xticks(index, date_axes, rotation=45)
    plt.show()


def filter(minutes, data):
    filtered = []
    counter = 0
    for item in data:
        #print "{0} {1}".format(counter,item )
        if item[1] != 'NULL' and item[2] != 'NULL':
            start = time.strptime(item[1],"%Y-%m-%d %H:%M:%S")
            end   = time.strptime(item[2],"%Y-%m-%d %H:%M:%S")
            duration = time.mktime(end) - time.mktime(start)
            if duration > (minutes*60):
                #print "Item: ",item," duration: ", duration/60
                foo = list(item)
                foo.append(duration)
                filtered.append(foo)
        counter += 1
    return filtered

def monthly(data):
    longer_than_5mins = filter(5, data)
    usage_by_month = {}
    for item in longer_than_5mins:
        start_time = time.strptime(item[1],"%Y-%m-%d %H:%M:%S")
        key = "{1}/{0}".format(start_time.tm_year, start_time.tm_mon)
        if key in usage_by_month:
            usage_by_month[key] += 1
        else:
            usage_by_month[key] = 1

    cur_year   = int(time.strftime("%Y", time.gmtime()));
    cur_month  = int(time.strftime("%m", time.gmtime()))
    temp       = time.strptime(longer_than_5mins[1][1],"%Y-%m-%d %H:%M:%S")
    index_year = temp.tm_year
    index_month= temp.tm_mon

    out = open('longerThan5minsMonthly.csv', 'w')
    while True:
        key = "{1}/{0}".format(index_year, index_month)
        if key in usage_by_month:
            foo = "{0}, {1}".format(key, usage_by_month[key])
            out.write(foo + "\n");
        if index_month == 12:
            index_month = 1
            index_year  += 1
        else:
            index_month += 1
        if index_year > cur_year and index_month > cur_month :
            break
    out.close()


def filter_by_unique(data):
    filtered = []
    script_ids = set()
    for item in data:
        if item[6] not in script_ids:
            script_ids.add(item[6])
            filtered.append(list(item))
        #else:
    return filtered


def monthly_unique_scripts(data):
    longer_than_5mins = filter_by_unique(data)
    usage_by_month = {}
    for item in longer_than_5mins:
        start_time = time.strptime(item[1],"%Y-%m-%d %H:%M:%S")
        key = "{1}/{0}".format(start_time.tm_year, start_time.tm_mon)
        if key in usage_by_month:
            usage_by_month[key] += 1
        else:
            usage_by_month[key] = 1

    cur_year   = int(time.strftime("%Y", time.gmtime()));
    cur_month  = int(time.strftime("%m", time.gmtime()))
    temp       = time.strptime(longer_than_5mins[1][1],"%Y-%m-%d %H:%M:%S")
    index_year = temp.tm_year
    index_month= temp.tm_mon

    out = open('monthlyUniqueScripts.csv', 'w')
    while True:
        key = "{1}/{0}".format(index_year, index_month)
        if key in usage_by_month:
            foo = "{0}, {1}".format(key, usage_by_month[key])
            out.write(foo + "\n");
        if index_month == 12:
            index_month = 1
            index_year  += 1
        else:
            index_month += 1
        if index_year > cur_year and index_month > cur_month :
            break
    out.close()

def filter_by_user(data):
    filtered = []
    script_ids = set()
    for item in data:
        if item[3] not in script_ids:
            script_ids.add(item[3])
            filtered.append(list(item))
            #print "New user id ", item[3]
#        else:
#            print "Id ", item[3], "present skipping"
    return filtered


def monthly_new_user(data):
    filtered_data = filter_by_user(data)
    usage_by_month = {}
    for item in filtered_data:
        start_time = time.strptime(item[1],"%Y-%m-%d %H:%M:%S")
        key = "{1}/{0}".format(start_time.tm_year, start_time.tm_mon)
        if key in usage_by_month:
            usage_by_month[key] += 1
        else:
            usage_by_month[key] = 1

    cur_year   = int(time.strftime("%Y", time.gmtime()));
    cur_month  = int(time.strftime("%m", time.gmtime()))
    temp       = time.strptime(filtered_data[1][1],"%Y-%m-%d %H:%M:%S")
    index_year = temp.tm_year
    index_month= temp.tm_mon

    out = open('monthlyNewUser.csv', 'w')
    while True:
        key = "{1}/{0}".format(index_year, index_month)
        if key in usage_by_month:
            foo = "{0}, {1}".format(key, usage_by_month[key])
            out.write(foo + "\n");
        if index_month == 12:
            index_month = 1
            index_year  += 1
        else:
            index_month += 1
        if index_year > cur_year and index_month > cur_month :
            break
    out.close()


#monthly(data)
#monthly_unique_scripts(data)
monthly_new_user(data)
#plotter_all()
#plotter_tiling()
exit()
