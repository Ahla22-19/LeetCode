class Solution:
    def hIndex(self, citations: List[int]) -> int:

        n = len(citations)
        counter = [0 for i in range(n + 1)]

        for cite in citations:
            counter[min(cite, n)] += 1

        greater = 0
        for h in range(n, -1, -1):
            greater += counter[h]
            if greater >= h:
                return h
        
        return 0

