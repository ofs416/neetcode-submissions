class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix) , len(matrix[0])
        output = [0]*n*m
        placed = 0

        i, j = 0, 0
        di = "r"

        c = {"r": 0, "d":0, "l":0, "u":0}
        
        while placed < n*m:
            output[placed] = matrix[i][j]
            placed += 1

            if di == "r" and j+1<n-c["d"]:
                j += 1
                continue
            elif di == "r":
                c[di] += 1
                di = "d"
                i += 1
                continue
            
            if di == "d" and i+1<m-c["l"]:
                i += 1
                continue
            elif di == "d":
                c[di] += 1
                di = "l"
                j -= 1
                continue

            if di == "l" and j>c["u"]:
                j -= 1
                continue
            elif di == "l":
                c[di] += 1
                di = "u"
                i -= 1
                continue

            if di == "u" and i>c["r"]:
                i -= 1
                continue
            elif di == "u":
                c[di] += 1
                di = "r"
                j += 1
                continue

        return output


            
