# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        result = []
        while queue:
            level = []
            for i in range(len(queue)):
                root = queue.popleft()
                level.append(root.val)
                if root.left: queue.append(root.left)
                if root.right: queue.append(root.right)

            # Exiting the for Loop means That i have processed an entire level
            if level:
                result.append(level)
            

        return result


        


        