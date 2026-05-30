class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        l, r = 0, 1
        best_profit = 0

        while l < r and r < len(prices):

            if prices[l] < prices[r]:
                best_profit = max(prices[r] - prices[l], best_profit)

                r += 1
            else:
                l = r
                r = l + 1
        
        return best_profit

        # [_, _, _, _, _, _]
        #              l  r
        # best_profit = max(prices[r] - prices[l], 0)