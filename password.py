
import random
import string

def generate_password(length=12, use_digits=True, use_special=True, use_upper=True, use_lower=True):
    # Build the character pool based on user preferences
    characters = ""
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("No character sets selected!")

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(count=5, length=12, **kwargs):
    return [generate_password(length, **kwargs) for _ in range(count)]

# Example usage
print("Single password:", generate_password(16, use_digits=True, use_special=True))
print("Multiple passwords:", generate_multiple_passwords(count=3, length=10, use_special=False))




