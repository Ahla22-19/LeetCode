class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i]=nums[i-1]+nums[i]
        print(nums)
        if nums[0]==nums[-1]:
            return 0
        l=1
        r=-1
        while l<len(nums):
            if nums[r]-nums[l]==nums[l-1]:
                return l
                break
            else:
                l+=1
        else:
            return -1

