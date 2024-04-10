class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        sorts = sorted(deck)
        q = deque()
        for i in range(len(deck)):
            q.append(i)
        op=[0]*len(deck)
        for i in range(len(sorts)):
            index = q.popleft()
            op[index]=sorts[i]
            if q:
                q.append(q.popleft())
        return op
                
        
            