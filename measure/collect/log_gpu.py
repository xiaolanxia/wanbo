#!/usr/bin/env python3
import sys
import time
import csv
import re
import subprocess
import os
# gpu_util gpu_mem
'''
gpu_save_filename = '/home/wanbo/data/%s_gpu.csv' % (
    time.strftime('%Y%m%d%H%M', time.localtime()))
'''
gpu_save_filename = '/home/wanbo/data/gpu_metadata.csv'

with open(gpu_save_filename, "a", newline="") as datacsv:
    csvwriter = csv.writer(datacsv, dialect=("excel"))
    command = "nvidia-smi --query-gpu=timestamp,index,name,utilization.gpu,utilization.memory,temperature.gpu --format=csv"
    command2 = "nvidia-smi dmon -s t -c 1"
    while 1:
        i = 1
        #output = os.popen(command)
        output = subprocess.check_output(
            command, shell=True, universal_newlines=True)
        output2 = subprocess.check_output(
            command2, shell=True, universal_newlines=True)
        info = output.splitlines()
        info2 = output2.splitlines()
        if not(os.path.exists(gpu_save_filename) and os.path.isfile(gpu_save_filename)):
            with open(gpu_save_filename, "a", newline="") as datacsv:
                while i < len(info):
                    str1 = re.split(', |%, ', info[i].strip())
                    str2 = info2[i + 1].strip().split()
                    timestamp = str1[0]
                    gpu_id = str1[1]
                    gpu_name = str1[2]
                    gpu_util = str1[3]
                    gpu_memory_util = str1[4]
                    gpu_temperature = str1[5]
                    gpu_pci_rx = str2[1]
                    gpu_pci_tx = str2[2]
                    try:
                        csvwriter = csv.writer(datacsv, dialect=("excel"))
                        csvwriter.writerow(
                            [timestamp, 1, gpu_id, gpu_name, gpu_util])
                        csvwriter.writerow(
                            [timestamp, 2, gpu_id, gpu_name, gpu_memory_util])
                        csvwriter.writerow(
                            [timestamp, 3, gpu_id, gpu_name, gpu_temperature])
                        csvwriter.writerow(
                            [timestamp, 4, gpu_id, gpu_name, gpu_pci_rx])
                        csvwriter.writerow(
                            [timestamp, 5, gpu_id, gpu_name, gpu_pci_tx])
                    except:
                        pass
                    i += 1
        else:
            while i < len(info):
                str1 = re.split(', |%, ', info[i].strip())
                str2 = info2[i + 1].strip().split()
                timestamp = str1[0]
                gpu_id = str1[1]
                gpu_name = str1[2]
                gpu_util = str1[3]
                gpu_memory_util = str1[4]
                gpu_temperature = str1[5]
                gpu_pci_rx = str2[1]
                gpu_pci_tx = str2[2]
                try:
                    csvwriter = csv.writer(datacsv, dialect=("excel"))
                    csvwriter.writerow(
                        [timestamp, 1, gpu_id, gpu_name, gpu_util])
                    csvwriter.writerow(
                        [timestamp, 2, gpu_id, gpu_name, gpu_memory_util])
                    csvwriter.writerow(
                        [timestamp, 3, gpu_id, gpu_name, gpu_temperature])
                    csvwriter.writerow(
                        [timestamp, 4, gpu_id, gpu_name, gpu_pci_rx])
                    csvwriter.writerow(
                        [timestamp, 5, gpu_id, gpu_name, gpu_pci_tx])
                except:
                    pass
                i += 1

        time.sleep(1)
