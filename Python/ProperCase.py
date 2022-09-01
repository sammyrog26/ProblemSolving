"""
Given a String, return the string with proper case
eg:
    I/P: this is python
    O/P: This Is Python

    I/P: everyone loves java !!aabc
    O/P: Everyone Loves Java !!aabc

    I/P: everyone loves        you
    O/P: Everyone Loves You
"""


def proper_name_case(str_val):
    return ' '.join(''.join([w[0].upper(), w[1:].lower()]) for w in str_val.split())


if __name__ == "__main__":
    original_string = "everyone loves        you"
    proper_case = proper_name_case(original_string)
    print("ORIGINAL STRING:", original_string)
    print("PROPER STRING:", proper_case)
