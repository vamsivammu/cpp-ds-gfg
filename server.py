# #
# #   Hello World server in Python
# #   Binds REP socket to tcp://*:5555
# #   Expects b"Hello" from client, replies with b"World"
# #

# import time
# import zmq as zmq

# context = zmq.Context()
# socket = context.socket(zmq.REP)
# socket.bind("tcp://*:5555")

# while True:
#     #  Wait for next request from client
#     message = socket.recv()
#     print("Received request: %s" % message)

#     #  Do some 'work'.
#     #  Try reducing sleep time to 0.01 to see how blazingly fast it communicates
#     #  In the real world usage, you just need to replace time.sleep() with
#     #  whatever work you want python to do, maybe a machine learning task?
#     time.sleep(1)

#     #  Send reply back to client
#     #  In the real world usage, after you finish your work, send your output here
#     socket.send(b"World")
import csv
inputs = []
outputs=[]
with open('realdata.csv') as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    for row in reader:
        d = list(map(float,row))
        e = [d[4],d[5],d[6]]
        f = [d[0],d[1],d[2],d[3]]
        inputs.append(e)
        outputs.append(f)
print(inputs[0])
print(outputs)