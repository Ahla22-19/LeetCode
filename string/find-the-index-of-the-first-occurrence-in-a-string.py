class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if not (needle in haystack):
            return -1 
        
        ans = 0

        for i in range(len(haystack)):
            if haystack[i:i + len(needle)] == needle:
                return i
                