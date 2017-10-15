#!/usr/bin/env python3
import sys
import time
import csv
import re
import subprocess
import os

#gpu_save_filename = '/home/wanbo/data/gpu_metadata.csv'
gpu_save_filename = time.strftime('%Y%m%d%H%M', time.localtime()) + '_gpu.csv'
with open(gpu_save_filename, "a", newline="") as datacsv:
    csvwriter = csv.writer(datacsv, dialect=("excel"))
    command = "nvidia-smi --query-gpu=timestamp,index,name,utilization.gpu,utilization.memory,memory.used,temperature.gpu --format=csv"
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
                    timestamp = time.mktime(time.strptime(str1[0], '%Y-%m-%d %H:%M:%S'))
                    gpu_index = str1[1]
                    gpu_name = str1[2]
                    gpu_util = str1[3]
                    gpu_memory_util = str1[4]
                    gpu_memory_used = str1[5]
                    gpu_temperature = str1[6]
                    gpu_pci_rx = str2[1]
                    gpu_pci_tx = str2[2]
                    try:
                        csvwriter = csv.writer(datacsv, dialect=("excel"))
                        csvwriter.writerow(
                            [timestamp, gpu_id, gpu_name, gpu_util])
                        csvwriter.writerow(
                            [timestamp, gpu_id, gpu_name, gpu_memory_util])
                        csvwriter.writerow(
                            [timestamp,  gpu_id, gpu_name, gpu_temperature])
                        csvwriter.writerow(
                            [timestamp,  gpu_id, gpu_name, gpu_pci_rx])
                        csvwriter.writerow(
                            [timestamp,  gpu_id, gpu_name, gpu_pci_tx])
                        csvwriter.writerow(
                            [timestamp,  gpu_id, gpu_name, gpu_memory_used])
                    except:
                        pass
                    i += 1
        else:
            while i < len(info):
                str1 = re.split(', |%, ', info[i].strip())
                str2 = info2[i + 1].strip().split()
                timestamp = time.mktime(time.strptime(str1[0], '%Y-%m-%d %H:%M:%S'))
                gpu_index = str1[1]
                gpu_name = str1[2]
                gpu_util = str1[3]
                gpu_memory_util = str1[4]
                gpu_temperature = str1[5]
                gpu_pci_rx = str2[1]
                gpu_pci_tx = str2[2]
                try:
                    csvwriter = csv.writer(datacsv, dialect=("excel"))
                    csvwriter.writerow(
                        [timestamp,  gpu_id, gpu_name, gpu_util])
                    csvwriter.writerow(
                        [timestamp, gpu_id, gpu_name, gpu_memory_util])
                    csvwriter.writerow(
                        [timestamp,  gpu_id, gpu_name, gpu_temperature])
                    csvwriter.writerow(
                        [timestamp,  gpu_id, gpu_name, gpu_pci_rx])
                    csvwriter.writerow(
                        [timestamp,  gpu_id, gpu_name, gpu_pci_tx])
                    csvwriter.writerow(
                        [timestamp,  gpu_id, gpu_name, gpu_memory_used])
                except:
                    pass
                i += 1

        time.sleep(1)
#os.system("nvidia-smi --query-gpu=timestamp,index,utilization.gpu,utilization.memory,memory.used --format=csv -l 1 -f %s" % (gpu_save_filename))
