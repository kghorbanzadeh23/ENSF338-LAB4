import timeit
import random
from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

#optimized
def binary_search(arr,target):
    left = 0
    right = len(arr) - 1

    # Adjust the start midpoint if it's within the bounds
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  
#non-optimized
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target if found
    return -1  # Return -1 if the target is not in the list

#4
#Binary is O(log(n))
#Linear is O(n)

#5

vectorSizes = [1000,5000,10000,15000, 20000]
sizes = []
binaryTimes = []
linearTimes = []



for i in vectorSizes:
    arr = sorted([random.randint(1, i*10) for _ in range(i)])  # Create a sorted vector
    target = random.choice(arr)
    sizes += [i for j in range(100)]
    
    tm = timeit.repeat(lambda: binary_search(arr,target), repeat=100, number=1)
    binaryTimes += tm
    print("The average time for Binary search with", i,"inputs is", sum(tm)/len(tm))

    tm = timeit.repeat(lambda: linear_search(arr,target), repeat=100, number=1)
    linearTimes += tm
    print("The average time for Linear search with", i,"inputs is", sum(tm)/len(tm), '\n')


slope, intercept = np.polyfit(sizes, linearTimes, 1)
linevalues = [slope * x + intercept for x in sizes]
plt.scatter(sizes,linearTimes, c='b')
plt.plot(sizes, linevalues, 'b', label="Linear Search")

plt.xlabel('Number of Records')
plt.ylabel('Time')
plt.legend()
plt.title('Linear Times')
plt.savefig('output.4.2.5.1.png')

plt.clf()

def log(x, a, b):
    return a*np.log(x) + b
constants = curve_fit(log, sizes, binaryTimes)
linevalues = [constants[0][0] * np.log(x) + constants[0][1] for x in sizes]
plt.scatter(sizes,binaryTimes, c='r')
plt.plot(sizes, linevalues, 'r', label="Binary Search")

plt.xlabel('Number of Records')
plt.ylabel('Time')
plt.legend()
plt.title('Binary Times')
plt.savefig('output.4.2.5.2.png')