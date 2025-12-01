class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        e = set(nums)
        for i in e:
            n = nums.count(i)
            count += n * (n-1) // 2
        return count