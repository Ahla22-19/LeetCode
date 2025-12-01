class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        def binary_search(l, r, target):
            while l <= r:
                m = (l+r)//2
                if nums[m] >= target:
                    r = m - 1
                else:
                    l = m + 1
            return r

        nums.sort()
        count = 0
        l = 0
        r = len(nums)-1
        for i in range(len(nums)):
            low = lower - nums[i]
            up = upper - nums[i]

            count += (
                binary_search( i + 1, len(nums) - 1, up + 1) -
                binary_search(i + 1, len(nums) - 1, low))
        
        return count