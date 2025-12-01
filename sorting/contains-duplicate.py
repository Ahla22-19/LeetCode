class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        nums_map = Counter(nums)
        return any(value for char, value in nums_map.items() if nums_map[char] >= 2)

        