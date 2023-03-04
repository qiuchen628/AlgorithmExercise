class WordDistance(object):
    def __init__(self, words):
        self.d = {}
        for index, val in enumerate(words):
            self.d[val] = self.d.get(val, []) + [index]

    def shortest(self, word1, word2):
        loc1, loc2 = self.locations[word1], self.locations[word2]
        l1, l2 = 0, 0
        mid_diff = float('inf')

        while l1 < len(loc1) and l2 < len(loc2):
            min_diff = min(min_diff, abs(loc1[l1] - loc[l2]))
            if loc1
