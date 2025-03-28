def selection_srt(array):
    # Iterate through the array
    n = len(array)
    for i in range(n):
        print('Iteration', i + 1, 'of', n)
        print("Current array:", array)
      
        # Assume the current position holds
        # the minimum element
        min_idx = i
        
        # Iterate through the unsorted portion
        # to find the actual minimum
        for j in range(i + 1, n):
            print('j =', j, 'of', n)
            if array[j] < array[min_idx]:
              
                # Update min_idx if a smaller element is found
                min_idx = j
        
        # Move minimum element to its
        # correct position
        array[i], array[min_idx] = array[min_idx], array[i]
    
    return array

# Test cases
if __name__ == "__main__":
    test_array1 = [64, 25, 12, 22, 11]
    test_array2 = [5, 3, 8, 6, 2]
    test_array3 = [1, 2, 3, 4, 5]

    print("Original:", test_array1)
    print("Sorted:", selection_srt(test_array1))

    print("Original:", test_array2)
    print("Sorted:", selection_srt(test_array2))

    print("Original:", test_array3)
    print("Sorted:", selection_srt(test_array3))
