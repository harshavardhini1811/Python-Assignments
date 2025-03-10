num = int(input("enter a number:"))
remainder = num % 2
match remainder:
    case 0 :
        print("the number is even:")
    case 1:
        print("the number is odd:")    

