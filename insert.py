def insert_element(arr, element, position):
    arr.insert(position, element)
    return arr
numbers = [10, 20, 30, 40, 50]
print("Original array:", numbers)
element_to_insert = int(input("Enter the element to insert: "))
position = int(input("Enter the position (0-based index) to insert at: "))
updated_numbers = insert_element(numbers, element_to_insert, position)
print("Updated array:", updated_numbers)