class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        curr = numbers[l] + numbers[r]

        while curr != target:

            if curr < target:
                l += 1
                while numbers[l] == numbers[l-1]:
                    l += 1
            elif curr > target:
                r -= 1
                while numbers[r] == numbers[r+1]:
                    r -= 1
            
            curr = numbers[l] + numbers[r]

        return [l+1, r+1]

            