class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        costs = sorted(costs, key=lambda x: x[0] - x[1])

        ans = 0
        balance = len(costs) // 2

        for i in range(balance):
            ans += (costs[i][0] + costs[len(costs) - 1 - i][1])

        return ans




            
        
        