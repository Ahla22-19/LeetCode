class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        new=sorted(list(set(arr)))
        rank={}
        for i in range(len(new)):
            rank[new[i]]=i+1
        for i in range(len(arr)):
            arr[i]=rank[arr[i]]
        return arr

    

        
                
        