import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    # list given isnot heap (doesn't maintain heap property --> Parent <= childrens)
    # first convert th list to a heap using the hepify method --> (O(n) Time)
    # list nums now become a heap (heapifying is done in place)
    
    '''
    Algorithm: getting reversed order requires having a maximum heap fromm the min heap
        1- heapifying the list --> obtain the min heap
    '''
    max_heap = []
    result = []
    for num in nums:
        heapq.heappush(max_heap , -num)

    while max_heap:
        result.append(-heapq.heappop(max_heap))
    
    return result




# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
