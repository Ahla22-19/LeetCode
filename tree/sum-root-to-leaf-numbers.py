# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        ans = []

        def Sum(root, val):

            if not root:
                return None

            if not root.left and not root.right:
                ans.append(val * 10 + root.val)
            
            Sum(root.left, val * 10 + root.val)
            Sum(root.right, val * 10 + root.val)

            return sum(ans)

        return Sum(root, 0)

          


            
        