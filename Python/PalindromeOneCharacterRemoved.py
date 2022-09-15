"""
    Find if the given string is a palindrome by removing only one character from the string

    I/P: racercar
    O/P: True
    Explanation: race r car -> character r can be removed and other string becomes a palindrome

    I/P: abcd
    O/P: False


"""


def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string


def is_palindrome2(string, start, end):
    while start <= end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True


def is_palindrome_remove_one_char(string):
    if not string:
        return True
    if len(string) <= 2:
        return True
    if is_palindrome(string):
        return True

    i = 0
    j = len(string) - 1
    while i <= j and string[i] == string[j]:
        i += 1
        j -= 1

    if i == j and len(string) % 2 == 1:
        return True

    if i < j and len(string) % 2 == 0:
        return True

    if is_palindrome(string[i:j]):
        # remove j char
        return True
    if is_palindrome(string[i+1:j+1]):
        # remove i char
        return True
    return False


if __name__ == "__main__":
    string_val = "malayaalam"
    print(is_palindrome_remove_one_char(string_val))