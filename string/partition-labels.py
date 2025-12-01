class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        lastIndex = {}

        for index, char in enumerate(s):
            lastIndex[char] = index
        print(lastIndex)

        res = []
        size = end = 0

        for index, char in enumerate(s):
            size +=  1
            end = max(end, lastIndex[char])

            if index == end:
                res.append(size)
                size = 0

        return res