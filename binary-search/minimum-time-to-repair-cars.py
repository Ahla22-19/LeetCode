class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def isValid(mid):
            car = 0
            for rank in ranks:
                car += int(sqrt(mid / rank))
            return car >= cars
 
        low = 1
        high = min(ranks) * cars * cars
        ans = high

        while low <= high:
            mid = (low+high)//2

            if isValid(mid):
                ans = mid
                high = mid - 1

            else:
                low = mid + 1 

        return ans