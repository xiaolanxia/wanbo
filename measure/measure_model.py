#!/usr/bin/env python3
import os
import time
import csv
import random
import sys
import threading
'''
readme
running model in different enviroments for collect metada of iter-time, like idle and different gpu/gpu_mem utilization
'''
# program: choose the add-model at random
# MAX_TURNS , total times of running
# MAX_COEFFICIENT, the number of model which runs in paraller
# models, present programs which run for producing metadata
# models_source, programs which run for change enviroment, source program
MAX_TURNS = 500
MAX_COEFFICIENT = 5
models = ['alexnet_benchmark.py',
          'cifar10_train.py', 'mnist_cnn.py', 'mnist_mlp.py']
models_source = ['alexnet_benchmark.py',
                 'cifar10_train.py', 'mnist_cnn.py', 'mnist_mlp.py', 'kmeans.py']

# use parrallel for creating different enviroments


class MyThread(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        os.system("docker run -it -e DEV=10.244.48.45:0 -v /home/wanbo/measure:/home  --workdir /home --rm 10.244.48.135:5000/wanbo_measure:v2 /home/program/change_env_program/%s" % (self.name))


def change_env(coe_array):
    i = 0
    while i < len(coe_array):
        c = coe_array[i]
        while c > 0:
            t1 = MyThread('%s' % (models_source[i]))
            t1.setDaemon(True)
            t1.start()
            c -= 1
        i += 1


def main(argv=None):
    # in different enviroments, every model run MAX_TURNS times in one
    # enviroment
    i = 0
    while i < len(models):
        turn = 0
        # 循环，结合不同model的gpu利用率	修改coe_array
        coe_array = [0, 0, 0, 0, 0]
        for a in range(0, MAX_COEFFICIENT):
            for b in range(0, MAX_COEFFICIENT):
                for c in range(0, MAX_COEFFICIENT):
                    for d in range(0, MAX_COEFFICIENT):
                        for e in range(0, MAX_COEFFICIENT):
                            coe_array = [a, b, c, d, e]
                            change_env(coe_array)
                            while turn < MAX_TURNS:
                                model = models[i]
                                # /home/xxx.py 1 ,present not idle enviroment, add program-running
                                # /home/xxx.py 0 ,present idle enviroment, add program-running
                                '''
                                if coe_array == [0, 0, 0, 0, 0]:
                                    os.system(
                                        "/home/wanbo/measure/program/ML_program/%s 0" % (model))
                                else:
                                    os.system(
                                        "/home/wanbo/measure/program/ML_program/%s 1" % (model))
                                turn += 1
                                '''
                                if coe_array == [0, 0, 0, 0, 0]:
                                    #os.system("/home/wanbo/measure/program/ML_program/%s 0" % (model))
                                    os.system("docker run -it -e DEV=10.244.48.45:0 -v /home/wanbo/measure:/home  --workdir /home --rm 10.244.48.135:5000/wanbo_measure:v2 /home/program/ML_program/%s 0" % (self.name))
                                else:
                                    #os.system("/home/wanbo/measure/program/ML_program/%s 1" % (model))
                                    os.system("docker run -it -e DEV=10.244.48.45:0 -v /home/wanbo/measure:/home  --workdir /home --rm 10.244.48.135:5000/wanbo_measure:v2 /home/program/ML_program/%s 1" % (self.name))
                                turn += 1
        i += 1

if __name__ == '__main__':
    main()
