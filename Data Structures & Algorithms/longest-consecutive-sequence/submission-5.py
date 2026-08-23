class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = sorted(list(set(nums)))
        
        try:
            temp_num = nums_set.pop(0)
            max_length = 1
        except: 
            return 0

        temp_length = 1
        for num in nums_set:
            print(num, temp_num+1)
            if num == temp_num+1:
                temp_length +=1
            else:
                temp_length = 1

            if temp_length > max_length:
                    max_length = temp_length
            
            temp_num = num
        
        return max_length



