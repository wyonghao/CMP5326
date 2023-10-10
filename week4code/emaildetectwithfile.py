import re
import csv

def find_emails(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    # NOTE: above code is altered with unicode encoding to avoid error
 
    # TODO: Write your regex pattern here using raw string
    email_pattern_raw = r'([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})' # Fill in your regex pattern here
 
    # TODO: Compile your regex pattern using re.compile
    email_pattern_compiled = re.compile(email_pattern_raw) # Fill in your regex pattern here
 
    # Using raw string pattern
    emails_raw = re.findall(email_pattern_raw, text)
 
    # Using compiled pattern
    emails_compiled = email_pattern_compiled.findall(text)
    
    print("Found the following email addresses using raw string:")
    for email in emails_raw:
        print(email)
    
    print("\nFound the following email addresses using compiled pattern:")
    for email in emails_compiled:
        print(email)
        
    with open('emails.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Emails"])
        
        for email in emails_compiled:
            writer.writerow([email])

if __name__ == "__main__":
    filename=input("Enter the filename: ")
    find_emails(filename)
