def remove_duplicates(arr):
    new_arr = []
    seen = set()
    for item in arr:
        if item not in seen:
            new_arr.append(item)
            seen.add(item)
    return new_arr
original_array = [1, 2, 2, 3, 4, 4, 5, 5, 6]
new_array = remove_duplicates(original_array)
print("Original array:", original_array)
print("New array without duplicates:",new_array)