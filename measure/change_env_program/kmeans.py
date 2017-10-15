#!/usr/bin/python3

import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets.samples_generator import make_blobs
from sklearn.datasets.samples_generator import make_circles

import sys

if len(sys.argv) > 1:
    MAX_ITERS = 200
    SHOW_FIG = True
else:
    MAX_ITERS = 200000
    SHOW_FIG = False

K = 4
N = 200

centers = [[-2, -2], [-2, 1.5], [1.5, -2], [2, 1.5]]

#data, features = make_circles(n_samples=200, shuffle=True, noise=0.1, factor=0.4)
data, features = make_blobs(n_samples=N, centers=centers, n_features = 2, cluster_std=0.8, shuffle=False, random_state=42)
print(data)
print(features)

def clusterMean(data, id, num):
    total = tf.unsorted_segment_sum(data, id, num)
    count = tf.unsorted_segment_sum(tf.ones_like(data), id, num)
    return total/count


points = tf.Variable(data)
cluster = tf.Variable(tf.zeros([N], dtype=tf.int64))
centers = tf.Variable(tf.slice(points.initialized_value(), [0, 0], [K, 2]))
repCenters = tf.reshape(tf.tile(centers, [N, 1]), [N, K, 2])
repPoints = tf.reshape(tf.tile(points, [1, K]), [N, K, 2])
sumSqure = tf.reduce_sum(tf.square(repCenters-repPoints), reduction_indices=2)
bestCenter = tf.argmin(sumSqure, axis=1)
change = tf.reduce_any(tf.not_equal(bestCenter, cluster))
means = clusterMean(points, bestCenter, K)

with tf.control_dependencies([change]):
    update = tf.group(centers.assign(means),cluster.assign(bestCenter))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    changed = True
    iterNum = 0
    while (not SHOW_FIG or changed) and iterNum < MAX_ITERS:
        iterNum += 1
        
        [changed, _] = sess.run([change, update])
        [centersArr, clusterArr] = sess.run([centers, cluster])
        #print(clusterArr)
        #print(centersArr)
        sys.stdout.write("\riter = %d" % iterNum)

        if not SHOW_FIG:
            continue
        fig, ax = plt.subplots()
        ax.scatter(data.transpose()[0], data.transpose()[1], marker='o', s=100, c=clusterArr)
        plt.plot()
        plt.show()

print("\nDone.")
