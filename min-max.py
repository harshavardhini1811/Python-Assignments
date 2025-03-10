def find_min_max(arr):
    if not arr:
        return None, None
    minimum = min(arr)
    maximum = max(arr)
    return minimum, maximum
numbers = [15, 22, 8, 19, 31, 7, 12]
min_val, max_val = find_min_max(numbers)
print("Minimum value:", min_val)
print("Maximum value:",max_val)