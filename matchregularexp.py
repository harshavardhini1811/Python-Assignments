import re 
pattern = r"Hello\s\w+"
text = "Hello Python"
match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No Match found:")    