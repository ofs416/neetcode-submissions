class Solution:
    def climbStairs(self, n: int, mem: Optional[dict] = None) -> int:

        if not mem:
            mem = {1: 1, 2: 2}

        if n in mem:
            return mem[n]
        else:
            mem[n-1] = self.climbStairs(n-1, mem) 

            mem[n] =  mem[n-1] + mem[n-2]
        
        return mem[n]