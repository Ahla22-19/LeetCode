class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        ans = 0
        count = 0

        for i in range(len(s)):
            
            if s[i] == "R":
                count += 1

            else:
                count -= 1
            
            if count == 0:
                ans += 1

        return ans