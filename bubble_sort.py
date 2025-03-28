def bubble_sort(array):
    # Get the length of the array
    n = len(array)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted, no need to compare them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
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
