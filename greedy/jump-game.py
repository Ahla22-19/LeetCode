class Solution:
    def canJump(self, nums: List[int]) -> bool:

        target = len(nums) - 1
        max_ = 0

        for i in range(len(nums)):

            if i > max_:
                return False

            max_ = max(max_, i + nums[i]) 

        return True



    