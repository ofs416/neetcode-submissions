class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    
        dr, dd, dl, du = (0, 1), (1, 0), (0, -1), (-1, 0)

        bounds = {dl:0, dr:len(matrix[0])-1, du:0, dd:len(matrix)-1}
        drct_map = {dr:dd, dd:dl, dl:du, du:dr}
        bound_map = {dr:du, dd:dr, dl:dd, du:dl}

        drct = dr
        result = []
        i, j = 0, 0

        while len(result)<len(matrix[0])*len(matrix):

            
            result.append(matrix[i][j])

            print(matrix[i][j],  drct, (i, j), bounds.values())
            
            if drct==dr and j==bounds[drct]:
                bounds[bound_map[drct]] += 1 
                drct = drct_map[drct]
            
            elif drct==dd and i==bounds[drct]:
                bounds[bound_map[drct]] -= 1 
                drct = drct_map[drct]

            elif drct==dl and j==bounds[drct]:
                bounds[bound_map[drct]] -= 1 
                drct = drct_map[drct]

            elif drct==du and i==bounds[drct]:
                bounds[bound_map[drct]] += 1 
                drct = drct_map[drct]

            

            i += drct[0]
            j += drct[1]


        return result
