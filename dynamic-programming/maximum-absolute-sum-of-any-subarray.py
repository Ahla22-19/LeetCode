class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:

        ans = 0
        max_pre = 0 
        min_pre = 0

        for num in nums:
            ans += num

            max_pre = max(max_pre, ans)
            min_pre = min(min_pre, ans)

        return max_pre - min_pre



            