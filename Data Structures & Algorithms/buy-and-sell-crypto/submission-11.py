class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        sliding window Technique (Two pointer in genera;l)

        '''

        left = 0 
        max_profit = 0

        for right in range(1, len(prices)):
            profit = prices[right] - prices[left]
            
            if profit < 0:
                left = right
            max_profit = max(profit , max_profit)
        return max_profit

