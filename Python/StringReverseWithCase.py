"""
Display reverse of a given string including cases
eg:
    I/P: DaTa
    O/P: aTaD

    I/P: TELECOM
    O/P: MOCELET
"""


def reverse_string(str_val):
    str_val = str(str_val)
    s1 = ''
    for c in str_val:
        s1 = c + s1  # appending chars in reverse order
    return s1


print(reverse_string("WelCome"))
