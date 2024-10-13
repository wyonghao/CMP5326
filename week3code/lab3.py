import re
import csv

def find_emails(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Regex pattern to match valid email addresses
    email_pattern_raw = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # Compile the regex pattern
    email_pattern_compiled = re.compile(email_pattern_raw)
    
    # Using raw string pattern
    emails_raw = re.findall(email_pattern_raw, text)
    
    # Using compiled pattern
    emails_compiled = email_pattern_compiled.findall(text)
    
    # Display emails found using raw pattern
    print("Found the following email addresses using raw string:")
    for email in emails_raw:
        print(email)
        
    # Display emails found using compiled pattern
    print("\nFound the following email addresses using compiled pattern:")
    for email in emails_compiled:
        print(email)
    
    # Write the email addresses to a CSV file
    with open('emails.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Emails"])
        for email in emails_raw:  # Writing the list from raw string matching
            writer.writerow([email])
    print("\nEmail addresses have been written to 'emails.csv'.")

# The following block ensures that the code runs only when the script is executed directly,
# and not when it is imported as a module in another script.
if __name__ == "__main__":
    filename = input("Enter the filename: ")
    find_emails(filename)