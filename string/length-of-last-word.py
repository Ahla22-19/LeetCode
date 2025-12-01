class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        i = len(s) - 1
        while not s[i].isalpha():
            i -= 1

        count = 0
        while i > -1 and s[i].isalpha():
            count += 1
            i -= 1
       
        return count

        
            
        