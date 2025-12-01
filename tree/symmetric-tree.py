# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isMirror(left_tree, right_tree):

            if not left_tree and not right_tree:
                return True
            if not left_tree or not right_tree:
                return False
            
            if right_tree.val != left_tree.val:
                return False

            return (isMirror(left_tree.left, right_tree.right) and 
            isMirror(left_tree.right, right_tree.left))
        
        return isMirror(root, root)