class Solution(object):

    def combinationSum(self, candidates, target):
        res = []
        path = []
        self.dfs(candidates, target, path, res)
        return res

    def dfs(self, candidates, target, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(len(candidates)):
            if candidates[i] == candidates[i-1]:
                print("kk")
                continue
            self.dfs(candidates[i:], target-candidates[i], path + [candidates[i]], res)


test_case = Solution()
res = test_case.combinationSum([1, 1, 2, 3, 5, 6, 7], 8)

print(res)




