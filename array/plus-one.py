class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        resulting_integer = int(''.join(map(str, digits)))
        resulting_integer += 1
        digits_list = [int(digit) for digit in str(resulting_integer)]
        return digits_list


        


            
            

       
