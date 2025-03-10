from collections import Counter

def find_duplicates(arr):
    # Count the frequency of each element in the array
    counts = Counter(arr)
    # Filter and return only those elements that occur more than once
    duplicates = [item for item, count in counts.items() if count > 1]
    return duplicates

# Example usage:
numbers = [1, 2, 3, 4, 2, 3, 5, 6, 3]
dup = find_duplicates(numbers)
print("Duplicate values:",dup)