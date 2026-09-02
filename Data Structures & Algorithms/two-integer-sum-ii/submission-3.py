class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while True:
            curr = numbers[l] + numbers[r]

            if curr < target:
                l += 1
                while numbers[l] == numbers[l-1]:
                    l += 1
            elif curr > target:
                r -= 1
                while numbers[r] == numbers[r+1]:
                    r -= 1
            else:
                break

        return [l+1, r+1]
    

            