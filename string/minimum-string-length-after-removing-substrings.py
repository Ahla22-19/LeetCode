class Solution:
    def minLength(self, s: str) -> int:
        e=[]
        for c in s:
            if not e:
                e.append(c)
                continue
            if c=='B' and e[-1]=='A':
                e.pop()
            elif c=='D' and e[-1]=='C':
                e.pop()
            else:
                e.append(c)
        return len(e)


          
        