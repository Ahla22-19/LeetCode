class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def isValid(mid):
            current = 0
            day = 1

            for weight in weights:
                if current + weight <= mid:
                    current += weight

                else:
                    current = weight
                    day += 1

            return day <= days

        low = max(weights)
        high = sum(weights)
        ans = high 

        while low <= high:
            mid = (low + high) // 2

            if isValid(mid):
                ans = mid
                high = mid -1
    
            else:
                low = mid + 1

        return ans

        