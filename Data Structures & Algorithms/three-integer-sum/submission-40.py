class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for ix, num in enumerate(nums):
            if num > 0:
                break
            if ix > 0 and nums[ix] == nums[ix - 1]:
                continue
            result.extend(sortedTwoSum(nums, ix + 1, -num))
        return result


def sortedTwoSum(nums, lo, target):
    l, r = lo, len(nums) - 1
    result = []
    while l < r:
        curr = nums[l] + nums[r]
        if curr < target:
            l += 1
        elif curr > target:
            r -= 1
        else:
            result.append([-target, nums[l], nums[r]])
            l += 1
            r -= 1
            while l < r and nums[l] == nums[l - 1]:
                l += 1
            while l < r and nums[r] == nums[r + 1]:
                r -= 1
    return result
