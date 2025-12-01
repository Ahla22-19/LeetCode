class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        ans = []
        total = sum(num for num in nums if num % 2 == 0)
        
        for added, index in queries:
            prev = nums[index]
            nums[index] += added

            if prev % 2 == 0:
                if nums[index] % 2 == 0:
                    total += added
                else:
                    total -= prev

            else:
                if nums[index] % 2 == 0:
                    total += nums[index]

            ans.append(total)
        
        return ans
                

        