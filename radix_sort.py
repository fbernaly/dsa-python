def counting_sort(array, exp):
    # Get the length of the array
    n = len(array)
    # If the array has 1 or no elements, it's already sorted
    if n <= 1:
        return array

    # Initialize the count array for digits (0-9)
    count = [0] * 10

    # Count the occurrences of each digit at the current exponent
    for i in range(n):
        index = (array[i] // pow(10, exp)) % 10
        count[index] += 1

    # Update the count array to store cumulative sums
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Create an output array to store the sorted elements
    output = [0] * n

    # Build the output array by placing elements in their correct positions
    for i in range(n - 1, -1, -1):
        # Extract the digit at the current exponent
        index = (array[i] // pow(10, exp)) % 10
        # Place the element in the correct position
        output[count[index] - 1] = array[i]
        # Decrement the count for the placed element
        count[index] -= 1

    # Copy the sorted elements back to the original array
    array = output
    return array


def radix_sort(array):
    # Find the maximum value to determine the number of digits
    max_value = max(array)
    num_digits = len(str(max_value))

    # Perform counting sort for each digit, starting from the least significant digit
    for i in range(num_digits):
        array = counting_sort(array, i)

    # Return the sorted array
    return array


if __name__ == "__main__":
    # Test case 1: Unsorted array
    test_array1 = [64, 25, 12, 22, 11]
    # Test case 2: Another unsorted array
    test_array2 = [5, 23, 28, 106, 102]
    # Test case 3: Already sorted array
    test_array3 = [1, 2, 3, 4, 5]
    # Test case 4: Small array with two elements
    test_array4 = [5, 3]
    # Test case 5: Single-element array
    test_array5 = [53]

    # Print original and sorted arrays for each test case
    print("Original:", test_array1)
    print("Sorted:", radix_sort(test_array1))

    print("Original:", test_array2)
    print("Sorted:", radix_sort(test_array2))

    print("Original:", test_array3)
    print("Sorted:", radix_sort(test_array3))

    print("Original:", test_array4)
    print("Sorted:", radix_sort(test_array4))

    print("Original:", test_array5)
    print("Sorted:", radix_sort(test_array5))
