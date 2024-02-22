import timeit
import random
from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def old_reverse(self):
        newhead = None
        prevNode = None
        for i in range(self.get_size()-1, -1, -1):
            currNode = self.get_element_at_pos(i)
            currNewNode = Node(currNode.data)
            if newhead is None:
                newhead = currNewNode
            else:
                prevNode.next = currNewNode
            prevNode = currNewNode
        self.head = newhead

    def get_size(self):
        return self.size

    def get_element_at_pos(self, index):
        current = self.head
        for i in range(index):
            current = current.next
        
        return current


    #2
    def new_reverse(self):
        current = self.head
        prev = None
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    def push(self, new_data):
        self.size += 1
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def empty(self):
        self.head = None
        self.size = 0
        
data = LinkedList()

vectorSizes = [1000,2000,3000,4000]
new_times = []
old_times = []


for i in vectorSizes:
    for j in range(i):
        data.push(j)
    
    tm = timeit.timeit(lambda: data.new_reverse(), number=100)
    new_times.append(tm/100)

    tm = timeit.timeit(lambda: data.old_reverse(), number=100)
    old_times.append(tm/100)

    data.empty()


slope, intercept = np.polyfit(vectorSizes, new_times, 1)
linevalues = [slope * x + intercept for x in vectorSizes]
plt.plot(vectorSizes, linevalues, 'b')
plt.scatter(vectorSizes,new_times, c="b", label="Improved Times")


plt.xlabel('Number of Records')
plt.ylabel('Time')
plt.legend()
plt.title('Improved Reverse Function')
plt.savefig('output.7.4.1.png')

plt.clf()

def quad(x,a,b):
    return a*np.power(x,2)+ b
constants = curve_fit(quad, vectorSizes, old_times)
linevalues = [constants[0][0] * np.power(x,2)+ constants[0][1] for x in vectorSizes]
plt.plot(vectorSizes, linevalues, 'r')
plt.scatter(vectorSizes,old_times, c="r", label="Old Times")

# Save the plot to a file named output.7.4.png
plt.xlabel('Number of Records')
plt.ylabel('Time')
plt.legend()
plt.title('Old Reverse Function')
plt.savefig('output.7.4.2.png')
