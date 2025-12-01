class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sub_arr = nums[0]
        cur_sum = 0

        for num in nums:
            if cur_sum < 0:
                cur_sum = 0

            cur_sum += num
            max_sub_arr = max(max_sub_arr, cur_sum)

        return max_sub_arr
                          