class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
    
        #             right,   down,  left,   up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        bounds =     [COLS-1, ROWS-1,  0     , 0      ]
        change =     [-1    , -1    ,  1     , 1      ]


        d = 0
        result = []
        i, j = 0, 0

        while len(result)<ROWS*COLS:
            
            result.append(matrix[i][j])

            di, dj = directions[d]
            limiting_dim = j if di == 0 else i

            if limiting_dim == bounds[d]:
                bounds[(d + 3) % 4] += change[(d + 3) % 4]
                d = (d + 1) % 4

            i += directions[d][0]
            j += directions[d][1]

        return result
