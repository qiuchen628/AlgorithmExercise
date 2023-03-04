class Solution:
    def maxProduct(self, nums):
        if len(nums) == 0:
            return 0

        max_curr = nums[0]
        min_curr = nums[0]

        result = max_curr

        for i in range(1, len(nums)):
            curr_num = nums[i]
            max_curr = max(curr_num, curr_num * max_curr, curr_num * min_curr)
            min_curr = min(curr_num, curr_num * max_curr, curr_num * min_curr)

            max_so_far = max_curr

            result = max(max_so_far, result)

        return result


