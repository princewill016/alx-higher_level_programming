def remove_char_at(str, n):
    # Check if n is within the valid range
    if n < 0 or n >= len(str):
        return str  # Return the original string if n is out of range

    # Create the new string without the character at index n
    return str[:n] + str[n+1:]

