class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        

        num_strs = len(strs)

        if num_strs == 1:
            return strs[0]
        
        result = strs[0]

        while len(result) != 0:
            count = 0
            for str in strs:
                if str[:len(result)] == result:
                    count += 1
                else:
                    result = result[:-1]
                    count = 0
                    break

            if count == num_strs:
                break
                
        return result