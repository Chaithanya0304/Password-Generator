import random
import string
def generate_password(length=12):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    password = (
        random.choice(uppercase_letters)
        + random.choice(lowercase_letters)
        + random.choice(digits)
        + random.choice(special_characters)
    )

    # Add random characters from all categories to complete the password
    password += ''.join(random.choice(all_characters) for _ in range(length - 4))

    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password

def generate_multiple_passwords(num_passwords, length):
    passwords = []
    for _ in range(num_passwords):
        password = generate_password(length)
        passwords.append(password)
    return passwords

password_length = int(input("Enter the length of the password: "))
num_of_passwords = int(input("Enter the number of passwords to generate: "))
generated_passwords = generate_multiple_passwords(num_of_passwords, password_length)

print(f"\nGenerated Passwords ({num_of_passwords} passwords of length {password_length}):")
for index, password in enumerate(generated_passwords, start=1):
    print(f"Password {index}: {password}")

