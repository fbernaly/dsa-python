def heap_sort(array):
    """
    Perform heap sort on the given array.

    Steps:
    1. Build a max heap from the input array.
    2. Extract elements one by one from the heap and place them at the end of the array.

    Args:
        array (list): The array to be sorted.

    Returns:
        list: The sorted array.
    """
    n = len(array)
    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Move the current root (largest element) to the end
        array[i], array[0] = array[0], array[i]
        # Call heapify on the reduced heap
        heapify(array, i, 0)

    return array


def heapify(array, n, i):
    """
    Ensure the subtree rooted at index i satisfies the max-heap property.

    Args:
        array (list): The array representing the heap.
        n (int): The size of the heap.
        i (int): The index of the root of the subtree to heapify.

    Steps:
    1. Compare the root with its left and right children.
    2. Swap the root with the largest child if necessary.
    3. Recursively heapify the affected subtree.
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if the left child exists and is greater than the root
    if left < n and array[largest] < array[left]:
        largest = left

    # Check if the right child exists and is greater than the largest so far
    if right < n and array[largest] < array[right]:
        largest = right

    # If the largest is not the root, swap and continue heapifying
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


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
    print("Sorted:", heap_sort(test_array1))

    print("Original:", test_array2)
    print("Sorted:", heap_sort(test_array2))

    print("Original:", test_array3)
    print("Sorted:", heap_sort(test_array3))

    print("Original:", test_array4)
    print("Sorted:", heap_sort(test_array4))

    print("Original:", test_array5)
    print("Sorted:", heap_sort(test_array5))
