class NumArray:

    def __init__(self, nums: List[int]):

        n = len(nums)
        self.pref = [0]* (n + 1)

        for i in range(1, n + 1):
            self.pref[i] = self.pref[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:

        return self.pref[right + 1] - self.pref[left]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)