
import re

with open("web_content.txt", "r") as file:
    content = file.read()

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(pattern, content)

unique_emails = list(set(emails))

print("Unique Email Addresses:")

for email in unique_emails:
    print(email)

print("Total Unique Emails:", len(unique_emails))
