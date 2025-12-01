class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        
      
        dict_nums = Counter(nums)
        return [num for num, val in dict_nums.items() if dict_nums[num] > 1]
