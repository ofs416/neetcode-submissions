from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        req = len(nums) / 2


        mode = Counter(nums).most_common()[0][0]

        return mode