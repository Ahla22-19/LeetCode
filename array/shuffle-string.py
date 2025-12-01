class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        dict_s = {}
        for i in range (len(s)):
            dict_s[indices[i]] = s[i]

        dict_sort = dict(sorted(dict_s.items()))

        shuffle = ''
        for key, value in dict_sort.items():
            shuffle += value
            
        return shuffle
        
