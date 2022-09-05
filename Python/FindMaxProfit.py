"""
Find and return the maximum profit you can achieve.


Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 7
    Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
                Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
    Total profit is 4 + 3 = 7.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
"""


def max_profit(prices):
    if not prices:
        return
    profit = 0
    for i in range(1, len(prices)):
        profit += max(prices[i] - prices[i - 1], 0)
    return profit


if __name__ == "__main__":
    list_stocks = [7, 1, 5, 3, 6, 4]
    print(max_profit(list_stocks))

