class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        lst=[0]*n
        for i in range(n):
            if (i+1)%3 == 0 and (i+1)%5==0:
                lst[i] = "FizzBuzz"
            elif (i+1)%3==0:
                lst[i] = "Fizz"
            elif (i+1)%5==0:
                lst[i] = "Buzz"
            else:
                lst[i] = str(i+1)
        return lst      