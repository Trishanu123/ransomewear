import subprocess
import sys

# Ensure the 'cryptography' library is installed
def ensure_cryptography_installed():
    try:
        import cryptography  # Check if the library is already installed
    except ImportError:
        print("The 'cryptography' library is not installed. Installing it now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "cryptography"])
        print("'cryptography' library installed successfully.")

# Import Fernet after ensuring the library is installed
ensure_cryptography_installed()
from cryptography.fernet import Fernet

# Generate a key and save it to a file
def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved as 'encryption_key.key'.")

# Load the key from a file
def load_key():
    with open("encryption_key.key", "rb") as key_file:
        return key_file.read()

# Encrypt the file
def encrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)

    # Read the file to encrypt
    with open(file_path, "rb") as file:
        file_data = file.read()

    # Encrypt the data
    encrypted_data = fernet.encrypt(file_data)

    # Write the encrypted data back to the file
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

    print(f"File '{file_path}' encrypted successfully.")

# Decrypt the file
def decrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)

    # Read the encrypted file
    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    # Decrypt the data
    decrypted_data = fernet.decrypt(encrypted_data)

    # Write the decrypted data back to the file
    with open(file_path, "wb") as file:
        file.write(decrypted_data)

    print(f"File '{file_path}' decrypted successfully.")

# Example usage
if __name__ == "__main__":
    ensure_cryptography_installed()
    generate_key()  # Run once to create a key
    file_to_encrypt = "example.txt"  # Specify the file you want to encrypt
    encrypt_file(file_to_encrypt)
    decrypt_file(file_to_encrypt)
