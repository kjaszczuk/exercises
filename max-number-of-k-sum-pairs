# https://leetcode.com/problems/max-number-of-k-sum-pairs/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = 0
        i = 0
        flag_popped = False
        while i < len(nums):
            if nums[i] >= k:
                nums.pop(i)
                continue
            i += 1
        i = 0
        while i < len(nums):
            for j in range (i+1, len(nums)):
                # print(i, nums, counter)
                if nums[i]+nums[j] == k:
                    nums.pop(i)
                    nums.pop(j-1)
                    counter += 1
                    flag_popped = True
                    # print(i, nums, counter)
                    break
            if not flag_popped:
                i += 1
            flag_popped = False
        return counter
