# password_logic.py
import random
import string

# Define constants
LOWERCASE_CHARS = string.ascii_lowercase
UPPERCASE_CHARS = string.ascii_uppercase
DIGIT_CHARS = string.digits
SYMBOL_CHARS = string.punctuation

def generate_password(length: int, include_lower: bool, include_upper: bool, include_digits: bool, include_symbols: bool) -> str:
    """
    Generates a strong, random password based on the specified criteria.
    """
    characters = ""
    required_chars = [] 

    # Build the pool of characters
    if include_lower:
        characters += LOWERCASE_CHARS
        required_chars.append(random.choice(LOWERCASE_CHARS))
    if include_upper:
        characters += UPPERCASE_CHARS
        required_chars.append(random.choice(UPPERCASE_CHARS))
    if include_digits:
        characters += DIGIT_CHARS
        required_chars.append(random.choice(DIGIT_CHARS))
    if include_symbols:
        characters += SYMBOL_CHARS
        required_chars.append(random.choice(SYMBOL_CHARS))

    # Error handling: Ensure at least one character type is selected
    if not characters:
        raise ValueError("Must select at least one character type for the password.")

    # Calculate remaining length
    random_part_length = length - len(required_chars)

    if random_part_length < 0:
        # If length is shorter than the required types, truncate
        password_list = required_chars[:length]
    else:
        # Fill the rest with random choices from the allowed pool
        random_part = [random.choice(characters) for _ in range(random_part_length)]
        password_list = required_chars + random_part

    # Shuffle to mix required characters
    random.shuffle(password_list)

    return "".join(password_list)