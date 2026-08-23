class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def twoSum(idx: int, nums: List[int]) -> List[List[int]]:
            result = []
            target = nums[idx]
            left, right = idx+1, len(nums)-1
            while left < right:
                s = nums[left] + nums[right] + target

                if s == 0:
                    result.append([target, nums[left], nums[right]])
                    right -= 1
                if s < 0:
                    left +=1
                if s > 0:
                    right -= 1
            return result

        ordered = sorted(nums)
        res = []
        for i, _ in enumerate(ordered):
            if i>0 and ordered[i] == ordered[i-1]:
                continue
            tmp_res = twoSum(i, ordered)
            
            for triplet in tmp_res:
                if triplet not in res:
                    res.append(triplet)
        
        return res
