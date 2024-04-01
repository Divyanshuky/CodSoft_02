import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    uppercase_chars = random.choices(uppercase_letters, k=2)
    digit = random.choice(digits)
    special_char = random.choice(special_characters)
    remaining_length = length - (2 + 1 + 1)
    remaining_chars = random.choices(lowercase_letters + uppercase_letters + digits + special_characters, k=remaining_length)
    password_chars = uppercase_chars + [digit] + [special_char] + remaining_chars
    random.shuffle(password_chars)
    password = ''.join(password_chars)
    return password

while True:
    try:
        length = int(input("Enter the length of the password: "))
        if length < 4:
            print("Password length must be at least 4 characters.")
        else:
            break
    except ValueError:
        print("Please enter a valid integer.")

# To Generate the password
password = generate_password(length)
print("Random Password:", password)
