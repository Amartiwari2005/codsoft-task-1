
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get desired password length from the user
length = int(input("Enter the desired password length: "))

# Generate the password
password = generate_password(length)

# Display the generated password
print("Generated Password:", password)

