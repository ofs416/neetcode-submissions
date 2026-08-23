class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
    
        dr, dd, dl, du = (0, 1), (1, 0), (0, -1), (-1, 0)

        bounds = {dl:0, dr:COLS-1, du:0, dd:ROWS-1}
        drct_map = {dr:dd, dd:dl, dl:du, du:dr}
        bound_map = {dr:du, dd:dr, dl:dd, du:dl}

        drct = dr
        result = []
        i, j = 0, 0

        while len(result)<ROWS*COLS:
            
            result.append(matrix[i][j])

            if (drct==dr and j==bounds[drct] or
                drct==dd and i==bounds[drct] or
                drct==dl and j==bounds[drct] or
                drct==du and i==bounds[drct]
                ):
                bounds[bound_map[drct]] += max(drct_map[drct], key=abs) 
                drct = drct_map[drct]
            
            i += drct[0]
            j += drct[1]


        return result
