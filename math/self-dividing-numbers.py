class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        x=[]  
        for i in range(left,right+1):
            n=str(i)
            ln = 0
            for j in n:
                 if j != '0' and i % int(j) == 0:
                     ln += 1
                 else:
                     break     
            if ln == len(n):
                  x.append(i)
        return x
        