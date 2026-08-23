from collections import Counter

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for i, row in enumerate(grid):
            for j, entry in enumerate(row):
                islands += BFS(grid, i, j)

        return islands



def BFS(grid, i, j):
    if grid[i][j] == "1":
        queue = deque([(i,j)])
        while queue:
            i, j = queue.popleft()

            grid[i][j] = "0"
            
            if i+1 < len(grid) and grid[i+1][j] == "1":
                queue.append((i+1, j))
            if i > 0 and grid[i-1][j] == "1":
                queue.append((i-1, j))

    
            if j+1 < len(grid[0]) and grid[i][j+1] == "1":
                queue.append((i, j+1))
            if j > 0 and grid[i][j-1] == "1":
                queue.append((i, j-1))

        return 1
    return 0