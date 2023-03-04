class Solution(object):

    def letterCombination(self,digits):
        phone = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        if len(digits) == 0:
            return res
        self.dfs(digits, phone, 0, '', res)
        return res

    def dfs(self, digits, index, phone, path, res):

        if index >= len(phone):
            res.append(path)
            return

        return res