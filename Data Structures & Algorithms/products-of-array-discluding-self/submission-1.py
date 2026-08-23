from collections import Counter

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)

        length = len(nums)
        output = [1] * length

        for i, num in enumerate(nums):
            counts[num] -= 1
            for key, value in counts.items():
                if value > 0:
                    output[i] *=  key ** value


            counts[num] += 1
  

        return output