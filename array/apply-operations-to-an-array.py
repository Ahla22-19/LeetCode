class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            if i > 0 and nums [i -1] == nums[i]:
                nums[i-1] = nums[i-1] * 2
                nums[i] = 0 

        ans = []
        for i in range(len(nums)):
            if nums[i] > 0 :
                ans.append(nums[i])

        count_zeros = len(nums) - len(ans)
        for i in range(count_zeros):
            ans.append(0)
            
        return ans
                  
        