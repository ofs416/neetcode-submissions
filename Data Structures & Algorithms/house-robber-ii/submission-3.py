class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def dfs(idx, arr, memo):

            if idx >= len(arr):
                return 0
            if idx not in memo:
                memo[idx] = max(arr[idx] + dfs(idx+2, arr, memo), dfs(idx+1, arr, memo))

            return memo[idx]

        return max(dfs(0, nums[1:], {}) , dfs(0, nums[:-1], {}))

            