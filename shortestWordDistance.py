class Solution:
    def shortest_distance(self, words, word1, word2):
        size = len(words)
        index1, index2 = size, size
        res = size

        for i in range(size):
            if words[i] == word1:
                index1 = i
                res = min(res, abs(index1 - index2))
            elif words[i] == word2:
                index2 = i
                res = min(res, abs(index1 - index2))

        return res

test_case = Solution()
res = test_case.shortest_distance(['apple', 'orange', 'lemon', 'banana', 'tomato'], 'apple', 'tomato')
print(res)