class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:


        total_sum = 0
        max_sum = float("-inf")

        for i in range(k):
            total_sum += nums[i]
            
        left = 0
        max_sum = total_sum

        for r in range(k, len(nums)):
            total_sum += nums[r]
            total_sum -= nums[left]

            max_sum = max(max_sum, total_sum)
            left += 1

        return max_sum / k



            

        

       


        