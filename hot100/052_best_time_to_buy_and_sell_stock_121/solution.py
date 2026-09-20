"""
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on
the ith day.

You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot
achieve any profit, return 0.

Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6),
    profit = 6-1 = 5.

Example 2:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: No transactions are done and the max profit = 0.

Constraints:
    1 <= prices.length <= 10^5
    0 <= prices[i] <= 10^4
"""

from typing import List


class Solution:
    # my original solution is totally wrong, the highest price may happen before the lowest price
    #
    # def maxProfit(self, prices: List[int]) -> int:
    #     min_price = float('inf')
    #     max_price = float('-inf')
    #     for p in prices:
    #         min_price = min(min_price, p)
    #         max_price = max(max_price, p)

    #     return max(max_price - min_price, 0)

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        prev_min = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - prev_min)
            prev_min = min(prev_min, prices[i])
        return max_profit
