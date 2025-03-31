def insertion_sort_recursive(array, n):
    if n <= 1:
        return
    insertion_sort_recursive(array, n-1)
    key = array[n - 1]
    j = n - 2
    while j >= 0 and array[j] > key:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = key

def insertion_sort(array):
    n = len(array)
    if n <= 1:
        return array
    
    # # using recursion
    # insertion_sort_recursive(array, n)
    
    # # with 2 for loops
    # for i in range(1, n):
    #     print('--- i: ', i)
    #     key = array[i]
    #     # Initialize j to the index before i
    #     k = i
    #     for j in range(i - 1, -1, -1):
    #         print('j: ', j)
    #         k = j
    #         if key < array[j]:
    #             array[j + 1] = array[j]
    #         else:
    #             break
    #     array[k] = key
    
    # with a for and a while loopd
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    
    return array


# Test cases
if __name__ == "__main__":
    # Test case 1: Unsorted array
    test_array1 = [64, 25, 12, 22, 11]
    # Test case 2: Another unsorted array
    test_array2 = [5, 3, 8, 6, 2]
    # Test case 3: Already sorted array
    test_array3 = [1, 2, 3, 4, 5]

    # Print original and sorted arrays for each test case
    print("Original:", test_array1)
    print("Sorted:", insertion_sort(test_array1))

    print("Original:", test_array2)
    print("Sorted:", insertion_sort(test_array2))

    print("Original:", test_array3)
    print("Sorted:", insertion_sort(test_array3))
