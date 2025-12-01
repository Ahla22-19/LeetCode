class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        my_dict = defaultdict(lambda : -1)

        for num in nums2:
            while stack and stack[-1] < num:
                val = stack.pop()
                my_dict[val] = num

            stack.append(num)
        
        return [my_dict[num] for num in nums1] 
               


            

        