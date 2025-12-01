class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        ans = []
        for string in words:
            s = set(string.lower())
            if s <= row1 or s <= row2 or s <= row3:
                ans.append(string)

        return ans
            


            
        