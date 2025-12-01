class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:

        seats.sort()
        students.sort()

        count = 0

        for i in range(len(seats)):
            ans = abs(seats[i] - students[i])
            count += ans

        return count


        