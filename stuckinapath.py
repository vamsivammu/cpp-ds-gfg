from collections import defaultdict
testcases = int(input())

class element:
    def __init__(self,forenode,backnode,cost):
        self.forenode=Node(forenode)
        self.backnode=Node(backnode)
        self.cost= cost
class Node:
    def __init__(self,nodenum):
        self.nodenum = nodenum

for i in range(testcases):
    nodenums = input().split(" ")
    for j in nodenums:
        intnodenum = int(j)
        
    