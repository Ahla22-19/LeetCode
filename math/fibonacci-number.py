class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        rec = [0 ,1]
        for i in range (n-1):
            rec.append(rec[-2]+rec[-1])
        print(rec)
        return rec[-1]
        
        