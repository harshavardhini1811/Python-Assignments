# Open the file in read mode
with open("example.txt", "r") as file:
    # Move to the 10th byte in the file
    file.seek(10)  

    # Read the next 20 bytes from the current position
    content = file.read(20)

    # Print the read content
    print("Read content from byte 10 to 30:", content)

    # Move to the beginning of the file again
    file.seek(0)
    print("\nFirst line of the file:", file.readline().strip())  # Read first line