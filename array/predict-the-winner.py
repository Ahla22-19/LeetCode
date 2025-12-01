class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def player1win(left , right , scorep1 , scorep2 , turn):

            if left > right:
                return scorep1 >= scorep2

            if turn:
                pick_left = player1win(left + 1, right, 
                scorep1 + nums[left], scorep2, 
                not turn)

                pick_right = player1win(left, right - 1, 
                scorep1 + nums[right], scorep2, 
                not turn)

                return pick_left or pick_right

            else:
                pick_left = player1win(left + 1, right, 
                scorep1, scorep2 + nums[left], 
                not turn)

                pick_right = player1win(left, right - 1, 
                scorep1, scorep2 + nums[right], 
                not turn)
                
                return pick_left and pick_right
    
        return player1win(0, len(nums) - 1, 0, 0, True)