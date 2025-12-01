# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def oddreverse(root):

            if not root:
                return []

            index = 0
            queue = deque([root])

            while queue:
                level = []
                for i in range(len(queue)):
                    node = queue.popleft()
                    level.append(node)

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                if index % 2 == 1:
                    left = 0
                    right = len(level) - 1
                    while left < right:
                        level[left].val, level[right].val = level[right].val, level[left].val
                        left += 1
                        right -= 1
                index += 1

            return root

        return oddreverse(root)
                    
