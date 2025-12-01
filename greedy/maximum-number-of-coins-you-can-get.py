class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        piles.sort()
        m = len(piles) // 3

        ans = 0
        for i in range(m, len(piles) ,2):
            ans += piles[i]
        
        return ans



            


        