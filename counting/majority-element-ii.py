class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        nums = Counter(nums)
        ans = []

        for num, repeat in nums.items():
            if repeat > n / 3:
                ans.append(num)
        
        return ans

