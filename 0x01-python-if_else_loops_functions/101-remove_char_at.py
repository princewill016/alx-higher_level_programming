#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    result = ""
    for i in range(len(str)):
        if i != n:
            result += str[i]
    return result
