# main.py
import sys
from input_handler import get_yes_no_input
from password_logic import generate_password

def main():
    """
    Main function to execute the Password Generator application.
    """
    print("--- 🔒 Secure Password Generator 🔒 ---")

    # 1. Get password length
    while True:
        try:
            length_input = input("Enter desired password length (min 8): ")
            length = int(length_input)
            
            if length < 8:
                print("Length must be at least 8 for security.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # 2. Get character set preferences using our imported module
    print("\nSelect character types to include:")
    
    include_lower = get_yes_no_input("Include lowercase letters? (Y/N): ")
    include_upper = get_yes_no_input("Include uppercase letters? (Y/N): ")
    include_digits = get_yes_no_input("Include numbers (0-9)? (Y/N): ")
    include_symbols = get_yes_no_input("Include symbols (!@#$%, etc.)? (Y/N): ")

    # 3. Validate selection
    if not (include_lower or include_upper or include_digits or include_symbols):
        print("\nError: You must select at least one character type. Exiting.")
        sys.exit(1)

    # 4. Generate and Output
    try:
        password = generate_password(length, include_lower, include_upper, include_digits, include_symbols)

        print("\n" + "="*40)
        print(f"✅ Generated Password (Length: {length}):")
        print(f"🔑 {password}")
        print("="*40)

    except ValueError as e:
        print(f"\nGeneration Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()