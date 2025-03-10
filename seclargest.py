def second_largest(arr):
    if len(arr) < 2:
        return None
    first = second = None
    for num in arr:
        if first is None or num > first:
            second = first
            first = num
        elif num != first and (second is None or num > second):
            second = num
    return second
numbers = [12, 35, 1, 10, 34, 35, 1]
result = second_largest(numbers)
if result is not None:
    print("The second largest number is:", result)
else:
    print("The array does not have enough distinct elements.")