original = [1, 2, 3, 4, 5]
copy_via_slice = original[:]
copy_via_constructor = list(original)
copy_via_method = original.copy()
print("Original Array:", original)
print("Copied using slicing:", copy_via_slice)
print("Copied using list() constructor:", copy_via_constructor)
print("Copied using copy() method:", copy_via_method)