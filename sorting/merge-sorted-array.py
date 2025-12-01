class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l=r=0
        if nums1 and nums2:
            while l<m :
                if nums1[l]<=nums2[r]:
                    l+=1
                else:
                    nums1[l],nums2[r]=nums2[r],nums1[l]
                    nums2.sort()
                    l+=1
            for i in range(l,len(nums1)):
                nums1[i],nums2[r]=nums2[r],nums1[i]
                r+=1