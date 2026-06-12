class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        buy = prices[0]

        for i in range(1, len(prices), 1):
            buy = min(buy, prices[i])
            
            profit = prices[i] - buy
            maxP = max(maxP, profit)
        
        return maxP
        