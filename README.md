# EN_DE_Crypt — Caesar Cipher Tool

EN_DE_Crypt is a command-line tool that encrypts and decrypts text using the classical Caesar cipher. It shifts alphabetic characters by a user-specified number of positions.

## ✨ Features

- Encrypt text using a configurable shift value.
- Decrypt text using the same shift value.
- Preserve uppercase and lowercase letters.
- Wrap alphabet positions using modulo arithmetic.
- Keep non-alphabetic characters unchanged.
- Validate menu selections and numeric shift input.
- Continue processing multiple messages in one session.

## 🛠️ Built With

- Python 3
- `string` standard-library module
- Functions
- String processing
- Modular arithmetic
- Input validation

No external packages are required.

## 🚀 Run Locally

```bash
git clone https://github.com/Mohamed-Elsafty-7/Project3.git
cd Project3
python en_de_crypt.py
```

Use `python3 en_de_crypt.py` if your system requires it.

## 🔐 How It Works

1. Choose encryption or decryption.
2. Enter the message.
3. Provide a shift number.
4. View the transformed text.
5. Continue with another message or exit.

The tool uses the English alphabet and wraps shifts around the 26 letters.

## 📚 What I Practiced

- Writing reusable functions.
- Working with uppercase and lowercase text.
- Applying modular arithmetic.
- Handling invalid user input.
- Separating program logic into encryption and decryption functions.

## ⚠️ Security Note

The Caesar cipher is a historical substitution cipher and is not secure for protecting sensitive information. This project is intended for learning and experimentation, not real-world data security.

## 🔮 Possible Improvements

- Add automated tests for different shift values.
- Support reading text from files.
- Improve the user interface.
- Explore modern cryptographic libraries for secure encryption use cases.

---

A Python learning project exploring text transformation and classical cryptography.
