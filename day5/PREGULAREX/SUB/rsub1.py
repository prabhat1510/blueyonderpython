# Example - sub function to replace the substrings



import re
text = "Python for beginner is a very cool Language."
print("Before Replacing :", text)

text2 = re.sub("cool", "good", text)
print("After Replacing :",text2)
