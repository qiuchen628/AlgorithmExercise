class Solution:
    def maximumSubarraySum(self, nums, k) :
        hashmap = {}
        start = 0
        maximum = 0
        for i in range(len(nums)):
            if len(hashmap) == k:
                maximum = max(maximum, sum(hashmap))
                hashmap.pop(nums[start])
                start += 1
            if nums[i] not in hashmap:
                hashmap[nums[i]] = i
            else:
                for j in range(start, i-1):
                    hashmap.pop(nums[j])
                hashmap[nums[i]] = i
                start = i
        if len(hashmap) == k:
            maximum = max(maximum, sum(hashmap))
        return maximum

case1=[]

for i in range(10001):
    case1.append(i)


res = Solution().maximumSubarraySum(case1, 3)
print(res)
