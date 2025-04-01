def quick_sort(array):
    """
    Sorts an array using the quick sort algorithm.

    This function serves as the entry point for the quick sort algorithm.
    It calls a helper function to perform the sorting recursively.

    Args:
        array (list): The list of elements to be sorted.

    Returns:
        list: The sorted array.
    """
    quick_sort_helper(array, 0, len(array) - 1)
    return array


def quick_sort_helper(array, start, end):
    """
    Recursively sorts the array using the quick sort algorithm.

    This function divides the array into subarrays using a partitioning
    scheme and recursively sorts the subarrays.

    Args:
        array (list): The list of elements to be sorted.
        start (int): The starting index of the current subarray.
        end (int): The ending index of the current subarray.
    """
    if start >= end:
        return
    # Partition the array and get the pivot index
    pivot_index = hoares_partition(array, start, end)
    # Recursively sort the left and right subarrays
    quick_sort_helper(array, start, pivot_index - 1)
    quick_sort_helper(array, pivot_index + 1, end)


def lomutos_partition(array, start, end):
    """
    Partitions the array around a pivot element using Lomuto's scheme.

    The pivot is chosen as the last element of the subarray. Elements smaller
    than the pivot are moved to its left, and elements greater than the pivot
    are moved to its right.

    Args:
        array (list): The list of elements to be partitioned.
        start (int): The starting index of the subarray.
        end (int): The ending index of the subarray.

    Returns:
        int: The final index of the pivot element after partitioning.
    """
    # Use the last element as the pivot
    pivot = array[end]
    i = start - 1
    for j in range(start, end):
        # If the current element is smaller than the pivot, swap it
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    # Place the pivot in its correct position
    array[i + 1], array[end] = array[end], array[i + 1]
    return i + 1


def hoares_partition(array, start, end):
    """
    Partitions the array using Hoare's partitioning scheme.

    The pivot is chosen as the first element of the subarray. Elements smaller
    than the pivot are moved to its left, and elements greater than the pivot
    are moved to its right. This scheme is efficient and minimizes swaps.

    Args:
        array (list): The list of elements to be partitioned.
        start (int): The starting index of the subarray.
        end (int): The ending index of the subarray.

    Returns:
        int: The final index of the pivot element after partitioning.
    """
    pivot = array[start]
    i = start + 1
    j = end
    while i <= j:
        # Move i to the right until an element >= pivot is found
        if array[i] < pivot:
            i += 1
        # Move j to the left until an element <= pivot is found
        elif array[j] > pivot:
            j -= 1
        else:
            # Swap elements at i and j
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    # Place the pivot in its correct position
    array[start], array[j] = array[j], array[start]
    return j


# Test cases
if __name__ == "__main__":
    # Test case 1: Unsorted array
    test_array1 = [64, 25, 12, 22, 11]
    # Test case 2: Another unsorted array
    test_array2 = [5, 3, 8, 6, 2]
    # Test case 3: Already sorted array
    test_array3 = [1, 2, 3, 4, 5]
    # Test case 4: Small array with two elements
    test_array4 = [5, 3]
    # Test case 5: Single-element array
    test_array5 = [53]

    # Print original and sorted arrays for each test case
    print("Original:", test_array1)
    print("Sorted:", quick_sort(test_array1))

    print("Original:", test_array2)
    print("Sorted:", quick_sort(test_array2))

    print("Original:", test_array3)
    print("Sorted:", quick_sort(test_array3))

    print("Original:", test_array4)
    print("Sorted:", quick_sort(test_array4))

    print("Original:", test_array5)
    print("Sorted:", quick_sort(test_array5))
