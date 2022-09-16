"""
Find if the given number is armstrong number

    I/P: 153
    O/P: True
    Explanation:
        153:    1*1*1 + 5*5*5 + 3*3*3 = 153

    I/P: 256
    O/P: False
    Explanation:
        153:    2*2*2 + 5*5*5 + 3*3*3 = 160

    I/P: 1634
    O/P: True
    Explanation:
        1634:    1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4 = 1634
"""


def armstrong(int_val):
    if not int_val:
        return
    val = [x for x in str(int_val)]
    number_length = len(str(int_val))
    sum = 0
    for each in val:
        # We can use pow as well
        # sum += pow(int(each), number_length)
        sum += find_power_of_three(int(each), number_length)
    if sum == int_val:
        return True
    else:
        return False


def find_power_of_three(base, power):
    x = 1
    for i in range(power):
        x *= base
    return x


def armstrong_number(num):
    """
        Time Complexity O(n):
    """
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if num == sum:
        return True
    return False


if __name__ == "__main__":
    print(armstrong_number(1634))
