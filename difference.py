def difference_largest_smallest(arr):
    if not arr:
        raise ValueError("The array is empty.")
    largest = max(arr)
    smallest = min(arr)
    return largest - smallest
numbers = [15, 22, 8, 19, 31, 7, 12]
difference = difference_largest_smallest(numbers)
print("Difference between largest and smallest values:",difference)