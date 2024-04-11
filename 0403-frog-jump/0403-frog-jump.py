class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # Create a dictionary to store the jump distances that can reach each stone
        dp = {stone: set() for stone in stones}
        dp[0] = {0}  # The frog starts at stone 0 with a jump distance of 0
        
        for stone in stones:
            for jump in dp[stone]:
                # Try all possible next jumps: k-1, k, k+1
                for next_jump in range(jump - 1, jump + 2):
                    if next_jump > 0 and stone + next_jump in dp:
                        dp[stone + next_jump].add(next_jump)
        
        # If the set of jump distances for the last stone is not empty, return True
        return bool(dp[stones[-1]])
                