def counting_sort(array):
    # Get the length of the array
    n = len(array)
    # If the array has 1 or no elements, it's already sorted
    if n <= 1:
        return array

    # Find the maximum value in the array to determine the range of the count array
    max_value = max(array)

    # Initialize the count array with zeros, size is max_value + 1
    count = [0] * (max_value + 1)

    # Count the occurrences of each element in the array
    for i in range(n):
        count[array[i]] += 1

    # Update the count array to store cumulative sums
    for i in range(1, max_value + 1):
        count[i] += count[i - 1]

    # Create an output array to store the sorted elements
    output = [0] * n

    # Build the output array by placing elements in their correct positions
    for i in range(n):
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1  # Decrement the count for the placed element

    # Return the sorted array
    return output


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
    print("Sorted:", counting_sort(test_array1))

    print("Original:", test_array2)
    print("Sorted:", counting_sort(test_array2))

    print("Original:", test_array3)
    print("Sorted:", counting_sort(test_array3))

    print("Original:", test_array4)
    print("Sorted:", counting_sort(test_array4))

    print("Original:", test_array5)
    print("Sorted:", counting_sort(test_array5))
