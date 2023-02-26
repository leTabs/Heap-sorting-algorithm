# heap sorting algorithm

def heap_sorting(array):
    proxy_array = []
    for i in range(len(array)):
        # iterate as many time as the items in the array
        proxy_array.append(min(array))
        # find the smallest value and append it to the proxy array
        array.remove(min(array))
        # remove the smallest value from the original array
    array = proxy_array[:]
    # replace the content of the original array with the proxy's
    # the original now has all it's values sorted
    return array

# arrays for testing
all_arrays = [
    [5, 2, 9, 1, 5, 6, 3, 8, 7, 4],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    [4, 2, 5, 4, 1, 3, 5, 6, 2, 3],
    [-10, -5, 0, 3, -2, 8, -6, 1, -4, 7],
    [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    [100000, 500000, 200000, 300000, 150000, 250000, 400000, 450000, 350000, 600000]
]
# testing...
for item in all_arrays:
    print(heap_sorting(item))

# output:
'''
[1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 2, 3, 3, 4, 4, 5, 5, 6]
[-10, -6, -5, -4, -2, 0, 1, 3, 7, 8]
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
[100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000, 600000]
'''
