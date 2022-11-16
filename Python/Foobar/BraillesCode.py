"""
 # Braille Translation

Braille is a writing system used to read by touch instead of by sight.
Each character is composed of 6 dots in a 2x3 grid, where each dot can either be a bump or be flat (no bump).
You plan to translate the signs around the space station to Braille so that the minions under Commander Lambda's command can feel the bumps on the signs and "read" the text with their touch.
The special printer which can print the bumps onto the signs expects the dots in the following order:
1 4
2 5
3 6

So given the plain text word "code", you get the Braille dots:

11 10 11 10
00 01 01 01
00 10 00 00

where 1 represents a bump and 0 represents no bump.  Put together, "code" becomes the output string "100100101010100110100010".

Write a function solution(plaintext) that takes a string parameter and returns a string of 1's and 0's representing the bumps and absence of bumps in the input string. Your function should be able to encode the 26 lowercase letters, handle capital letters by adding a Braille capitalization mark before that character, and use a blank character (000000) for spaces. All signs on the space station are less than fifty characters long and use only letters and spaces.
Input:
"code"
Output:
    100100101010100110100010

Input:
"Braille"
Output:
    000001110000111010100000010100111000111000100010

Input:
"The quick brown fox jumps over the lazy dog"
Output:
    000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110
"""


ASCII_CODES = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z']
BRAILLES_CODE = [
    '000000',
    '100000',
    '110000',
    '100100',
    '100110',
    '100010',
    '110100',
    '110110',
    '110010',
    '010100',
    '010110',
    '101000',
    '111000',
    '101100',
    '101110',
    '101010',
    '111100',
    '111110',
    '111010',
    '011100',
    '011110',
    '101001',
    '111001',
    '010111',
    '101101',
    '101111',
    '101011']


def solution(s):
    output = ""

    for i in range(0, len(s)):
        if s[i].isupper():
            output = output + '000001'

        output = output + BRAILLES_CODE[ASCII_CODES.index(s[i].lower())]

    return output


if __name__ == "__main__":
    print(solution("The quick brown fox jumps over the lazy dog"))
