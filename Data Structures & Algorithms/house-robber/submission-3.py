class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}

        def dfs(idx):

            if idx in memo:
                pass
            else:
                if idx+1 > len(nums)-1:
                    memo[idx] = nums[idx]
                elif idx+1 == len(nums)-1:
                    memo[idx] = max(nums[idx], dfs(idx+1))
                else:
                    memo[idx] = max(nums[idx] + dfs(idx+2), dfs(idx+1))

            return memo[idx]

        return dfs(0)

            