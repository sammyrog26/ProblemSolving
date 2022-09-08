"""
Find the Longest Palindrome substring:

    I/P:babad
    O/P: bab

    I/P: basdaunjinddss
    O/P: dd

"""


def longest_palindrome(s):
    palindrome = ''

    # loop through the input string
    for i in range(len(s)):

        # loop backwards through the input string
        for j in range(len(s), i, -1):

            # Break if out of range
            if len(palindrome) >= j - i:
                break

            # Update variable if matches
            elif s[i:j] == s[i:j][::-1]:
                palindrome = s[i:j]
                break

    return palindrome


if __name__ == "__main__":
    str_val = "basdaunjinddss"
    print(longest_palindrome(str_val))