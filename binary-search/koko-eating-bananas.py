class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def isValid(mid):
            hour = 0
            for bananas in piles:
                hour += ceil(bananas/mid)
            return hour <= h

        low = 1
        high = max(piles)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            if isValid(mid):
                ans = mid
                high = mid - 1

            else:
                low = mid + 1

        return ans
