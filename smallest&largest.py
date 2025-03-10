def find_smallest_largest(a, b):
    smallest = min(a, b)
    largest = max(a, b)

    print("smallest number:", smallest)
    print("largest number:", largest)

x = int(input("enter a first number:"))
y = int(input("enter a second number:"))
find_smallest_largest(x, y)    