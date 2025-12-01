class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:


        #just a medium question easy
        if k % 2 == 0 or k % 5 == 0:
            return -1

        n = 0
        l = 0
        for i in range(k):
            n = n * 10 + 1
            l += 1
            if n % k == 0:
                return l
                
        return -1

            
            
        


        

        