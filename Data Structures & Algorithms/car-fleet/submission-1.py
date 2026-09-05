class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        I- Algorithm Main Idea: -> uses a Stack
            - Speed -> Represents the Slope of the Graph (velocity = distance/time)
            - If there exist intersection between the graphs -> represent a car fleet
                a- Intesecting means that the slower car will catch the up head car in speed
            - No Intersection: -> slower car won't catch up the up head car 
            - Alogorithmic way of computuing the Intersection -> compute the Time between cars
                a- Time of slower car <= (closely) to Time of faster car uphead:
                    - means that slower car will catch up the next faster car -> considered car fleet
                b- Time of slower car > (farly large) from Time of faster car uphead:
                    - means that slower car will never catch the next faster car uphead
            - since that cars won't pass each other (they can only have the same position and speed) if they
            catch another car (and Considered a car fleet) -> they maintain the relative sorted order
       
        II- Algorithmic Implementation:
            a- Traverse the array from the right to left (Traverse array from end)
            b- Compute the Intersection point -> Time for car to reach the target destination
            c- compare time for given element with top of stack
                case-1: Time taken for given element <= time of car top of stack -> intersection occur
                    a- Pop the Top of stack
                    b- insert that given element   (Considered a car fleet)
            d- Push element to stack
            Trick: 
                a- sort the array (according to the position)
                b- Traverse the array from right to left

        III- Time Complexity: -> O(n*logn)
            - due sorting + actually 
            - Traversing the array + computing time taken to reach destination: O(n)
        
        IV- Space Complexity: -> O(n)
            - using a Stack 
        '''
        




        stack = []
        # step-1: build a list of Tuples having the following format = [(pos1,sp1) , (pos2,sp2),...]
        pos_speed = [(p,s) for p, s in zip(position, speed)]
        #for pos , sp in zip(position,speed):
        #    pos_speed.append((pos,sp))
        
        # Step-2: Maintain the Realtive Sorted Order in place (sort according to the Position -> Tuple[0])
        pos_speed.sort(key = lambda x: x[0] , reverse = False)

        # Step-3: Traverse the Array from the Right to Left
        for i in range(len(pos_speed) - 1 , -1 ,-1):
            # Step-4: Compute time Taken to get to destination + append reuslt to stack
            stack.append((target - pos_speed[i][0]) / pos_speed[i][1])

            # Step-5: comparison + Poping Phase(time of new element <= time of top stack -> collision occur)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


           
            















