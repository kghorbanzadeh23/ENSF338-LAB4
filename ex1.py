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

    # function to find out middle element
    def middle(self,start, last):

        if (start == None):
            return None

        slow = start
        fast = start.next

        while (fast != last):
        
            fast = fast.next
            if (fast != last):
            
                slow = slow.next
                fast = fast.next
            
        return slow

    #2
    def binarySearch(self, value):
        start = self
        last = None

        while True :
        
            mid = self.middle(start, last)

            if (mid == None):
                return None

            if (mid.data == value):
                return mid

            elif (mid . data < value):
                start = mid.next

            else:
                last = mid

            if not (last == None or last != start):
                break

        return None

def newNode(x):
    temp = Node(0)
    temp.data = x
    temp.next = None
    return temp

#3
class array:
    def __init__(self, startring_array):
        self.data = startring_array
    
    def binary_search(self,target):
        left = 0
        right = len(self.data) - 1

        # Adjust the start midpoint if it's within the bounds
        while left <= right:
            mid = (left + right) // 2

            if self.data[mid] == target:
                return mid
            elif self.data[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1  

#4 The complexity for a linked list is O(N) as you can't really jump to the middle point like you can in an array.
#As in a linked list you have to traverse the list each time to check if a value is at a certain point.
    
linkedTimes = []
arrayTimes = []

vectorSizes = [1000,2000,4000,8000]
for i in vectorSizes:
    arr = array(range(i)) 
    head = newNode(0)
    temp = head
    for k in range(1,i):
        temp.next = newNode(k)
        temp = temp.next

    target = random.randint(0, i - 1)
    tm = timeit.timeit(lambda: arr.binary_search(target), number=20)/20
    arrayTimes.append(tm)

    tm = timeit.timeit(lambda: head.next.binarySearch(target), number=20)/20
    linkedTimes.append(tm)


slope, intercept = np.polyfit(vectorSizes, linkedTimes, 1)
linevalues = [slope * x + intercept for x in vectorSizes]
plt.scatter(vectorSizes,linkedTimes, c='r')
plt.plot(vectorSizes, linevalues, 'r', label="Linked List")


def logn(x,a,b):
    return a*np.log(x) + b
constants = curve_fit(logn, vectorSizes, arrayTimes)
linevalues = [constants[0][0] * np.log(x)+ constants[0][1] for x in vectorSizes]
plt.plot(vectorSizes, linevalues, 'b', label="Array")
plt.scatter(vectorSizes,linkedTimes, c='b')

# Save the plot to a file named output.6.4.png
plt.xlabel('Number of Records')
plt.ylabel('Time')
plt.title('Comparison Between Linked List and Array')
plt.legend()
plt.savefig('output.1.6.png')

