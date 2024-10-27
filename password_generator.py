import json
import os
import random
import string
from cryptography.fernet import Fernet

# Generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Load or create a key
def load_key():
    if os.path.exists("secret.key"):
        return open("secret.key", "rb").read()
    else:
        key = generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        return key

# Encrypt the password
def encrypt_password(password, key):
    f = Fernet(key)
    encrypted = f.encrypt(password.encode())
    return encrypted

# Decrypt the password
def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_password).decode()
    return decrypted

# Save passwords to a JSON file
def save_password(service, password, key):
    encrypted_password = encrypt_password(password, key)
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as f:
            passwords = json.load(f)
    else:
        passwords = {}

    passwords[service] = encrypted_password.decode()  # Store as string
    with open("passwords.json", "w") as f:
        json.dump(passwords, f)

# Generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Retrieve a password
def retrieve_password(service, key):
    if not os.path.exists("passwords.json"):
        return None
    with open("passwords.json", "r") as f:
        passwords = json.load(f)
    
    if service in passwords:
        encrypted_password = passwords[service].encode()
        return decrypt_password(encrypted_password, key)
    return None

def main():
    key = load_key()

    while True:
        choice = input("Choose an option: [save, retrieve, generate, exit]: ").strip().lower()
        
        if choice == "save":
            service = input("Enter the service name: ")
            password = input("Enter the password: ")
            save_password(service, password, key)
            print(f"Password for {service} saved successfully.")
        
        elif choice == "retrieve":
            service = input("Enter the service name: ")
            password = retrieve_password(service, key)
            if password:
                print(f"Password for {service}: {password}")
            else:
                print("Service not found.")
        
        elif choice == "generate":
            service = input("Enter the service name: ")
            password = generate_password()
            save_password(service, password, key)
            print(f"Generated password for {service}: {password}")
        
        elif choice == "exit":
            print("Exiting the password manager.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
