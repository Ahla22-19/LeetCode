class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        word_count = {}

        for char in s:
            word_count[char] = word_count.get(char, 0) + 1

        for char in t:
            word_count[char] = word_count.get(char, 0) - 1
                
        return all(value == 0 for value in word_count.values())