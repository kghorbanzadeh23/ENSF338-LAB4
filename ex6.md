1.Compare advantages and disadvantages of arrays vs linked list

The advatages of linked lists is that it is resizable, as well as non-contiguous. However, the bad part about is it is not indexable.
The advantages of an array is that it allows random access, and it has memeory efficiency.On the other hand, it is not sizable, making them less flexible than linked lists. As well as having contiguous memory allocation, which can be challenging to obtain for large arrays, especially in memory-contrained environments.

2.For arrays, we are interested in implementing a replace function
that acts as a deletion followed by insertion. How can this function
be implemented to minimize the impact of each of the standalone
tasks?

In order to implement the impact of a standalone task (deletion and insertion), it would be wise to use a built-in list methods for deletion and insertion. Then, perform the deletion and insertion operation seperatly to minimize the impact of each solution. 

3.Assuming you are tasked to implement a doubly linked list with a
sort function, given the list of sort functions below, state the
feasibility of using each one of them and elaborate why is it
possible or not to use them. 
1. Insertion sort

The Insertion sort is feasible for sorting a doubly linked list. Since the insertion sort is an efficient algortihm for small lists, thus making it suitable for doubly linked where random access is not efficient. 
2. Merge sort

Merge sort is feasible but it is also less straightforward to implement for sortinga doubly linked list. Since, it is a divide and conquer algorithm that recursively divides the list into smaller subset , sorts them, and then merges them back together.

4.Also show the expected complexity for each and how it differs from
applying it to a regular array


Insertion Sort:
double linked list: 
- time complexity: 
  - best case: O(n)
  - Avarage Case: O(n^2)
  - Worst case: O(n^2)

Regular Array:
- time complexity: 
  - best case: O(n)
  - Avarage Case: O(n^2)
  - Worst case: O(n^2)

Merge Sort: 
double linked list: 
- time complexity: 
  - best case: O(n log n)
  - Avarage Case: O(n log n)
  - Worst case: O(n) log n

Regular Array:
- time complexity: 
  - best case: O(n log n)
  - Avarage Case: O(n log n)
  - Worst case: O(n log n)

Although, both insertion and Merge sort are similar in time complexities when applied to regular arays and doubly linked lists. However, the array-based are slightly better because they have better performance. Doubly linked lists offer efficient insertion and deletion operations, making them suitable for insertion sort. However, recursive operations in Merge Sort may lead to more overhead compared to arrays, even though the time complexity remains the same.




