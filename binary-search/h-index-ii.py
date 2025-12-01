class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l=0
        r=citations[-1]
        n=len(citations)
       
        def helper(x):
            index = n-bisect_left(citations, x)
            if x<=index:
                return index


        while l <= r:
            m = (r+l) // 2
            
            if helper(m):
                l = m + 1
            else:
                r = m - 1

        return l-1