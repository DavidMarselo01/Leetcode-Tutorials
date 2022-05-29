#Time Complexity: O(n)
#Space Complexity: O(1)
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0
        max_profit = 0
        for right in range(1, len(prices)):
            profit = prices[right] - prices[left]
            if profit < 0:
                left = right
            elif profit > 0:
                max_profit = max(max_profit, profit)
                
        return max_profit