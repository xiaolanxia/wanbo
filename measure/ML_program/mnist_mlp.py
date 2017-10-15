#!/usr/bin/env python3

import pdb
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import sys
import time
import csv

'''
readme
run like this :
	python ./mnist_mlp.py  iters
	it means run iters-times
'''
if len(sys.argv) <= 1:
    MAX_ITERS = 50000
else:
    MAX_ITERS = 50000000

if len(sys.argv) >= 2:
    env = int(sys.argv[1])
else:
    env = 0
# log csv_file
filename = '/home/data/metadata_run_ml/' + 'log_ml.csv'
csvfile = open(filename, 'a')
writer = csv.writer(csvfile, dialect='excel')
#writer.writerow(['timestamp', 'iters[/second]'])

mnist = input_data.read_data_sets('/tmp/MNIST_data', one_hot=True)

x = tf.placeholder("float", shape=[None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W) + b)
y_ = tf.placeholder("float", shape=[None, 10])

cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
# train data and get results for batches
init = tf.global_variables_initializer()
sess = tf.Session()
# pdb.set_trace()
sess.run(init)
print()

time1 = time.time()
time2 = time1
iter_temp1 = 1
# train the data
for i in range(MAX_ITERS):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
    sys.stdout.write("\riter = %d" % i)

    time2 = time.time()
    if time.time() - time2 > 1:
        time2 = time.time()
        iter_interval = i - iter_temp1
        iter_temp1 = i
        writer.writerow(['%f' % (time.time()), 1, '%f' %
                         (iter_interval), 1, env])

print("\nDone.")
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

acc = sess.run(accuracy, feed_dict={
               x: mnist.test.images, y_: mnist.test.labels})
print("accuracy =", acc)

prediction = tf.argmax(y, 1)
assert(acc >= 0.8 and acc <= 1.0)

# test = [ mnist.test.images[0] ]
# print("images:", test)
# print("predictions", prediction.eval(feed_dict={x: test}, session=sess))

total_time = time.time() - time1
timestamp = time.time()
#writer.writerow(['timestamp', 'training_iters', 'total_time'])
writer.writerow(['%f' % (timestamp), 2, '%f' %
                 (MAX_ITERS), '%f' % (total_time), env])
csvfile.close()
