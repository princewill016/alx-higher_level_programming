def print_alternating_reverse():
    for i in range(25, -1, -1):
        # Print lowercase and uppercase alternately
        if i % 2 == 0:
            print(chr(122 - i), end="")  # 'z' (122) minus index 'i'
        else:
            print(chr(90 - (i - 1)), end="")  # 'Y' (90) minus (i - 1)
