import re

# Open and read the content of lab1example.txt
with open('lab1example.txt', 'r', encoding="utf8") as input_file:
    lines = input_file.readlines()  # Read the file line by line for line number tracking

# Prompt the user to input a regex search pattern
search_pattern = input("Please enter a regex search pattern: ")

# Validate regex pattern
compiled_pattern = re.compile(search_pattern)

# Print the matching results with line numbers and save to a file
print("\nMatching Results:")
with open('regex_matches.txt', 'w') as output_file:
    for line_number, line in enumerate(lines, start=1):
        matches = compiled_pattern.findall(line)
        if matches:
            result = f"Line {line_number}: {matches}"
            print(result)
            output_file.write(result + "\n")