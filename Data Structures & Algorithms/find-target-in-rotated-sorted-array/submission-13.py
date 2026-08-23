class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in set(nums):
            return -1

        l, r = 0, len(nums)-1
        while l <= r:
            c = (l + r) // 2

            if target == nums[c]:
                return c

            if nums[l] <= nums[c]:
                if nums[l] <= target <= nums[c]:
                    r = c
                else:
                    l = c+1
            else:
                if nums[c] <= target <= nums[r]:
                    l = c
                else:
                    r = c-1
