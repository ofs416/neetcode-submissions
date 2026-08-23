class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = defaultdict(lambda:math.inf)
        memo[0] = 0
        for coin in coins:
            memo[coin] = 1

        def dfs(current):

            if current in memo:
                return memo[current]

            for coin in coins:
                subproblem = current - coin
                if subproblem < 0:
                    continue
              
                memo[current] = min(dfs(subproblem) + 1, memo[current])

            return memo[current] 

       

        dfs(amount)


        return -1 if memo[amount] == math.inf else memo[amount]

    
