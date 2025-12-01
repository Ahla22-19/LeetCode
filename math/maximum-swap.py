class Solution:
    def maximumSwap(self, num: int) -> int:
        v=num
    
        if (s:=str(v)) == (S:=''.join(sorted(s)[::-1])): return v

        i = next(i for i,(p,q) in enumerate(zip(S,s)) if p!=q)

        return int(s[:i]+s[j:=s.rfind(S[i])]+s[i+1:j]+s[i]+s[j+1:])


        