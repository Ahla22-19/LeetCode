class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        ans = []
        n  = len(arr)

        def flip(right):
            left = 0
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        for i in range(n - 1, -1, -1):
            for j in range(i, - 1, -1):
                max_ = i
                if arr[j] > max_:
                    max_ = j

                if max_ != i:
                    flip(max_)
                    flip(i)
                    ans.append(max_ + 1)
                    ans.append(i + 1)

        return ans




        

        
        