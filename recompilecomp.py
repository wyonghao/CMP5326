import re

text1 = "The rain in Spain"
text2 = "The sun in Spain"

pattern = r"\bS\w+"

# Using the pattern on text1
matches1 = re.findall(pattern, text1)
print(matches1)

# Using the pattern on text2
matches2 = re.findall(pattern, text2)
print(matches2)

import re

text1 = "The rain in Spain"
text2 = "The sun in Spain"

# Compile the pattern
compiled_pattern = re.compile(r"\bS\w+")

# Using the compiled pattern on text1
matches1 = compiled_pattern.findall(text1)
print(matches1)

# Using the compiled pattern on text2
matches2 = compiled_pattern.findall(text2)
print(matches2)