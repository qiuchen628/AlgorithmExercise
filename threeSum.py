class Solution:
    def three_sum(self, nums):
        res_sum = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.two_sum(nums, i, res_sum)
        return res_sum

    def two_sum(self, nums, i, res):
        low, high = i + 1, len(nums) - 1
        while low < high:
            sum = nums[i] + nums[low] + nums[high]
            if sum < 0:
                low += 1
            elif sum > 0:
                high -= 1
            else:
                res.append([nums[i], nums[low], nums[high]])
                low += 1
                high -= 1
                while low < high and nums[low] == nums[low - 1]:
                    low += 1



test_case = Solution()
res = test_case.three_sum([-2,0,1,1,2])
print(res)