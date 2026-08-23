class Solution:
    def climbStairs(self, n: int) -> int:
        
        mem = {1:1, 2: 2}

        def dfs(i):
            if i in mem:
                return mem[i]
            else:
                mem[i] = dfs(i-1) + dfs(i-2)
                return mem[i]

        dfs(n)

        return mem[n]