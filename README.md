# Simple Input Checker

This is a simple input checker module that provides functions for validating user input. The module is implemented in `validation.py`.

## Functions

### `is_integer(input)`

Checks if the input is a valid integer.

**Parameters:**
- `input` (any): The input to be checked.

**Returns:**
- `True` if the input is a valid integer, `False` otherwise.

### `is_valid_input(question, answer, case_sensitive=False)`

Validates the user's input by asking for confirmation.

**Parameters:**
- `question` (str): The question to ask the user.
- `answer` (str): The user's input to validate.
- `case_sensitive` (bool, optional): Whether the validation is case-sensitive. Defaults to False.

**Returns:**
- `bool`: True if the input is considered valid, False otherwise.

### `ask_for_number(question, min, max)`

Asks the user for a number within a specified range.

**Parameters:**
- `question` (str): The question to ask the user.
- `min` (int): The minimum value allowed.
- `max` (int): The maximum value allowed.

**Returns:**
- `int`: The number entered by the user.

**Raises:**
- `ValueError`: If the user enters a non-numeric value.

### `ask_for_alphabet(question, case_sensitive=False)`

Asks the user for an alphabet (letters) input.

**Parameters:**
- `question` (str): The question to ask the user.
- `case_sensitive` (bool, optional): Whether the input is case-sensitive. Defaults to False.

**Returns:**
- `str`: The alphabet entered by the user.

Example usage:
