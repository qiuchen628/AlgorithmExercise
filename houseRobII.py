class Solution:
    def rob(self, nums) :
        if len(nums) == 0 or nums is None:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_simple(nums[:-1]), self.rob_simple(nums[1:]))

    def rob_simple(self, nums):
        pre_max = nums[0]
        curr_max = nums[0]
        for num in nums:
            tmp = curr_max
            curr_max = max(pre_max + num, curr_max)
            pre_max = tmp