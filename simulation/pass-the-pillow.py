class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        #full-pass = 2*(n-1)

        pass_compeleted = time//(n - 1)
        remainder_pass = time % (n - 1)

        if pass_compeleted % 2 == 0:
            return remainder_pass + 1
        else:
            return n - remainder_pass 
        