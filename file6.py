import os

# Specify the file name
file_name = "example.txt"

# Check if the file has read access
if os.access(file_name, os.R_OK):
    print(f"The file '{file_name}' has read access.")
else:
    print(f"The file '{file_name}' does NOT have read access.")

# Check if the file has write access
if os.access(file_name, os.W_OK):
    print(f"The file '{file_name}' has write access.")
else:
    print(f"The file '{file_name}' does NOT have write access.")