"""
Find Fibonacci for a integer value provided
eg:
    I/P: 10
    O/P: 0 1 1 2 3 5 8 13 21 34
"""


def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        a = 0
        b = 1
        print(a)
        print(b)
        for _ in range(b, num - 1):
            c = a + b
            print(c)
            a = b
            b = c


if __name__ == "__main__":
    fibonacci(5)
