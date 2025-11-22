# input_handler.py

def get_yes_no_input(prompt: str) -> bool:
    """
    Helper function to validate Y/N input.
    Repeats the prompt until the user enters Y, y, N, or n.
    
    Args:
        prompt: The question to ask the user.
        
    Returns:
        True if user enters 'Y', False if user enters 'N'.
    """
    while True:
        user_input = input(prompt).strip().upper()
        
        if user_input == 'Y':
            return True
        elif user_input == 'N':
            return False
        else:
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")