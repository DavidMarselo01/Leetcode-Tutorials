#Time Complexity: O(n^2)
#Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                max_profit = max(profit, max_profit)
                
        return max_profit