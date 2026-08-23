from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        counters = list(map(lambda a : Counter(a) , strs))


        while len(strs) > 0:

            current_str = strs.pop(0)
            current_counter = counters.pop(0)

            output.append([current_str])

            for idx, str in reversed(list(enumerate(strs))):
                if current_counter == counters[idx]:
                    output[-1].append(str)
                    strs.pop(idx)
                    counters.pop(idx)
        
        return output