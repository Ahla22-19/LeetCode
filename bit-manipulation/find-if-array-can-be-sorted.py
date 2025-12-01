class Solution:
    def canSortArray(self, nums: List[int]) -> bool:

        if nums == sorted(nums):
            return True

        for j in range(len(nums)):

            for i in range(len(nums)-j-1):

                if nums[i] > nums[i+1]:
                
                    if bin(nums[i]).count("1") == bin(nums[i + 1]).count("1"):
                        nums[i] , nums[i+1] = nums[i+1] , nums[i]

                    else:
                        return False

        return True
    

