def find_common_values(arr1, arr2):
    return list(set(arr1) & set(arr2))

# Example usage:
array1 = [1, 2, 3, 4, 5]
array2 = [4, 5, 6, 7, 8]

common = find_common_values(array1, array2)
print("Common values:",common)