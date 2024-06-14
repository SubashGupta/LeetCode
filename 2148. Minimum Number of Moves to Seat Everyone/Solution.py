class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        x=0
        for i in range(len(students)):
            x+=(abs(students[i]-seats[i]))
        return x