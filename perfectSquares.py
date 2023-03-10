import math


class perfectSquares:
    def numSqaures(self, n):
        sqaures_nums = [i**2 for i in range(0, int(math.sqrt(n)) + 1)]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for squre in sqaures_nums:
                if i < squre:
                    break
                dp[i] = min(dp[i], dp[i-squre] + 1)

        return dp[-1]
