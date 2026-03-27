import secrets, os, subprocess, datetime
# ===== CLASS =====
class User:
    def __init__(self, label, password, date):
        self.label = label
        self.password = password
        self.date = date
    def __str__(self):
        return f"Password task: {self.label}\n  Date: {self.date}\n  Password: {self.password}"

#  ===== GET_CHOICE =====
def get_choice(text):
    while True:
        choice = str(input(text))
        if choice in ("1", "2", "3"):
            return choice
        else:
            print("Please enter a valid option!")

#  ===== GENERATION PASSWORD =====
def generation(password_file, menu):
    label = input("\nWhat do you need the password for: ")
    date = f"({datetime.datetime.date(datetime.datetime.now())})"
    print("\n====NUMBER OF CHARACTERS====\n1. 8 characters.\n2. 16 characters.\n3. 32 characters.\n")
    choice = get_choice("Choose an action: ")

    lengths = {"1": 8, "2": 16, "3": 32}                                # <--- GENERATION PASSWORD
    password = secrets.token_urlsafe(lengths[choice])
    print(f"\nPassword successfully generated: {password}")

    user = User(label, password, date)
    menu.append(user)                                                   # <--- SAVE IN LIST

    with open(password_file, "a", encoding="utf-8") as file:            # <--- SAVE IN TXT
        file.write(f"\u25CF {user}\n\n")

# ===== OPEN TXT =====
def open_passwords(password_file):
    subprocess.Popen(['notepad.exe', password_file])

# ===== PROGRAM =====
def main():
    # GETTING THE PATH TO THE CURRENT USER'S DESKTOP
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    password_file = os.path.join(desktop, "passwords.txt")              # <--- FILE ON THE DESKTOP

    menu = []                                                           # <--- LIST

    while True:
        print("\n=====GENERATING PASSWORD=====")
        print("1. Generate a new password.\n2. Open txt file.\n3. Exit.")
        choice = get_choice("\nChoose an action: ")
        if choice == "1":                                               # <--- GENERATION PASSWORD
            generation(password_file, menu)
        elif choice == "2":                                             # <--- OPEN TXT
            open_passwords(password_file)
            break
        elif choice == "3":                                             # <--- EXIT
            print("\nGoodbye!")
            break

# ===== START =====
if __name__ == "__main__":
    main()
