# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return
        # Phase-1 Swap the left nd right childerns
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # Phase-2: Call Recusively the function to invert each subtree recusrsively

        self.invertTree(root.left)
        self.invertTree(root.right)

                
        return root

