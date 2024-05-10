class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        lst=[]
        ind=[]
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                lst.append(arr[i]/arr[j])
                ind.append([arr[i],arr[j]])
        lst.sort()
        x = lst[k-1]
        for s in ind:
            if s[0]/s[1] == x:
                return s
        