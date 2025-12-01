class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:

        new_list = [int(digit) for number in nums for digit in str(number)]
        return new_list
      
