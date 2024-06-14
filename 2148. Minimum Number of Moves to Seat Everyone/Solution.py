class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        maxi = max(max(seats),max(students))
        op = [0]*maxi
        for i in seats:
            op[i-1]+=1
        print(op)
        for i in students:
            op[i-1]-=1
        print(op)
        moves=0
        unmatched=0
        for i in op:
            moves+=abs(unmatched)
            unmatched+=i
            print(moves,unmatched)
        return moves
        