class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a=0
        for i in nums:
            if i==target:
                a+=1
        if not nums or a==0:
            return[-1,-1]
        else:
            b=[]
            b.append(bisect_left(nums,target))
            b.append(bisect_right(nums,target)-1)
            return b
        