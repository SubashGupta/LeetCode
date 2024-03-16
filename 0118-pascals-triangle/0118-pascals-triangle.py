class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst=[]
        lst2=[]
        for i in range(1,numRows+1):
            if i==1:
                lst2.append([1])
            elif i==2:
                lst2.append([1,1])
            else:
                for j in range(i):
                    if j==0 or j==i-1:
                        lst.append(1)
                    else:
                        val = lst2[i-2][j-1]+lst2[i-2][j]
                        lst.append(val)
                lst2.append(lst)
                lst=[]
        return lst2