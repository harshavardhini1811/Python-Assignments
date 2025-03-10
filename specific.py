def contains_value(arr, target):
    return target in arr
numbers = [19, 256, 30, 90, 100]
target = int(input("Enter the number to search: "))

if contains_value(numbers, target):
    print(f"{target} is in the array.")
else:
    print(f"{target} is not in the array.")