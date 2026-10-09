class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # not in-place algo
        k = k % len(nums)
        if not nums:
            return

        latter_portion = nums[len(nums) - k : ]
        front_portion = nums[ : len(nums) - k]
        nums.clear()
        nums_new = latter_portion + front_portion
        for num in nums_new:
            nums.append(num)
        return