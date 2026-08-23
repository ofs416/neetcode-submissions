class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        result = []




        def dfs(matrix, right, down, left, up):
            if not matrix:
                return
            if right:
                row_list = matrix
                result.extend(row_list[0])
                dfs(matrix[1:], False, True, False, False)
            elif down:
                col_list = [list(col) for col in zip(*matrix)]
                result.extend(col_list[-1])
                matrix = [list(col) for col in zip(*col_list[:-1])]
                dfs(matrix, False, False, True, False)
            if left:
                row_list = matrix
                result.extend(reversed(row_list[-1]))
                dfs(matrix[:-1], False, False, False, True)
            elif up:
                col_list = [list(col) for col in zip(*matrix)]
                result.extend(reversed(col_list[0]))
                matrix = [list(col) for col in zip(*col_list[1:])]
                dfs(matrix, True, False, False, False)

        dfs(matrix, True, False, False, False)
        return result