class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prev = {}
        for i, n in enumerate(numbers, start =1):
            diff = target-n
            if diff in prev:
                return [prev[diff], i]
            prev[n]=i
        return
