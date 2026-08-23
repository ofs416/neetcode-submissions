class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_l, sell_r = 0, 1
        max_prf = 0
        while sell_r < len(prices):
            buy, sell = prices[buy_l], prices[sell_r]
            if buy < sell:
                max_prf = max(max_prf, sell - buy)
            else:
                buy_l = sell_r
            sell_r += 1
        return max_prf