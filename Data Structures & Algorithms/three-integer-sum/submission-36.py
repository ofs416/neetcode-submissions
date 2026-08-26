class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for ix, num in enumerate(nums):
            sub_result = sortedTwoSum(nums[:ix]+nums[ix+1:], -num)
            if sub_result:
                for sr in sub_result:
                    sr.sort()
                    if sr not in result:
                        result.append(sr)
        return result


def sortedTwoSum(nums, target):

    l, r = 0, len(nums)-1
    result = []
    while  l < r:
        curr = nums[l] + nums[r]
        if curr < target:
            l += 1
        elif curr > target:
            r -= 1
        else:
            result.append([-target, nums[l], nums[r]])
            l += 1
            r -= 1

    return result
