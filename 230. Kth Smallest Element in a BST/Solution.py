# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(root: TreeNode):
            nonlocal kthNode 
            nonlocal k
            if not root or k < 0:
                return
            helper(root.left)
            k -= 1
            if k == 0:
                kthNode = root.val
                return
            helper(root.right)
        kthNode = 0
        helper(root)
        return kthNode
        