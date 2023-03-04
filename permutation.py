class Solution:
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)

test_case = Solution()
res = test_case.permute([1, 1, 8, 9])
print('the results are:', res)
