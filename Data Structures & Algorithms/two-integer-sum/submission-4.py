class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        left = 0
        
        while True:
            right = left + 1
            for idx, num in enumerate(nums[right:]):
                if nums[left] + num == target:
                    return [left, right + idx]

            left +=1
