# File containing functions for validating user input of various types.
def is_integer(number):
    """
    Checks if a number is an integer.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is an integer, False otherwise.
    """
    return isinstance(number, int)


def is_valid_input(question, answer, case_sensitive=False):
    """
    Validates the user's input by asking for confirmation.

    Args:
        question (str): The question to ask the user.
        answer (str): The user's input to validate.
        case_sensitive (bool, optional): Whether the validation is case-sensitive. Defaults to False.

    Returns:
        bool: True if the input is considered valid, False otherwise.
    """
    while True:
        valid = input(f"Is {question}: {answer} correct? (y/n): ").lower()
        valid_options = [["y", "yes", "1", "true"], ["n", "no", "0", "false"]]
        if valid in valid_options[0]:
            return True
        elif valid in valid_options[1]:
            return False
        else:
            print("Please enter yes or no")

def ask_for_number(question, min, max):
    """
    Asks the user for a number within a specified range.

    Args:
        question (str): The question to ask the user.
        min (int): The minimum value allowed.
        max (int): The maximum value allowed.

    Returns:
        int: The number entered by the user.

    Raises:
        ValueError: If the user enters a non-numeric value.
    """
    while True:
        try:
            question_to_ask = f"{question} ({min} - {max}):"
            number = int(input(question_to_ask))
            if min <= number <= max:
                valid = is_valid_input(question_to_ask, number)
                if valid:
                    return number
            else:
                print(f"Please enter a number between {min} and {max}")
        except ValueError:
            print("Please enter a number")

def ask_for_alphabet(question, case_sensitive=False):
    while True:
        try:
            question_to_ask = f"{question}: "
            alphabet = input(question_to_ask)
            alphabet_split = alphabet.split(" ")  # Splits name, to get rid of spaces, and grab each word.
            for i in alphabet_split:
                if not i.isalpha():
                    raise ValueError
            
            # Checks user wants to submit this (correct) name
            valid = is_valid_input(question_to_ask, alphabet)
            if valid:
                return alphabet, alphabet_split
        except ValueError:
            print("Please enter only letters")

name = ask_for_alphabet("Enter your name")
print(name[1])