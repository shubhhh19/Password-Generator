import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def gen_password():
    password_length = int(input("Enter password length: "))

    random.shuffle(characters)
    password = []

    for x in range(password_length):
        password.append(random.choice(characters))
        
    random.shuffle(password)
    password = "".join(password)
    print(password)

option = input("Do you want to generate password? (Yes/No):" + "\n")
if option == "Yes":
    gen_password()
elif option == "No":
    print("Program ended")
    quit()
else: 
    print("Program exited")
    quit()