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

vectorSizes = [1000,5000,10000,15000,20000]
binaryTimes = []
linearTimes = []

for i in vectorSizes:
    arr = sorted([random.randint(1, i*10) for _ in range(i)])  # Create a sorted vector
    target = random.choice(arr)
    
    tm = timeit.repeat(lambda: binary_search(arr,target), repeat=100, number=1)
    print("The average time for Binary search with", i,"inputs is", sum(tm)/len(tm))

    tm = timeit.repeat(lambda: linear_search(arr,target), repeat=100, number=1)
    print("The average time for Linear search with", i,"inputs is", sum(tm)/len(tm), '\n')

arr = sorted([random.randint(1, 1000*10) for _ in range(1000)])  # Create a sorted vector
target = random.choice(arr)
    
tm = timeit.repeat(lambda: binary_search(arr,target), repeat=100, number=1)
binaryTimes += tm

tm = timeit.repeat(lambda: linear_search(arr,target), repeat=100, number=1)
linearTimes += tm


plt.hist(linearTimes, color='w', edgecolor = 'r',)

plt.xlabel('Time(s)')
plt.ylabel('Frequency')
plt.title('Linear Times')
plt.savefig('output.4.2.5.1.png')

plt.clf()

plt.hist(linearTimes, color='w', edgecolor = 'b',)

plt.xlabel('Time(s)')
plt.ylabel('Frequency')
plt.title('Binary Times')
plt.savefig('output.4.2.5.2.png')