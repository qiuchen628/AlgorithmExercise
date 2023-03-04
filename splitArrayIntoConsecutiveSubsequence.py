import collections


class Solution:
    def isPossible(self, nums) :
        if len(nums) < 3: return False
        frequency = collections.Counter(nums)
        print(frequency)
        subsequence = collections.defaultdict(int)
        print(subsequence)
        for i in nums:
            if frequency[i] == 0:
                continue
            frequency[i] -= 1
            # option 1 - add to an existing subsequence
            if subsequence[i - 1] > 0:
                subsequence[i - 1] -= 1
                subsequence[i] += 1
            # option 2 - create a new subsequence
            elif frequency[i + 1] and frequency[i + 2]:
                frequency[i + 1] -= 1
                frequency[i + 2] -= 1
                subsequence[i + 2] += 1
            else:
                return False
        return True

num1 = [1,2,3,3,4,5,5]
obj1 = Solution()
test_case = obj1.isPossible(num1)
print(test_case)