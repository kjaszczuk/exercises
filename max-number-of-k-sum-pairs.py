class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = 0
        nums.sort()
        # limit = len(nums)

        # get rid of values that are too high -- its
        # for i in range (len(nums)-1,-1,-1):
        #     if nums[i] < k:
        #         limit = i+1
        #         break
        # r = limit-1
        # nums = nums[:limit]
        r = len(nums)-1
        i = 0

        while i < r:
            if nums[i] == k - nums[r]:
                i += 1
                r -= 1
                counter += 1
            elif nums[i] < k-nums[r]:
                i += 1
            else:
                r -= 1

        return counter
