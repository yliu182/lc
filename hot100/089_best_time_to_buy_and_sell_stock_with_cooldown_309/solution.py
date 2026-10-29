"""
309. Best Time to Buy and Sell Stock with Cooldown

You are given an array prices where prices[i] is the price of a given stock on
the ith day. Find the maximum profit you can achieve. You may complete as many
transactions as you like (i.e., buy one and sell one share of the stock multiple
times) with the following restrictions:
    - After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

Note: You may not engage in multiple transactions simultaneously (i.e., you must
sell the stock before you buy again).

Example 1:
    Input: prices = [1,2,3,0,2]
    Output: 3
    Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:
    Input: prices = [1]
    Output: 0

Constraints:
    - 1 <= prices.length <= 5000
    - 0 <= prices[i] <= 1000
"""

from typing import List


class Solution:
    '''
    推荐使用状态机动态规划。每天结束时只有三种状态：
    hold：手里持有股票
    sold：今天刚卖出股票
    rest：手里没有股票，并且今天没有卖出
    状态转移：
    新的 hold = max(
        昨天已经持有,
        昨天处于 rest 状态，今天买入
    )

    新的 sold = 昨天持有股票，今天卖出

    新的 rest = max(
        昨天已经处于 rest,
        昨天刚卖出，今天冷冻休息
    )
    用价格表示就是：
    hold = max(previous_hold, previous_rest - price)
    sold = previous_hold + price
    rest = max(previous_rest, previous_sold)
    最关键的是：买入只能从昨天的 rest 转移到 hold，不能从昨天的 sold 买入。这正好体现卖出后的第二天不能买入。
    初始状态：
    hold = -prices[0]  # 第一天买入
    sold = 负无穷      # 第一天不可能完成卖出
    rest = 0           # 第一天什么都不做
    '''

    '''
    has a series bug

    def maxProfit(self, prices: List[int]) -> int:
        cash_ready_to_buy = 0
        cash_just_sold = float('-inf')
        stock = -prices[0]

        for i in range(1, len(prices), 1):
            cash_ready_to_buy = max(
                cash_ready_to_buy,
                cash_just_sold,
            )
            cash_just_sold = stock + prices[i]
            stock = max(
                stock,
                cash_ready_to_buy - prices[i]
            )

        return max(cash_ready_to_buy, cash_just_sold)
    '''

    def maxProfit(self, prices: List[int]) -> int:
        cash_ready_to_buy = 0
        cash_just_sold = float('-inf')
        stock = -prices[0]

        for price in prices[1:]:
            previous_cash_ready_to_buy = cash_ready_to_buy
            previous_cash_just_sold = cash_just_sold
            previous_stock = stock

            cash_ready_to_buy = max(
                previous_cash_ready_to_buy,
                previous_cash_just_sold,
            )
            cash_just_sold = previous_stock + price
            stock = max(
                previous_stock,
                previous_cash_ready_to_buy - price
            )

        return max(cash_ready_to_buy, cash_just_sold)
