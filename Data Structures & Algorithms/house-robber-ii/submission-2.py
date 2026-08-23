class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        memo1, memo2 = {}, {}

        def dfs(idx, arr, memo):

            if idx in memo:
                pass
            else:
                if idx+1 > len(arr)-1:
                    memo[idx] = arr[idx]
                elif idx+1 == len(arr)-1:
                    memo[idx] = max(arr[idx], arr[idx+1])
                else:
                    memo[idx] = max(arr[idx] + dfs(idx+2, arr, memo), dfs(idx+1, arr, memo))

            return memo[idx]

        return max(dfs(0, nums[1:], memo1) , dfs(0, nums[:-1], memo2))

            