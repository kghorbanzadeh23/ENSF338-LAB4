import timeit
import random
from matplotlib import pyplot as plt
import numpy as np

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

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target if found
    return -1  # Return -1 if the target is not in the list

#4
#Binary is O(log(n))
#Linear is O(n)

#5

vectorSizes = [1000,1500,2000,2500,3000,3500,4000,4500,5000]
sizes = []
binaryTimes = []
linearTimes = []



for i in vectorSizes:
    arr = sorted([random.randint(1, i*10) for _ in range(i)])  # Create a sorted vector
    target = random.choice(arr)
    sizes.append(np.full((100), i))
    
    tm = timeit.repeat(lambda: binary_search(arr,target), repeat=100, number=1)
    binaryTimes.append(tm)

    tm = timeit.repeat(lambda: linear_search(arr,target), repeat=100, number=1)
    linearTimes.append(tm)



plt.scatter(sizes,linearTimes, c="b", label="Linear Search")

plt.xlabel('Number of Records')
plt.ylabel('Time')
plt.legend()
plt.title('Linear Times')
plt.savefig('output.4.2.5.1.png')

plt.clf()

plt.scatter(sizes,binaryTimes, c="r", label="Binary Search")

plt.xlabel('Number of Records')
plt.ylabel('Time')
plt.legend()
plt.title('Binary Times')
plt.savefig('output.4.2.5.2.png')