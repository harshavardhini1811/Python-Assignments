gender = input("enter your gender (m/f):")
match gender:
    case "m":
        print("male")
    case "f":
        print("female")
    case _:
        print("Invalid input. please enter 'm' or 'f'.")    