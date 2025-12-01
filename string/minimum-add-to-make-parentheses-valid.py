class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count1=0   #counts "(" parenthesis
        count2=0   #counts ")" parenthesis
        for i in range(len(s)):
            if s[i]=="(":
                count1+=1
            else:
                if count1>0:
                    count1-=1
                else:
                    count2+=1
        return count1+count2

        