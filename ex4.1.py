def processdata(li):
    for i in range(len(li)):
        if li[i] > 5:
            for j in range(len(li)):
                li[i] *= 2

#1
#The worst case is O(N^2) as if had to go into the second for loop each time the complexity would be N^2
#The best case is O(N) as if we never touched the for loop we would only go through the loop once making the 
#complexity N.
#The Average case is O(N^2) As on average the amount of times the code is going to search through the array is going to be more than once. 
#In which the operations performed is going to increase quadically.
                
#They are not the same as for example if the entries are all less than 5 it wouldn't even touch the second for loop.
#But if they are greater it would touch the second for loop.
def processdata(li):
    for i in range(len(li)):
            for j in range(len(li)):
                if li[i] > 5:
                    li[i] *= 2
