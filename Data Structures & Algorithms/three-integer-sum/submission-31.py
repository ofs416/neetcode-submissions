class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def twoSum(idx: int, nums: List[int]) -> List[Tuple[int]]:
            result = []
            seen = set()
            target = nums[idx]
            left, right = idx+1, len(nums)-1
            while left < right:
                s = nums[left] + nums[right] + target
                if s == 0:
                    result.append([target, nums[left], nums[right]])
                    left +=1
                    right -=1

                    try:
                        while nums[left] == nums[left-1]:
                            left +=1
                        while nums[right] == nums[right+1]:
                            right -=1
                    except:
                        pass

                if s < 0:
                    left +=1
                if s > 0:
                    right -= 1


               
                
                
            return result

        ordered = sorted(nums)
        #res = set()
        res = []
        for i, _ in enumerate(ordered):

            if i > 0 and ordered[i] == ordered[i-1]:
                continue

            #tmp_set = set(twoSum(i, ordered))
            #res = res.union(tmp_set)

            tmp = twoSum(i, ordered)
            if tmp:
                res.extend(tmp)

        
        return res #list(map(list, res))
