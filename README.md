# 🔐 Password Generator

The Password Generator is a Python-based tool designed to generate secure, random passwords for various use cases. It also allows you to save and view previously created passwords. This project ensures easy and efficient password management while emphasizing security.

## 🔧 Features

- Generate strong passwords with a mix of:
  - 🔷 Lowercase letters
  - 🔺 Uppercase letters
  - 🔢 Digits
  - ✨ Special characters
- Specify the length of the password (minimum 4 characters).
- Save passwords to a file for future reference.
- View previously generated passwords using a secure access code.

## 📊 How It Works

1. The user provides a purpose or subject for the password.
2. The user specifies the desired password length.
3. A random password is generated using Python's `secrets` library, ensuring high levels of randomness and security.
4. The password is saved to a text file located on the desktop.
5. Users can view all previously generated passwords by entering a special access code.

## 🗒 File Structure

The generated passwords are stored in a file named `passwords.txt` located in:

```
C:\Users\<username>\Desktop\passwords\
```

## 🔧 Prerequisites

- Python 3.6 or higher
- Libraries used:
  - `secrets` (part of Python's standard library)
  - `os` (part of Python's standard library)
  - `pyfiglet` (install with `pip install pyfiglet`)

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/password-generator.git
   cd password-generator
   ```

2. Install the required library:
   ```bash
   pip install pyfiglet
   ```

3. Run the script:
   ```bash
   python password_generator.py
   ```

## 🔓 Usage

1. Run the script.
2. Enter the purpose for the password (e.g., "Email", "Facebook").
3. Specify the desired password length.
4. Copy the generated password and use it securely.
5. To view all saved passwords, type the special code `789123`.

## 🎨 Example

```
Password generator
The new Touti password generator
If you want to see the passwords already created, type this code: 789123

What is the username of this computer? : JohnDoe

Where will you use your password? : Email
How many characters do you want in your password? : 12
Your password is: x2E!mH7p9c$a
```

## 🛡️ Security

This script uses the `secrets` library for password generation, which is recommended for cryptographic purposes. However, note that passwords are saved in plaintext, so ensure that the `passwords.txt` file is stored securely.

## 🕵️‍♂️ Disclaimer

This project is for educational purposes only. While it generates secure passwords, it is your responsibility to ensure that the generated passwords and the saved file are handled securely.

## 📚 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

