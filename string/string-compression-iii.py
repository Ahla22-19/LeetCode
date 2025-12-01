class Solution:
    def compressedString(self, word: str) -> str:
        comp=""
        i=0
        while i<len(word) :
            a = word[i]
            count=0
            while i<len(word) and count<9 and a==word[i] :
                count+=1
                i+=1
            comp+=str(count)+a


           
        return comp


        