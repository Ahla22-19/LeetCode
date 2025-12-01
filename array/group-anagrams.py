class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sorted_dict = defaultdict(list)

        for string in strs:
            anagram = "".join(sorted(string))
            sorted_dict[anagram].append(string)

        return list(sorted_dict.values())
        

        
