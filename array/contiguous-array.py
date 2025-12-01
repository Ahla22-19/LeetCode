class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        max_len = 0
        my_dict = {0:-1}
        count = 0

        for i in range (len(nums)):

            if nums[i] == 1:
                count += 1
            else:
                count -= 1

            if not count in my_dict:
                my_dict[count] = i

            else:
                max_len = max(max_len, i  - my_dict[count])

        return max_len
            

