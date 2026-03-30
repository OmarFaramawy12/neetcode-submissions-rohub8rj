'''
    Algorithm: Sliding Window
    Time Complexity: O(n)
    Space Complexity: O(1)
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # intialize variables
        left = 0
        max_profit = 0
        
        # Loop over the Array to find Subarray with maximum profit using th eright pointer
        for right in range(left+1 , len(prices)):
            # Track the minimum price as this is the best day to buy Neetcoin
            min_price = min(prices[left] , prices[right])
            
            while prices[left] > min_price:
                left +=1

            if left == right:
                continue

            transaction = prices[right] - prices[left]
            max_profit = max(max_profit , transaction)
        return max_profit
            


        

        
        