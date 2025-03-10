def find_index(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1
numbers = [10, 20, 30, 40, 50]
target = int(input("Enter the element to search: "))
index = find_index(numbers, target)

if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the array.")