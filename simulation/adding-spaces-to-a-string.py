class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        ss = [ ]
        p1 = 0
        p2 = 0 

        while p2 < len(spaces) and p1 < len(s):
            if p1 != spaces[p2]:
                ss.append(s[p1])
                p1 += 1
            if p1 == spaces[p2]:
                ss.append(" ")
                p2 += 1

        for i in range (p1 , len(s)):
            ss.append(s[i])

        return "".join(ss)

