class Solution:
    def countGoodNumbers(self, n: int) -> int:

        mod = 10**9 + 7
        def pow(x, n):
            if n == 0:
                return 1
           
            res = pow(x, n//2)
            return (x * res * res) % mod if n % 2 else (res * res) % mod
            
        a = (n + 1)//2
        b = n // 2
        ans = (pow(5, a) % mod) * (pow(4, b) % mod)

        return ans % mod
        