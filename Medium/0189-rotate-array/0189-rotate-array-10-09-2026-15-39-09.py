class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        # in-place algo: o(1) extra space
        k = k % len(nums) # normalise k if (>= n)

        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
                # 2-pointer in-place reversal algo

        size = len(nums)
        # reverse the entire array
        reverse(0, size - 1)
        # reverse the front portion
        reverse(0, k - 1)
        # reverse the latter portion
        reverse(k, size - 1)
        return