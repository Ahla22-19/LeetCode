class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        def isequal(s, p):
            for i in p:
                if not i in s or s[i] != p[i]:
                    return False
            return True
        l,r =0, len(p)
        ans = []
        k=defaultdict(int)
        j = defaultdict(int)
        for i in p:
            k[i] += 1
        for i in range(len(p)):
            j[s[i]] += 1
        if isequal(j, k):
            ans.append(l)
        while r < len(s):
            j[s[l]] -= 1
            j[s[r]] += 1
            l += 1
            r += 1
            if isequal(j, k):
                ans.append(l)  
        return ans
