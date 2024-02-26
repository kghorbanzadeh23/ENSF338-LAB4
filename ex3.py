import sys
import timeit
import matplotlib.pyplot as plt

"""
1)
The strategy used to grow arrays when they are full in this implementation is
based on a proportional over-allocation scheme. This scheme ensures that there
is room for additional growth without requiring frequent reallocations.
The growth factor is approximately 1.125, or 9/8.

new_allocated = ((size_t)newsize + (newsize >> 3) + 6) & ~(size_t)3;

Here, 'newsize' is the desired new size of the list. The expression 'newsize
>> 3' calculates 1/8th of 'newsize', providing the proportional over-allocation.
Adding 6 to '(newsize >> 3)' ensures that there's always a minimum growth even if
'newsize' is small. Finally, '& ~(size_t)3' ensures that the allocated size is a multiple
of 4, which is a common optimization for memory alignment purposes.

if (newsize - Py_SIZE(self) > (Py_ssize_t)(new_allocated - newsize))
    new_allocated = ((size_t)newsize + 3) & ~(size_t)3;
This check ensures that if the new size is significantly
closer to the over-allocated size than to the old size,
the over-allocation is reduced to avoid excessive waste of memory.

5)
By comparing the histograms, we can observe whether there are significant
differences in the time taken for these operations. If there are differences,
they may be attributed to variations in memory allocation strategies or other
factors that influence list resizing in Python. For instance, appending an element
when the list size changes from S-1 to S may involve a different memory allocation
pattern compared to appending an element when the list size changes from S to S+1,
leading to differences in execution time.

"""
def test_list_capacity():
    lst = []
    capacity = -1
    for i in range(64):
        lst.append(i)
        new_capacity = sys.getsizeof(lst)
        if new_capacity != capacity:
            print(f"Capacity changed at size {len(lst)}: {new_capacity} bytes")
            capacity = new_capacity

def measure_growth_time(S):
    # Define a function to create a list of size S
    def create_list(S):
        return [None] * S

    # Define setup code for timeit
    setup_code = f"""
import sys

# Define a function to create a list of size S
def create_list(S):
    return [None] * S

# Define the largest array size S
S = {S}
    """

    # Define statement for timeit for growing array from size S-1 to S
    stmt_growth_S_minus_1_to_S = """
# Create a list of size S-1
lst = create_list(S-1)

# Append one element to the list
lst.append(None)
    """

    # Measure the time it takes to grow the array from size S-1 to S, repeated 1000 times
    time_taken_S_minus_1_to_S = timeit.timeit(stmt=stmt_growth_S_minus_1_to_S, setup=setup_code, number=1000)

    # Define statement for timeit for growing array from size S to S+1
    stmt_growth_S_to_S_plus_1 = """
# Create a list of size S
lst = create_list(S)

# Append one element to the list
lst.append(None)
    """

    # Measure the time it takes to grow the array from size S to S+1, repeated 1000 times
    time_taken_S_to_S_plus_1 = timeit.timeit(stmt=stmt_growth_S_to_S_plus_1, setup=setup_code, number=1000)

    return time_taken_S_minus_1_to_S, time_taken_S_to_S_plus_1

def plot_distribution(data, title):
    plt.hist(data, bins=20, color='blue', alpha=0.7)
    plt.title(title)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency')
    plt.show()

if __name__ == "__main__":
    print("Testing list capacity:")
    test_list_capacity()

    # Replace S with the desired array size
    S = 64
    print(f"\nMeasuring growth time for array size S={S}:")
    time_taken_S_minus_1_to_S = []
    time_taken_S_to_S_plus_1 = []
    for _ in range(1000):
        time_S_minus_1_to_S, time_S_to_S_plus_1 = measure_growth_time(S)
        time_taken_S_minus_1_to_S.append(time_S_minus_1_to_S)
        time_taken_S_to_S_plus_1.append(time_S_to_S_plus_1)

    plot_distribution(time_taken_S_minus_1_to_S, 'Distribution of time taken to grow from S-1 to S')
    plt.clf()
    plot_distribution(time_taken_S_to_S_plus_1, 'Distribution of time taken to grow from S to S+1')
