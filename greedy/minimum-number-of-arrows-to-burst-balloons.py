class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort()
        prev = points[0]
        count = len(points)

        for i in range(1, len(points)):
            cur = points[i]

            if cur[0] <= prev[1]:
                count -= 1
                prev = [prev[0], min(prev[1], cur[1])]
            
            else:
                prev = cur

        return count