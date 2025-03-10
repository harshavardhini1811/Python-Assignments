import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def compare_strings(str1, str2):
    """Compare two strings in a manner similar to Java's compareTo().
       Returns a descriptive result based on lexicographical order."""
    result = locale.strcoll(str1, str2)
    if result < 0:
        return f'"{str1}" comes before "{str2}"'
    elif result > 0:
        return f'"{str1}" comes after "{str2}"'
    else:
        return f'"{str1}" is equal to "{str2}"'
text = "Hello, Python Programming!"
print("Does the text start with 'Hello'? :", text.startswith("Hello"))
print("Does the text end with 'Programming!'? :", text.endswith("Programming!"))
str1 = "Apple"
str2 = "Banana"
comparison_result = compare_strings(str1, str2)
print("Comparison result using compareTo() equivalent:")
print(comparison_result)
