class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        minimum = abs(min(nums))
        maximum = max(nums)
        counter = [0 for i in range(maximum + minimum + 1)]

        for num in nums:
            counter[num + minimum] += 1

        j = 0
        for index, value in enumerate(counter):
            for i in range(value):
                nums[j] = index - minimum
                j += 1

        return nums
        

        