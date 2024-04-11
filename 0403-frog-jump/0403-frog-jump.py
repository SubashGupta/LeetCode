class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp={}
        for stone in stones:
              dp[stone] = set()
        dp[0] = {0}
        for stone in stones:
            for jump in dp[stone]:
                for next_jump in range(jump - 1, jump + 2):
                    if next_jump > 0 and stone + next_jump in dp:
                        dp[stone + next_jump].add(next_jump)
        return bool(dp[stones[-1]])