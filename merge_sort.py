def merge_sort(array):
    """
    Sorts an array using the merge sort algorithm.
    
    Args:
        array (list): The list of elements to be sorted.
    
    Returns:
        list: The sorted list.
    """
    n = len(array)
    merge_sort_helper(array, 0, n - 1)
    return array


def merge_sort_helper(array, start, end):
    """
    Recursively divides the array into halves, sorts them, and merges them.
    
    Args:
        array (list): The list of elements to be sorted.
        start (int): The starting index of the current subarray.
        end (int): The ending index of the current subarray.
    """
    if start >= end:
        return
    mid = (start + end) // 2
    merge_sort_helper(array, start, mid)
    merge_sort_helper(array, mid + 1, end)
    i = start
    j = mid + 1
    aux = []
    # Merge the two sorted halves into the auxiliary array.
    while i <= mid and j <= end:
        if array[i] <= array[j]:
            aux.append(array[i])
            i += 1
        else:
            aux.append(array[j])
            j += 1
    while i <= mid:
        aux.append(array[i])
        i += 1
    while j <= end:
        aux.append(array[j])
        j += 1
    # Copy the sorted elements back into the original array.
    for i in range(0, len(aux)):
        array[start + i] = aux[i]


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
    print("Sorted:", merge_sort(test_array1))

    print("Original:", test_array2)
    print("Sorted:", merge_sort(test_array2))

    print("Original:", test_array3)
    print("Sorted:", merge_sort(test_array3))
