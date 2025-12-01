class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        max_ = deque() #monotonic decreasing 
        min_ = deque() #monotonic increasing
        left = 0
        ans = 0

        for right in range(len(nums)):

            while max_ and nums[right] > max_[-1]:
                max_.pop()

            while min_ and min_[-1] > nums[right]:
                min_.pop()            

            min_.append(nums[right])
            max_.append(nums[right])

            while max_[0] - min_[0] > limit:
                if nums[left] == max_[0]:
                    max_.popleft()
                if nums[left] == min_[0]:
                    min_.popleft()
                left += 1

            ans = max(ans, right - left + 1)

        return ans
            