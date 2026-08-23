class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        row_0 = [False] * ROWS
        col_0 = [False] * COLS

        for i in range(ROWS):
            if row_0[i]:
                continue

            for j in range(COLS):
                

                if matrix[i][j] == 0:
                    row_0[i] = True
                    col_0[j] = True

        for i, row_bool in enumerate(row_0):
            if row_bool:
                matrix[i] = [0] * COLS
         
        for j, col_bool in enumerate(col_0):
            if col_bool:
                for i in range(ROWS):
                    matrix[i][j] = 0

    
        