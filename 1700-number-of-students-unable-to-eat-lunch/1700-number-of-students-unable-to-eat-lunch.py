class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwichindex=0
        studentindex=0
        while len(students)!=0:
            if students[studentindex] == sandwiches[sandwichindex]:
                del students[studentindex]
                del sandwiches[sandwichindex]
            else:
                x = students[0]
                prev = students.copy()
                del students[studentindex]
                students.append(x)
                if prev == students:
                    return len(prev)
        return 0
        