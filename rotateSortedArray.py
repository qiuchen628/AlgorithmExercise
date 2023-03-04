class Solution:

    def binary_search(self, nums, target):
        if not nums:
            return -1;
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = int(low + (high - low) / 2)
            print('mid: ', + mid)
            if target == nums[mid]:
                return mid
            elif nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

test_case = Solution()
res = test_case.binary_search([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1, 2, 3], 7)
print(res)