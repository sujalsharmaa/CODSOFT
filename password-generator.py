import random
import string

def generate_password():
    """
    Generates a secure, random password based on user-specified
    length and complexity.
    """
    
    # 1. Define the character sets
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    digit_chars = string.digits
    symbol_chars = string.punctuation

    # --- User Input ---

    # 2. Get user input for length
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 8): "))
            if length < 8:
                print("For security, password length must be at least 8 characters.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # 3. Get user input for complexity
    wants_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    wants_digits = input("Include numbers? (y/n): ").lower() == 'y'
    wants_symbols = input("Include symbols (e.g., @, #, $)? (y/n): ").lower() == 'y'

    # --- Generate Password ---

    # 4. Build the character pool and the initial password
    
    # The pool will contain all possible characters
    all_chars = list(lowercase_chars)
    
    # The password list will be built up, starting with
    # one guaranteed character from each selected set.
    password = [random.choice(lowercase_chars)]
    
    if wants_uppercase:
        all_chars.extend(list(uppercase_chars))
        password.append(random.choice(uppercase_chars))
        
    if wants_digits:
        all_chars.extend(list(digit_chars))
        password.append(random.choice(digit_chars))

    if wants_symbols:
        all_chars.extend(list(symbol_chars))
        password.append(random.choice(symbol_chars))

    # 5. Fill the rest of the password
    # Calculate how many more characters we need
    remaining_length = length - len(password)
    
    if remaining_length > 0:
        # Add random characters from the *entire* pool
        password.extend(random.choices(all_chars, k=remaining_length))

    # 6. Shuffle the password
    # This is crucial! It ensures the guaranteed characters
    # (e.g., 'a', 'A', '1', '!') don't always appear at the start.
    random.shuffle(password)

    # 7. Convert the list of characters back into a final string
    final_password = "".join(password)
    
    # --- Display the Password ---
    
    print("\n" + "="*27)
    print("  🔐 Your Generated Password")
    print("="*27)
    print(f"  {final_password}")
    print("="*27 + "\n")


# Run the main function when the script is executed
if __name__ == "__main__":
    generate_password()