import secrets
import os
import pyfiglet

api = pyfiglet.figlet_format("Password generator", font="slant")
print(api + "The new Touti password generator\nIf you want to see the passwords already created, type this code: 789123\n")
username=input("what is the user name of this computer? : ")
password_dir = "C:\\Users\\" + username +"\\Desktop\\passwords"
os.makedirs(password_dir, exist_ok=True)

while True:
    try:
        subject = input("\nWhere will you use your password? : ").strip()
        if subject == "789123": 
            with open(os.path.join(password_dir, "passwords.txt"), "r", encoding="utf-8") as file:
                content = file.read()
                print(content)
            continue  

        while not subject:
            print("I said, write where you will use your password!")
            subject = input("Where will you use your password? : ").strip()

        length = int(input("How many characters do you want in your password? : "))

        while length < 4:
            print("You need at least 4 characters for a secure password.")
            length = int(input("How many characters do you want in your password? : "))

        digits = "0123456789"
        letters = "azertyuiopmlkjhgfdsqwxcvbn"
        uppercase_letters = letters.upper()
        special_characters = "}@()é&à=+-*/ç_²$ù^!;,"

        full_list = list(letters + digits + uppercase_letters + special_characters)
        
        password = ''.join(secrets.choice(full_list) for _ in range(length))
        with open("C:\\Users\\"+ username +"\\Desktop\\passwords\\passwords.txt", "a", encoding="utf-8") as file:
            file.write(f"{subject}: {password}\n")

        print("Your password is: ", password)

    except ValueError:
        print("Enter a number, not a word!")
    except KeyboardInterrupt:
        print("Okay! The program will terminate!")
        break
