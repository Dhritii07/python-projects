import re 
import requests

sample_domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "rediffmail.com"]

tlds = [".com", '.org', '.net', 'edu', '.gov', '.info', '.co', '.io', '.me', '.biz']

def checkMail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if not re.fullmatch(regex, email):
        return False
    
    domain = email.split('@')[1]
    if domain not in sample_domains:
        print(f"Warning: The domain '{domain}' is uncommon. Please verify if correct.")
    
    tld = '.' + domain.split('.')[-1]
    if tld not in tlds:
        print(f"Warning: The TLD '{tld}' might not be valid. Please verify.")
    
    return True

def get_output(email):
    username = email[0:email.index('@')]
    domain = email[email.index('@') + 1:]

    return username, domain

email = input('Enter your email id: ')

if checkMail(email):
    username, domain = get_output(email)
    print("Username: ", username)
    print('Domain: ', domain)
else:
    print("Invalid Email!")