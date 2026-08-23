class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = sorted(list(set(nums)))
        
        try:
            temp_num = nums_set.pop(0)
            max_len = 1
            temp_len = 1
            for num in nums_set:
                if num == temp_num+1:
                    temp_len +=1
                else:
                    temp_len = 1

                max_len = max(max_len, temp_len)
                
                temp_num = num
            
            return max_len

        except: 
            return 0

        


