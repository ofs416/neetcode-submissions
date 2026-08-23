class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}

        def dfs(idx):
            if idx >= len(nums):
                return 0
            if idx not in memo:
                memo[idx] = max(nums[idx] + dfs(idx+2), dfs(idx+1))
            return memo[idx]

        return dfs(0)

            