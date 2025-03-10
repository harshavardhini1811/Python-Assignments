def print_odd_even(n):
    print("Even numbers:")
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i, end=" ")
    
    print("\nOdd numbers:")
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i, end=" ")
num = int(input("Enter a positive integer: "))
print_odd_even(num)