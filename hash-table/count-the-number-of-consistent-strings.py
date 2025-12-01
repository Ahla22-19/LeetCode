class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        ans = 0

        for word in words:
            Flag = True
            for w in set(word):
                if not w in set(allowed):
                    Flag = False
            if Flag :
                ans += 1
        return ans
                
            