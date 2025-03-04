import random
import string

def generate_password(length=12):
    # Define character sets
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Get user input for password length
length = int(input("Enter the desired password length: "))
password = generate_password(length)
print(f"Generated Password: {password}")

