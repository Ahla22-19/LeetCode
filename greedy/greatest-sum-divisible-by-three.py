from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        #///////////////////////////
        total = sum(nums)
        rem1 = sorted([x for x in nums if x % 3 == 1])
        rem2 = sorted([x for x in nums if x % 3 == 2])
        
        r = total % 3
        if r == 0:
            return total
        
        res = 0
        if r == 1:
            option1 = total - rem1[0] if rem1 else 0
            option2 = total - sum(rem2[:2]) if len(rem2) >= 2 else 0
            res = max(option1, option2)
        else:  # r == 2
            option1 = total - rem2[0] if rem2 else 0
            option2 = total - sum(rem1[:2]) if len(rem1) >= 2 else 0
            res = max(option1, option2)
        
        return res
