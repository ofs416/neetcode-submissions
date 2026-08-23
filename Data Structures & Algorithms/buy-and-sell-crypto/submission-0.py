class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i, buy in enumerate(prices):
            for j, sell in enumerate(prices[i+1:]):
                profit = sell-buy
                max_profit = profit if profit > max_profit else max_profit

        return max_profit