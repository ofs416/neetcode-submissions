class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for ix, num in enumerate(nums):
            for jx, complement in enumerate(nums):
                if ix == jx:
                    continue
                if num + complement == target:
                    return [ix, jx]

                    