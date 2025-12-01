class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=1
        while l<len(nums):
            a=int(nums[l])
            if r==len(nums) and a!=int(nums[l-1]):
                return a
            elif r<len(nums) and a==int(nums[r]):
                l=r+1
                r=l+1
            else:
                return a
                break