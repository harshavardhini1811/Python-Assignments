def contains_specified_elements(arr):
    return 12 in arr and 23 in arr
numbers = [10, 12, 14, 23, 45, 67]
if contains_specified_elements(numbers):
    print("The array contains both 12 and 23.")
else:
    print("The array does not contain both 12 and 23.")