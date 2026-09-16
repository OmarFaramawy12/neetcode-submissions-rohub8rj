class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        Main Idea:
            - Exist N Piles in Array (Number of Piles = Length of the Array)
            - Each Pile must take 1 Hour of eating (Hardcoded):
                a- Case-1: pile contain a small number of bananas to eat (e.g 1 banana in pile):
                    - eating it will take very small amount of time (epsion min or sec)
                    - koko must stay there until one hour finishes to advance to next pile

                b- Case-2: Pile Contain very large number of bananas that 1 hour won't finish it:
                    - Number ofhours to finish that pile = number of bananas in pile / Rate of eating
            - Note: Exist several Rates you can finish the Total Piles in lesss than given Number of 
            hours (h) -> Return min amount of rate 

            - Several Aspects:
                Rule: len(piles) <= Hours:
                    - that means minimum number of hours to finsih whole piles is bounded minimally 
                    be the number of piles in the array
                    -e.g: Having 4 piles -> minmum no of hours to finish it on the assumption of 1 
                    hour per pile -> 4 Hours (each pile Take 1 hour)

                -Question: What if we eat at rate k where k > maximum number of bananas in a pile?
                (aka: max piles array)? How much timewe will finish all piles??
                    - since number of hours Bounded to Number of piles in array (len(piles) <= Hours)
                    - then if we ate at the maximum rate or grater -> we will still finsih on n hours
                    where n = len(piles)

                    -e.g in the following ex: having max_n_banans = 11 in a given pile
                        - if we ate 11 bananas per hour -> we will finsih all piles at 4 hours (len 
                        of piles)
            II- Main Question to Form the algorithm:

                1- What is the maximum and minimum Range (search range) (aka: smallest number of 
                bananas and the maximum number of banas) to eat per hour??
                    a- minmum number of bananas is 1 banana per hour
                    b- maximum number banana is bounded by maximum number of bananas per pile

                2- Given the searvh range (Rates of bananas per hour):
                    - there exist rates  that will gives us the minimum hours (recall min hours 
                    bounded by number of piles) (MAx Rate)
                    - exist rates that will actually surpass the given time to  finish all the piles 
                    (like eating 1 banana every 1 hour) (min Rate)

            III-: Core Algorithm
                1- Given A search Range you will apply the Binary Search to eliminate half of the 
                sratcj space
                
                2- choose given Rate K (according to algorithm):
                    a- compute the Total Number of hours to finish all piles:
                        - Step-1: Loop over array of pile and for each pile
                            -Step-2: Divide the number of bananas / rate (k)
                            -Step-3: Accumlate the Number of Hours for the wholw array 
                    
                    b- Exist 2 Cases

                        Case-1: Computed Number of Hours > hours given:
                            - we are going so slow -> increase rate
                            - discard the left portion-> serch in right portion
                                left = mid (k) + 1
                        Case-2: Computed Number of Hours <= hours given:
                            - the Rate is good
                            - Goal: find the min Rate (decrease rate)
                            - Discard the Right Portion (search the left portion):
                                right = mid(k) -1 
                3- Retrun min
        '''



        left , right = 1 , max(piles)       # max -> O(n)

        minRate = right
        while left <= right:
            # mid = k
            mid = left + (right - left) // 2
            hours = 0
            
            for pile in piles:
                # Step-1: Compute the Total Number of hours of the whole array at given rate k (mid)
                hours += math.ceil(pile / mid)
            # Case: going very slow on rate (increase rate)
            if hours > h:
                left = mid + 1
            # Case: Rate is good (Goal: Find minimum) -> Search the left portion of array    
            else:
                minRate = min(minRate , mid)
                right = mid - 1
        return minRate







