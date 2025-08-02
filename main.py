import sys
import pikepdf
from pikepdf import PasswordError
from tqdm import tqdm

pdf_file = sys.argv[1]

wordlist = sys.argv[2]

passwords = [line.strip() for line in open(wordlist)]

for password in tqdm(passwords, "Decrypting PDF"):
    try:
        with pikepdf.open(pdf_file, password=password) as pdf:
            print("[+] Password found: ", password)
            break
    except PasswordError as e:

        continue
else:
    print("[+] No password found! ")