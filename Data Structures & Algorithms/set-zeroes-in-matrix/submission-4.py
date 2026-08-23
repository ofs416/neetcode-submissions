class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        row_set = [set(row) for row in matrix]
        col_set = [set(col) for col in zip(*matrix)]

        
        row_0 = list(map(lambda x: 0 in x, row_set))
        col_0 = list(map(lambda x: 0 in x, col_set))

        for i, row_bool in enumerate(row_0):
            if row_bool:
                matrix[i] = [0] * COLS
         
        for j, col_bool in enumerate(col_0):
            if col_bool:
                for i in range(ROWS):
                    matrix[i][j] = 0

    