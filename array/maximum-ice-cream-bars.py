class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        costs.sort()
        count = 0
        total = 0

        for i in range(len(costs)):
            total += costs[i]
            if total <= coins:
                count += 1
        
            
        return count


