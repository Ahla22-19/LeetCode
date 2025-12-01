class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:  
        if len(matrix)==1 and len(matrix[0])==1:
            if matrix[0][0]==target:
                return True
            else:
                return False
        for i in range(len(matrix)):
            a=matrix[i]
            l=0
            r=len(a)-1
            print(matrix[0])
            while l<r:
                mid=(l+r)//2
                if a[mid]<target:
                    l=mid+1
                else:
                    r=mid
            if a[r]==target:
                return True
        return False


        