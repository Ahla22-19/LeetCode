class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        ans = float('-inf')

        for left in range(len(nums)):
            left2 = left + 1
            right = len(nums) - 1

            while left2 < right:

                if abs(nums[left] + nums[left2] + nums[right] - target) < abs(ans - target) :
                    ans = nums[left] + nums[left2] + nums[right]

                if nums[left] + nums[left2] + nums[right] > target:
                    right -= 1

                elif nums[left] + nums[left2] + nums[right] < target:
                    left2 += 1

                else:
                    return nums[left] + nums[left2] + nums[right]

        return ans