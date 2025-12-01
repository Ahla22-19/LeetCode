class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:

        def is_prime(n):
            for i in range(2,int(sqrt(n))+1):
                if n%i==0:
                    return False
            return True

        prev = 0
        for n in nums:
            bound = n - prev
            largest_prime = 0

            for i in reversed(range(2,bound)):
                if is_prime(i):
                    largest_prime = i
                    break

            if n - largest_prime <= prev:
                return False

            prev = n - largest_prime

        return True

            
            