class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        l, r = 0, 1
        best_profit = 0

        while l < r and r < len(prices):
            best_profit = max(max(0, prices[r] - prices[l]), best_profit)
            print("bp: ", best_profit)
            print("l: ", l)
            print("prices[l]: ", prices[l])
            print("r: ", r)
            print("prices[r]: ", prices[r])
            print("**********")

            if prices[l] < prices[r]:
                r += 1
            else:
                l += 1
                r = l + 1
        
        return best_profit

        # [_, _, _, _, _, _]
        #              l  r
        # best_profit = max(prices[r] - prices[l], 0)