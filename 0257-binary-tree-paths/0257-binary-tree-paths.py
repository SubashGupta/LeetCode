# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        d={}
        op=[]
        temp= ''
        def path(d,root, temp):
            if temp == '':
                d[root.val] = str(root.val)
            else: 
                d[root.val] = temp +'->'+ str(root.val)
            temp = d[root.val]
            if not root.left and not root.right:
                op.append(temp)
            if root.left:
                path(d, root.left, temp)
            if root.right:
                path(d,root.right, temp)
        path(d,root ,temp)
        return op        