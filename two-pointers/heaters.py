class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        
        l = 0
        r = 10**10
        
        def helper(r):
            
            heat = [0]* (len(houses)+1)
            
            for heater in heaters:
                left = bisect_left(houses, heater - r)
                right = bisect_right(houses, heater + r)

                heat[left] += 1
                heat[right] -= 1
            

            if heat[0] == 0:
                return False

            for i in range(1, len(houses)):
                heat[i] = heat[i-1] + heat[i]
                if heat[i] == 0:
                    return False
            
            return True
            

        while l<=r:
            m=l+(r-l)//2
            
            if helper(m):
                r=m-1
            else:
                l=m+1

        return r + 1