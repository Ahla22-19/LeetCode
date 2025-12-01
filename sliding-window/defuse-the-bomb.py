class Solution:
    def decrypt(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        res = [0] * n
        cur_sum = 0
        l = 0

        for r in range (n + abs(k)):
            cur_sum += nums[r % n]

            if r - l + 1 > abs(k):
                cur_sum -= nums[l % n]
                l = (l + 1) % n

            if r - l + 1 == abs(k):
                if k > 0:
                    res[(l -1) % n] = cur_sum
                elif k < 0:
                    res[(r+1) % n] = cur_sum

        return res  






 
        