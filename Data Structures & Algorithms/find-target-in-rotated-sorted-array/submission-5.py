class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) < 2:
            return 0 if nums[0] == target else -1

        if target not in set(nums):
            return -1

        l, r = 0, len(nums)-1
        while l != r:
            c = (l + r + 1) // 2

            if nums[l] < nums[c]:
                if nums[l] <= target <= nums[c]:
                    r = c
                else:
                    l = c
            else:
                if nums[c] <= target <= nums[r]:
                    l = c
                else:
                    r = c

            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
 
        