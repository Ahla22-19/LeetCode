class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        for i in range(k):
            m = max(gifts)
            n = floor(sqrt(m))
            gifts.remove(m)
            gifts.append(n)
           

        s = sum(gifts)

        return s