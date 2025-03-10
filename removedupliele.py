def remove_duplicates(arr):
    seen = set()
    unique_list = []
    for item in arr:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list
numbers = [1, 2, 3, 2, 4, 1, 5, 6, 4]
result = remove_duplicates(numbers)
print("Array with duplicates removed:",result)