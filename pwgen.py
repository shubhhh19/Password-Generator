import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def gen_pass():
    pass_length = int(input("Enter password length: "))

    random.shuffle(characters)
    password = []

    