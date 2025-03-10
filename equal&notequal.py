def compare_numbers(a, b):
    if a == b:
        print(f"Equal operator (==) returns True: {a} == {b} is True")
    else:
        print(f"Equal operator (==) returns False: {a} == {b} is False")
    
    if a != b:
        print(f"Not equal operator (!=) returns True: {a} != {b} is True")
    else:
        print(f"Not equal operator (!=) returns False: {a} != {b} is False")

# Example usage:
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
compare_numbers(num1,num2)