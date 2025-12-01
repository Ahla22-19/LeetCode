class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        remainder = {0:1}
        count = 0
        prefix = 0

        for num in nums:
            prefix += num
            r = prefix % k 

            if r in remainder:
                count += remainder[r]

            remainder[r] = remainder.get(r, 0) + 1   


        return count
             
        
