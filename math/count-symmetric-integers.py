class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        count = 0
        for j in range(low, high + 1):
            s = str(j)

            if len(s) % 2 == 0:

                a = 0
                b = 0
                for i in range(len(s)//2):
                    a += int(s[i])
                for i in range(len(s)//2, len(s)):
                    b += int(s[i])
                    
                if a == b:
                    count += 1

        return count
