class Solution:
    def minSwaps(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            if s[i]=="[":
                count+=1
            else:
                if count>0:
                    count-=1
        c=(count+1)//2    
        return c
        


        