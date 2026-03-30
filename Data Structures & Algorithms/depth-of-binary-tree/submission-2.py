# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # phase-1: initialize queue
        queue = deque()
        queue.append(root)

        # Phase-2: Loop over queue
        level = 0
        while queue:
            for i in range(len(queue)):

                root = queue.popleft()
                if root.left: queue.append(root.left)
                if root.right: queue.append(root.right)
            level += 1

        return level



        
        