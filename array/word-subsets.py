class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:\

        ans = []
        max_freq = defaultdict(int)
        for word in (words2):
            count = Counter(word)
            
            for c in count:
                max_freq[c] = max(count[c],max_freq[c])
            
        for word in words1:
            count2 = Counter(word)

            flag = True
            for c in max_freq:
                if max_freq[c] > count2[c]:
                    flag = False
                    break
            if flag:
                ans.append(word)

        return ans






