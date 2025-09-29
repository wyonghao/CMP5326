import re  # Import the 're' module for working with regular expressions
text = "Contact: john.doe@example.com, 192.168.1.1;  leo@bcu.ac.ukkaty@gmail.com"  # Sample text containing emails and other data
email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
emails = re.findall(email_pattern, text)  # Find all substrings in 'text' that match the email pattern
print("Extracted Emails:", emails)  # Output the list of extracted email addresses