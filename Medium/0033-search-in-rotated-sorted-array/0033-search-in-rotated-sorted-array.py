class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1

        def modified_bs(left: int, right: int) -> int:
            if left > right:
                return -1

            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    return modified_bs(left, mid - 1)
                else:
                    return modified_bs(mid + 1, right)
            else:
                if nums[right] >= target > nums[mid]:
                    return modified_bs(mid + 1, right)
                else:
                    return modified_bs(left, mid - 1)

        index = modified_bs(0, len(nums) - 1)
        return index if index != -1 else -1