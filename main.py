import sys
import pikepdf
from pikepdf import PasswordError
from tqdm import tqdm

# Handle user arguments
pdf_file = sys.argv[1]
wordlist = sys.argv[2]

# Get passwords from wordlist
passwords = [line.strip() for line in open(wordlist)]

# Attempt to crack pdf using the passwords.
for password in tqdm(passwords, "Decrypting PDF"):
    try:
        with pikepdf.open(pdf_file, password=password) as pdf:
            print("[+] Password found: ", password)
            break
    except PasswordError as e:
        continue
else:
    print("[+] No password found! ")