# This problem was asked by Amazon.

# Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.

# For example, for the input [1, 2, 3, 10], you should return 7.

# Do this in O(N) time.

def find_smallest_positive(arr):
    result = 1

    for num in arr:
        # If the current element is less than or equal to the result, update result
        if num <= result:
            result += num
        else:
            # If the current element is greater than result, stop the iteration
            break

    return result

input_array = [1, 2, 3, 10]
output = find_smallest_positive(input_array)
print(output)  # Output: 7