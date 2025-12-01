# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # changing to sorted array using inorder
        nums = []
        def tolist(root):
            if not root:
                return None

            tolist(root.left)
            nums.append(root.val)
            tolist(root.right)

        tolist(root)

        # constructing TreeNode using the sorted array
        def toTree(nums):
            mid = len(nums) // 2

            if not nums:
                return None

            root = TreeNode(nums[mid])
            root.right = toTree(nums[mid + 1:])
            root.left = toTree(nums[:mid])
                
            return root

        return toTree(nums)