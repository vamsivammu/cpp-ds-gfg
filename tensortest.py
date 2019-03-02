import tensorflow as tf
# from tensorflow.examples.tutorials.mnist import input_data
# mnist = input_data.read_data_sets("/tmp/data/", one_hot = True)

import csv
import sys
from decimal import Decimal
outputs =[]
inputs=[]
with open('realdata.csv') as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    for row in reader:
        d = list(map(float,row))
        e = [d[4],d[5],d[6]]
        f = [d[0],d[1],d[2],d[3]]
        inputs.append(e)
        outputs.append(f)
    

n_nodes_hl1 = 5
n_nodes_hl2 = 6
n_nodes_hl3 = 5
print(len(inputs))
import numpy as np

n_classes = 4
batch_size = 1

x = tf.placeholder('float', [None, 3])
wei = tf.constant([[1,1,1,20]])
y = tf.placeholder('float')

def neural_network_model(data):
    hidden_1_layer = {'weights':tf.Variable(tf.random_normal([3, n_nodes_hl1])),
                      'biases':tf.Variable(tf.random_normal([n_nodes_hl1]))}

    # hidden_2_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
    #                   'biases':tf.Variable(tf.random_normal([n_nodes_hl2]))}

    # hidden_3_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
    #                   'biases':tf.Variable(tf.random_normal([n_nodes_hl3]))}

    output_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl1, n_classes])),
                    'biases':tf.Variable(tf.random_normal([n_classes]))}


    l1 = tf.add(tf.matmul(data,hidden_1_layer['weights']), hidden_1_layer['biases'])
    l1 = tf.nn.relu(l1)

    # l2 = tf.add(tf.matmul(l1,hidden_2_layer['weights']), hidden_2_layer['biases'])
    # l2 = tf.nn.relu(l2)

    # l3 = tf.add(tf.matmul(l2,hidden_3_layer['weights']), hidden_3_layer['biases'])
    # l3 = tf.nn.relu(l3)

    output = tf.matmul(l1,output_layer['weights']) + output_layer['biases']

    return output

starter_rate = 0.01
def train_neural_network(x):
    prediction = neural_network_model(x)
    # OLD VERSION:
    # cost = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(logits=prediction,labels=y) )
    # NEW:
    
    los = tf.subtract(prediction,y)
    los = tf.abs(los)

    loss = tf.losses.compute_weighted_loss(los,[[1,1,1,50]])

    # los = tf.losses.compute_weighted_loss(los)
    cost = tf.reduce_mean( loss )
    # a = 10*prediction[:,3]
    # b =[]

    # for i in range(4):
    #     if i==3:
    #         b.append(a)
    #     else:
    #         b.append(prediction[:,i])
    # for i in 

    # c = tf.reduce_mean(tf.losses.)
    global_step = tf.Variable(1, trainable=False)
    learning_rate = tf.train.exponential_decay(starter_rate, global_step,
                                           1000, 0.0001, staircase=True)
    optimizer = tf.train.RMSPropOptimizer(0.001,decay=0.01).minimize(loss)
    
    hm_epochs = 100000
    saver = tf.train.Saver()
    with tf.Session() as sess:
        # OLD:
        #sess.run(tf.initialize_all_variables())
        # NEW:
        sess.run(tf.global_variables_initializer())
            
        for epoch in range(hm_epochs):
            epoch_loss = 0
            
            for _ in range(1):

                # print(epoch_x)
                # print(len(epoch_x[0]))
                # print(len(epoch_y[0]))
                
                # print(epoch_y)
                _, c = sess.run([optimizer, cost], feed_dict={x: inputs, y: outputs})
            
                epoch_loss += c
            if(epoch%1000==0):
                save_path=saver.save(sess,"./ckpts/m13.ckpt")
            
            print('Epoch', epoch, 'completed out of',hm_epochs,'loss:',epoch_loss)
        
        # correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))

        # accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
        # print('Accuracy:',accuracy.eval({x:mnist.test.images, y:mnist.test.labels}))

train_neural_network(x)
