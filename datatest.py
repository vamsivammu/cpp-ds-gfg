import csv
import sys
from decimal import Decimal
dataset =[]
import tensorflow as tf
x =[0]
def retoutput(x):
    l = list(map(float,x))
    for p in l:
        print(p)
def getfloated(x):
    return list(map(float,x))
n_nodes_hl1=10
n_nodes_hl2 = 6
n_nodes_hl3 = 5
n_classes = 4
#114.7927,0.9973218,0.07271035
hidden_1_layer = {'weights':tf.Variable(tf.random_normal([3, n_nodes_hl1])),
                      'biases':tf.Variable(tf.random_normal([n_nodes_hl1]))}

# hidden_2_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
#                       'biases':tf.Variable(tf.random_normal([n_nodes_hl2]))}

# hidden_3_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
#                       'biases':tf.Variable(tf.random_normal([n_nodes_hl3]))}

output_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl1, n_classes])),
                    'biases':tf.Variable(tf.random_normal([n_classes])),}

saver = tf.train.Saver()
a=0
b=0
c=0
# a = sys.argv[1]
# b = sys.argv[2]
# c = sys.argv[3]

k = [0.2725219,0.9550063,7.7565760]
# retoutput(k)
# p = getfloated(k)
x[0] = k

# def neural_network_model(data):
#     hidden_1_layer = {'weights':tf.Variable(tf.random_normal([3, n_nodes_hl1])),
#                       'biases':tf.Variable(tf.random_normal([n_nodes_hl1]))}

#     hidden_2_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
#                       'biases':tf.Variable(tf.random_normal([n_nodes_hl2]))}

#     hidden_3_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
#                       'biases':tf.Variable(tf.random_normal([n_nodes_hl3]))}

#     output_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])),
#                     'biases':tf.Variable(tf.random_normal([n_classes])),}


#     l1 = tf.add(tf.matmul(data,hidden_1_layer['weights']), hidden_1_layer['biases'])
#     l1 = tf.nn.relu(l1)

#     l2 = tf.add(tf.matmul(l1,hidden_2_layer['weights']), hidden_2_layer['biases'])
#     l2 = tf.nn.relu(l2)

#     l3 = tf.add(tf.matmul(l2,hidden_3_layer['weights']), hidden_3_layer['biases'])
#     l3 = tf.nn.relu(l3)

#     output = tf.matmul(l3,output_layer['weights']) + output_layer['biases']

#     return output
# x = [[0.7077,0.7077,30]]
#velocity.x velocity.z angularvelocity.y angle unitvector.x unitvector.y distance  

with tf.Session() as sess:
    
    saver.restore(sess,"D:/cpp-ds-gfg/ckpts/m12.ckpt")
    l1w = sess.run(hidden_1_layer['weights'])
    l1b = sess.run(hidden_1_layer['biases'])
#     l2w = sess.run(hidden_2_layer['weights'])
#     l2b = sess.run(hidden_2_layer['biases'])
#     l3w = sess.run(hidden_3_layer['weights'])
#     l3b = sess.run(hidden_3_layer['biases'])
    l4w = sess.run(output_layer['weights'])
    l4b = sess.run(output_layer['biases'])
        
    l1 = tf.add(tf.matmul(x,l1w), l1b)
    l1 = tf.nn.relu(l1)
#     print(l1w)
    
#     print("\n")
#     print(l1b)
#     print("\n")
#     print(l2w)
    
#     print("\n")
#     print(l2b)
    
#     print("\n")
#     print(l3w)
    
#     print("\n")
#     print(l3b)
    
#     print("\n")
#     print(l4w)
    
#     print("\n")
#     print(l4b)

#     l2 = tf.add(tf.matmul(l1,l2w), l2b)
#     l2 = tf.nn.relu(l2)

#     l3 = tf.add(tf.matmul(l2,l3w), l3b)
#     l3 = tf.nn.relu(l3)

    output = tf.matmul(l1,l4w) + l4b
    o = sess.run(output)
    
    retoutput(o[0])
