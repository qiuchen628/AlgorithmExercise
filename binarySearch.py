from typing import List


class Solution:
    def search_binary(self, target, nums):
        low, high = 0, len(nums)
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] >= target:
                high = mid
            else:
                low = mid + 1
        return low





test_case = Solution()
res = test_case.search_binary(13, [1,3,11,13,16])
print(res)

