"""
1 Quarter----> 25 Cents
1 Dine   ----> 10 Cents
1 Nickle ----> 5 Cents
1 Penny  ----> 1 Cent

Calculate Min Count to satisfy Cents
Eg: 33
    25 ---> 1
    10 ---> 0
    5  ---> 1
    3  ---> 3
Count = 5
"""


def count_cents(cents):
    if cents == 0:
        return 0
    coins = [25, 10, 5, 1]
    coin_count = 0
    for coin in coins:
        coin_count += cents // coin
        cents = cents % coin
        if cents == 0:
            break
    return coin_count


if __name__ == "__main__":
    print(count_cents(31))
