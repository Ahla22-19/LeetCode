class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = Counter(digits)
        ans = []

        for even_num in range(100, 1000, 2):
            temp_count = count.copy()  
            flag = True

            for digit in str(even_num):
                if temp_count[int(digit)] > 0:
                    temp_count[int(digit)] -= 1
                else:
                    flag = False
                    break

            if flag:
                ans.append(even_num)
        
        return sorted(ans)  

         
