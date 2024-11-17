# 🔐 Password Generator with Translation

A secure password generator built using **Streamlit** and **GoogleTranslator**. This app takes an input word in English, translates it into another language (default: Spanish), and generates a secure password by appending special characters, numbers, and a unique suffix. 

The app also attempts to copy the generated password directly to your clipboard for convenience!

---

## 🚀 Features
- **Translation-Based Passwords**: Translates the input word into another language (default: Spanish).
- **Customizable Options**: 
  - Include/exclude special characters.
  - Include/exclude numbers.
- **Unique Passwords**: Ensures every generated password is unique by appending a random suffix.
- **Clipboard Support**: Automatically copies the generated password to your clipboard (if supported by the environment).

---

## 📂 Requirements
To run this application, you will need:
- **Python 3.7+**
- The following Python libraries:
  - `streamlit`
  - `deep_translator`
  - `pyperclip`
  - `random`
  - `uuid`

---

## 🛠️ Installation
1. Clone this repository or copy the code into a local directory:
   ```bash
   git clone https://github.com/your-repo/password-generator.git
   cd password-generator
