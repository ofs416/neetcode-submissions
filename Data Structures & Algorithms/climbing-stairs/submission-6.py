class Solution:
    def climbStairs(self, n: int) -> int:
        
        mem = {1:1, 2: 2}

        for i in range(1, n+1):
            if i in mem:
                continue
            else:
                mem[i] = mem[i-1] + mem[i-2]
    
        return mem[n]