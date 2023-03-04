class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 0, n - 1
        while low <= high:
            mid = (high - low) // 2
            is_bad = isBadVersion(mid)
            if is_bad == True:
                if isBadVersion(mid - 1) == False:
                    return mid
                high = mid - 1
            else:
                low =  mid + 1