def bubble_sort(array):
    """
    Sorts an array using the bubble sort algorithm.
    
    This implementation includes an optimization to terminate early if the array
    becomes sorted before completing all passes.
    
    Args:
        array (list): The list of elements to be sorted.
    
    Returns:
        list: The sorted list.
    """
    # Get the length of the array
    n = len(array)
    # Initialize the sorted flag to False
    sorted = False
    # Continue looping until no swaps are made
    while sorted == False:
        sorted = True  # Assume the array is sorted
        for j in range(0, n - 1):
            # Swap if the current element is greater than the next element
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                sorted = False  # Set flag to False as a swap was made

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
    print("Sorted:", bubble_sort(test_array1))

    print("Original:", test_array2)
    print("Sorted:", bubble_sort(test_array2))

    print("Original:", test_array3)
    print("Sorted:", bubble_sort(test_array3))
