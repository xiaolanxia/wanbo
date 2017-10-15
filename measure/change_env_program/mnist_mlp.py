#!/usr/bin/python3

import pdb

from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

import sys, time

if len(sys.argv) <= 1:
    MAX_ITERS = 10000
else:
    MAX_ITERS = 100000


mnist = input_data.read_data_sets('/tmp/MNIST_data', one_hot=True)

x = tf.placeholder("float", shape=[None, 784])
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x,W) + b)
y_ = tf.placeholder("float", shape=[None, 10])

cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
# train data and get results for batches
init = tf.global_variables_initializer()
sess = tf.Session()

# pdb.set_trace()
sess.run(init)

print()
# train the data
for i in range(MAX_ITERS):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
    sys.stdout.write("\riter = %d" % i)

print("\nDone.")
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

acc = sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels})
print("accuracy =", acc)

prediction=tf.argmax(y,1)
assert(acc >= 0.8 and acc <= 1.0)

#test = [ mnist.test.images[0] ]
#print("images:", test)
#print("predictions", prediction.eval(feed_dict={x: test}, session=sess))
