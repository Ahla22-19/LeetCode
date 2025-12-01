class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 1
        if len(nums) == 1:
            return 1
        while r < len(nums):
            a = nums[l]
            b = nums[r]
            if a == b:
                r+=1
            else:
                l+=1
                nums[l], nums[r] = nums[r], nums[l]
                r+=1
        print(nums)
        return l + 1