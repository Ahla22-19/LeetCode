class Solution:
    def printVertically(self, s: str) -> List[str]:

        words = s.split()

        n = len(max(words, key = len))
        ans = []

        for i in range(n):
            
            curr = ''
            for word in words:
                if len(word) > i:
                    curr += word[i]
                else:
                    curr += ' '
            ans.append(curr.rstrip())
        
        return ans 
        