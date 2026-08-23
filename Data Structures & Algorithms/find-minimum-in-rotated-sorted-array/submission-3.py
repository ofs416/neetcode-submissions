class Solution:
    def findMin(self, nums: List[int]) -> int:
        # the smallest is always in the half with rotation partition

        def binary_search(inputs: List[int]) -> int:
            
        
            midpoint = (len(inputs)-1) // 2
            
            if inputs[0] > inputs[midpoint]:
                # This is the half with the partition.
                inputs = inputs[:midpoint+1]
            else:
                inputs = inputs[midpoint+1:]

            if inputs[0] <= inputs[-1]:
                return inputs[0]
            else:
                return binary_search(inputs)
            


        # First check if rotated
        if nums[0] <= nums[-1]:
            return nums[0] 

        return binary_search(nums)