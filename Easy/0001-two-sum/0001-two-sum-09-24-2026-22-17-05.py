class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 0 or target is None:
            return

        complements = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in complements:
                return [complements[complement][1], i]
            complements[num] = [complement, i]

        return