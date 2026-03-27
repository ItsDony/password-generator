# Password Generator

A simple Python script to generate secure passwords and save them to a text file on your Desktop.

## Features
- Generate random passwords of 8, 16, or 32 characters
- Save passwords with labels and creation date
- View all saved passwords in a text file
- Simple menu-driven interface

## How It Works
1. When you run the script, you'll see a menu:
   - **Generate a new password**
   - **Open the saved passwords file**
   - **Exit**
2. To generate a password:
   - Enter what the password is for (label)
   - Choose the length (8, 16, or 32 characters)
   - The script generates a secure random password
   - The password is saved to a `passwords.txt` file on your Desktop along with the label and date
3. To view passwords:
   - Choose the menu option to open the file
   - On Windows, it opens automatically in Notepad

## Installation
1. Make sure you have **Python 3** installed.
2. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/password-generator.git
cd password-generator
