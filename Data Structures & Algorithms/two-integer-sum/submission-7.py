class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for ix, num in enumerate(nums):
            complement = target-num
            if complement in seen.keys():
                return [seen[complement], ix]
            seen[num] = ix
            
