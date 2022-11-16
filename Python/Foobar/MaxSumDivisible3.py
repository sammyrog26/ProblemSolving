"""
# please-pass-the-coded-messages:

You have L, a list containing some digits (0 to 9).
Write a function solution(L) which finds the largest number that can be made from some or all of these digits and is divisible by 3.
If it is not possible to make such a number, return 0 as the solution. L will contain anywhere from 1 to 9 digits.
The same digit may appear multiple times in the list, but each element in the list may only be used once.

Input:
{3, 1, 4, 1}
Output:
    4311

Input:
{3, 1, 4, 1, 5, 9}
Output:
    94311

Input:
[3, 1, 4, 1]
Output:
    4311

Input:
[3, 1, 4, 1, 5, 9]
Output:
    94311
"""


def solution(l):
    if not l:
        return 0
    if sum(l) % 3 == 0:
        return sum(d * 10 ** i for i, d in enumerate(sorted(l)))
    return max(solution(l[:i] + l[i + 1:]) for i, d in enumerate(l) if d % 3)


if __name__ == "__main__":
    solution([3, 1, 4, 1])