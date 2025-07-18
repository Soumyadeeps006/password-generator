import random
import string

def get_user_input():
    length = int(input("Enter password length: "))
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    return length, use_upper, use_lower, use_digits, use_special

def build_character_pool(use_upper, use_lower, use_digits, use_special):
    pool = ""
    if use_upper:
        pool += string.ascii_uppercase
    if use_lower:
        pool += string.ascii_lowercase
    if use_digits:
        pool += string.digits
    if use_special:
        pool += string.punctuation
    return pool

def generate_password(pool, length):
    if not pool:
        raise ValueError("Character pool is empty. Please select at least one character type.")
    password = ''.join(random.choices(pool, k=length))
    return password

def main():
    print("🔐 Welcome to the Password Generator!")
    length, use_upper, use_lower, use_digits, use_special = get_user_input()
    pool = build_character_pool(use_upper, use_lower, use_digits, use_special)
    
    try:
        password = generate_password(pool, length)
        print(f"\n✅ Generated Password: {password}")
    except ValueError as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()