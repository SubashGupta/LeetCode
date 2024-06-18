class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        combined = list(zip(difficulty, profit))
        combined.sort(key=lambda x: x[0])
        difficulty, profit = zip(*combined)
        worker.sort()
        total=0
        j=0
        profits=0
        for i in worker:
            while j < len(difficulty) and difficulty[j]<=i:
                    profits = max(profits, profit[j])
                    j+=1
            total+=profits
        return total