# 🔓 PDF Password Cracker (Bruteforce, Python, PikePDF)

## 📖 Overview

This project demonstrates how to crack password-protected PDF files using Python. It uses a dictionary-based brute-force attack to attempt decryption with each password from a wordlist. The script uses the `pikepdf` library, which supports opening encrypted PDFs and raises an error if the password is incorrect.

This tool is designed for **educational purposes** and ethical testing of password security.

## ✨ Features

- Crack password-protected PDF files using a wordlist
- Detects successful password and halts on match
- Uses `tqdm` for a clean progress bar
- Handles encoding issues in wordlists gracefully
- Lightweight and simple — written in pure Python

## 🧰 Installation

Clone the repository and install required dependencies:

```bash
git clone https://github.com/yourusername/pdf-password-cracker.git
cd pdf-password-cracker
pip install -r requirements.txt
```

Or install dependencies manually:

```bash
pip install pikepdf tqdm
```

## ▶️ Usage

Run the script using the following command:

```bash
python main.py "path/to/locked.pdf" "path/to/wordlist.txt"
```

### Example:

```bash
python main.py "FilesToCrack/LockedDocument.pdf" "rockyou.txt"
```

> Note: Use quotes around file paths if they contain spaces.

## 🧪 Testing

You can create your own password-protected PDF using tools like:
- Microsoft Print to PDF (with security settings)
- LibreOffice
- Adobe Acrobat

Or download sample locked PDFs from:
- [https://www.pdf2go.com/protect-pdf](https://www.pdf2go.com/protect-pdf)
- [https://www.ilovepdf.com/protect-pdf](https://www.ilovepdf.com/protect-pdf)

Then try cracking them with a custom wordlist like:

```
1234
admin
password
letmein
secret123
```

## 📚 Documentation

### File Structure

```
pdf-password-cracker/
├── main.py              # Main cracking script
├── README.md            # This documentation file
└── requirements.txt     # Python dependencies
```

### How It Works

1. Loads the wordlist into memory
2. Tries to open the encrypted PDF with each password
3. On success, prints the correct password and exits
4. On failure, tries the next password until the list is exhausted

## 🤝 Contributing

Pull requests are welcome! Please open an issue to discuss changes or feature suggestions first.

## ⚖️ License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for full details.

## 📞 Contact

**Project Author**: Code Savvy  
**Email**: info@codesavvy.club
**GitHub**: [https://github.com/codesavvyclub](https://github.com/codesavvyclub)

## 🔗 Project Link

[https://github.com/codesavvyclub/pdf-password-cracker](https://github.com/codesavvyclub/pdf-password-cracker)
