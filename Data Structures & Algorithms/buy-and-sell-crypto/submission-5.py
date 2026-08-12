class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        profit -> 1- buy rhing with small price
                  2- sell it with huge price
                  3- must buy first then sell --> on any given index (day) -> buying will occur + selling will occur 
                  on [(i+1) - > nth] day
                  4- Mathematics:
                        profit = selling - buying (maximize selling + minimize buying) (right - left)
                        - selling: will occur at the right index
                        - buying: will occur ar the left index 
                    
        '''
        


        left , right = 0 , 1 # right will always preced the left
        max_profit = 0
          
        while right < len(prices):
            if prices[left] < prices[right]:                
                # make the transaction
                profit = prices[right] - prices[left]
                max_profit = max(max_profit , profit)
            # case where we can't make the transaction
            else:
                left  = right

            right +=1
        return max_profit
