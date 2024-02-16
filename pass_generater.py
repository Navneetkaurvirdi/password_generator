import random
import string

def generate_password(length=12):
    """Generate a random password."""
    # Define characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure minimum length
    if length < 12:
        raise ValueError("Password length should be at least 12 characters.")

    # Generate the random password
    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Check if password meets requirements (e.g., no repeated characters)
        if (not any(password[i] == password[i+1] for i in range(len(password)-1))
            and not password.isdigit()     # Avoid all digits
            and not password.isalpha()):   # Avoid all alphabets
            break

    return password

def generate_multiple_passwords(num_passwords, length=12):
    """Generate multiple random passwords."""
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

def main():
    print("*** Strong Password Generator ***")
    num_passwords = int(input("Enter the number of passwords to generate: "))
    password_length = int(input("Enter the length of each password (minimum 12 characters): "))
    
    passwords = generate_multiple_passwords(num_passwords, password_length)
    
    print("\nGenerated Passwords:")
    for idx, password in enumerate(passwords, start=1):
        print(f"Password {idx}: {password}")

if __name__ == "__main__":
    main()


