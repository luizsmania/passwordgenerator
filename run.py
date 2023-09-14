import random
import string

def generate_password(length, has_letters=True, has_symbols=True):
    pwd = ""
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    while len(pwd) < length:
        new_letter = random.choice(letters)
        new_number = random.choice(numbers)
        new_symbol = random.choice(symbols)

        choice = random.randint(0,3)
        if choice == 1 and has_letters:
            pwd += new_letter
        elif choice == 2:
            pwd += new_number
        elif choice == 3 and has_symbols:
            pwd += new_symbol
                
    return pwd

what_length = int(input("Enter the minimum length: "))
want_number = input("Do you want to have numbers (y/n)?").lower() == "y"
want_special = input("Do you want to have special characters (y/n)?").lower() == "y"
pwd = generate_password(what_length, want_number, want_special)
print(pwd)