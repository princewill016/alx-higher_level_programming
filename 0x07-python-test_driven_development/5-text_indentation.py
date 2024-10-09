#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The input string to process.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize an empty string to store the formatted text
    formatted_text = ""

    # Loop through each character in the input text
    i = 0
    while i < len(text):
        formatted_text += text[i]
        # Check if the character is '.', '?', or ':'
        if text[i] in ['.', '?', ':']:
            formatted_text += "\n\n"  # Add two newlines
            i += 1
            # Skip any spaces following '.', '?', or ':'
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1

    # Strip extra spaces from the start and end of each line and print the result
    print(formatted_text.strip(), end="")
