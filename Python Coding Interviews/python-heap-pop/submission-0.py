import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    # By deafult the heap is the minimum heap in python
    result = []
    while heap:
        # 1- pop the smallest priority element from heap
        # 2- insert the removed element in the list
        result.append(heapq.heappop(heap))
    return result


# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
