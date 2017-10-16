#!/usr/bin/env python3
import psutil
import time
import csv
import sys

# use psutil or top
# just for cpu mem_virtual mem_swap net

"""
import os
# Return CPU temperature as a character string
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

# Return % of CPU used by user as a character string
def getCPUuse():
    return(str(os.popen("top -n1 | awk '/top \- / {print $3} /Cpu\(s\):/ {print $2}'").readline().strip(\
)))
"""


def get_time():
    #timestamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    cpu_time = time.time()
    return cpu_time

# cpu


def get_cpu_usage():
    cpu_usage = psutil.cpu_percent()
    return cpu_usage

'''
def get_mem_virtual_usage():
    memory = psutil.virtual_memory()
    available = memory.available
    
    memory = psutil.virtual_memory()
    total = memory.total
    available = memory.available
    percent = memory.percent
    used = memory.used
    free = memory.free
    active = memory.active
    inactive = memory.inactive
    buffers = memory.buffers
    cached = memory.cached
    shared = memory.shared
    return available
 '''

# mem virtual


def get_mem_virtual_total():
    return psutil.virtual_memory().total


def get_mem_virtual_free():
    return psutil.virtual_memory().free


def get_mem_virtual_available():
    return psutil.virtual_memory().available


def get_mem_virtual_used():
    return psutil.virtual_memory().used


def get_mem_virtual_percent():
    return psutil.virtual_memory().percent

# mem swap


def get_mem_swap_total():
    return psutil.swap_memory().total


def get_mem_swap_free():
    return psutil.swap_memory().free


def get_mem_swap_used():
    return psutil.swap_memory().used


def get_mem_swap_percent():
    return psutil.swap_memory().percent

# net


def get_net_bytes_sent():
    return psutil.net_io_counters(pernic=False).bytes_sent


def get_net_bytes_recv():
    return psutil.net_io_counters(pernic=False).bytes_recv


def get_net_packets_sent():
    return psutil.net_io_counters(pernic=False).packets_sent


def get_net_packets_recv():
    return psutil.net_io_counters(pernic=False).packets_recv

# server_138 client135 client137
filename = '/home/wanbo/measure/data/metadata_cpu/' + \
    time.strftime('%Y%m%d%H%M', time.localtime()) + '_cpu.csv'
csvfile = open(filename, 'a')
writer = csv.writer(csvfile, dialect='excel')
'''
writer.writerow(['cpu_us[%]', 'timestamp', 'mem_total[MiB]', 'mem_free[MiB]',
                 'mem_used[MiB]', 'mem_available', 'mem_swap_total[MiB]', 'mem_swap_free[MiB]', 'mem_swap_used[MiB]', 'mem_swap_percent[%]'])
'''

while True:
    writer.writerow(['%f' % (get_time()), 1, '%f' %
                     (get_cpu_usage()), '%f' % (get_mem_virtual_percent())])
    time.sleep(1)

csvfile.close()
