class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        p1=0
        p2=0
        for i in arr2:
            while p2<len(arr1):
                if arr1[p2] == i:
                    arr1[p1],arr1[p2] = arr1[p2],arr1[p1]
                    p1+=1
                p2+=1
            p2=p1
        if p1<len(arr1):
            for i in range(p1, len(arr1)):
                mini = arr1[i]
                index = i
                for j in range(i+1, len(arr1)):
                    if arr1[j] < mini:
                        mini = arr1[j]
                        index = j
                arr1[i], arr1[index] = arr1[index], arr1[i]
        return arr1
            