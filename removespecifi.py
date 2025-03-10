def remove_first_occurrence(arr, element):
    try:
        arr.remove(element)
    except ValueError:
        print(f"{element} not found in the array.")
    return arr
my_array = [1, 2, 3, 4, 3, 5]
print("Original array:", my_array)
element_to_remove = int(input("Enter the element to remove: "))
result = remove_first_occurrence(my_array, element_to_remove)
print("Array after removal of first occurrence:",result)