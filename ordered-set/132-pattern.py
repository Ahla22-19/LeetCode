class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        stack = []
        i = float("-inf")

        for num in reversed(nums):

            if i > num:
                return True

            while stack and stack[-1] < num:
                i = stack.pop()

            stack.append(num)
            
        return False

           
            
            

        