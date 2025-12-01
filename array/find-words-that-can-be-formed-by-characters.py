class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        count = Counter(chars)
        res = 0

        for char in words:
            cur_word = defaultdict(int)
            good = True

            for w in char:
                cur_word[w] += 1
                if w not in count or cur_word[w] > count[w]:
                    good = False
                    break

            if good:
                res += len(char)
                
        return res
