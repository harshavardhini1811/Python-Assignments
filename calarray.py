def calculate_average(arr):
    if not arr:
        return 0

    total = sum(arr)
    average = total / len(arr)
    return average
numbers = [10, 20, 30, 40, 50]
avg = calculate_average(numbers)
print("The average of the array is:", avg)