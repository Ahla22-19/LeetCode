# A number can have four divisors iff it is prime^3 or if it is the product of two distinct prime numbers

class Solution:
    def is_prime(self, n: int) -> bool:
        if n < 2:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True
            
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        
        for x in nums:
            # Case 1: x = p^3 where p is prime
            p = round(x ** (1 / 3))
            if p * p * p == x and self.is_prime(p):
                total += 1 + p + p * p + x
                continue

            # Case 2: x = p * q where p != q and both are prime
            p = 2
            while p * p <= x:
                if x % p == 0:
                    q = x // p
                    if p != q and self.is_prime(p) and self.is_prime(q):
                        total += 1 + p + q + x
                        break
                p += 1

        return total