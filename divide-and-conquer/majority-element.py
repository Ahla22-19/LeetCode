class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        nums = Counter(nums)

        
        for num, repeat in nums.items():
            if repeat > n / 2:
                return num
                break

