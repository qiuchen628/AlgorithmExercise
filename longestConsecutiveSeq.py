class Solution:
    def longestConsectutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                curren_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    curren_streak += 1

                longest_streak = max(curren_streak, longest_streak)

        return longest_streak


test_case = Solution()
res = test_case.longestConsectutive([1, 3, 455, 2, 8, 9, 10, 11, 12, 7])

print('res:', res)