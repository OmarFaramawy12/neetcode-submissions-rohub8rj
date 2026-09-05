class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Problem Formulation: -> Decreasing Monotonick Stack
            - Objective: find the next greater (aka: Warmer) temprature after the i-th day (find the next warmer 
            Temprature in the future)
            - Monotonic Decreasing Stack -> Design Princibles: must achieve Monotonic Property
                a- The stack will be Non-Increasing
                b- elements on the stack will be waiting for reservation until finding the next greater 
                element that beats up the current element on stack
                c- Case Succeded: if i-th element in array beats up the waiting temps -> a- pop all the beated temps
                                                                                         b- insert the new element
                d- Case Failed: (i-th element doesn't beat up the waiting element in stack) -> push element to stack
        (Last-Step)    e- Reached the End of the array + exist elements in the stack -> fill indices with zeros
        Note: 1- Elements wont remove from stack untill finding the next greater
              2- Stack will contain indices


        II- Time Complexity: -> O(n)
        III- Space Complexity: O(n)

        '''           # 0    1    2    3    4    5    6     7   8     9
       #temperatures = [ 89 , 62 , 70 , 58 , 47 , 47 , 46 , 76 , 100 , 70 ]      stck = []
       #output = []

        stack = []
        result = [0] * len(temperatures)
        # Monontonic Non-Decreasing Stack
        for i , num in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < num:
                result[stack[-1]] = (i - stack[-1])
                stack.pop()
            stack.append(i)
        
        return result
       

        
