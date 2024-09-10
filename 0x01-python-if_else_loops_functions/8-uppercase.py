def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            # Convert to uppercase by subtracting 32 from the ASCII value
            print(chr(ord(char) - 32), end="")
        else:
            print(char, end="")
    print()  # Print a new line at the end
