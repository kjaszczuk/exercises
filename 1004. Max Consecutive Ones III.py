class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        indexes_0 = []
        max_1 = 0
        n = len(nums)

        for i in range (n):
            if nums[i] == 0:
                indexes_0.append(i)
                if len(indexes_0) > k+1:
                    max_1 = max(max_1, indexes_0[-1]-indexes_0[-k-2]-1)

        # check edges
        if indexes_0 == [] or len(indexes_0) <= k:
            return n
        if k == 0:
            return max(max_1, n - indexes_0[-k-1]-1, indexes_0[k])
        else:
            return max(max_1, n - indexes_0[-k-1]-1, indexes_0[k-1]+1)
# 89, 15

# alternative (performance worse, but simpler and less memory)

"""class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, zero_count, max_length = 0, 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length
# 65, 76
"""
