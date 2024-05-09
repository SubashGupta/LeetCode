class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        heaps = [-h for h in happiness]
        heapq.heapify(heaps)
        total = 0
        turn = 0
        for i in range(k):
            # Invert again to get the original value
            total += max(-heapq.heappop(heaps) - turn, 0)

            # Increment turns for the next iteration
            turn += 1
        return total
        