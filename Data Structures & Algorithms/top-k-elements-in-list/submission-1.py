from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        output = []

        for i in range(k):
            mc = counts.most_common()[0][0]
            counts.pop(mc)
            
            output.append(mc)
        
        return output