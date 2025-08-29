class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = 0
        nums.sort()
        limit = len(nums)

        # get rid of values that are too high
        for i in range (len(nums)-1,-1,-1):
            if nums[i] < k:
                limit = i+1
                break
        r = limit
        nums = nums[:limit]
        i = 0

        # try to solve it using count()
        while i < len(nums) and nums[i] < k/2:
            # print(i, nums[i], nums)
            i_count = nums.count(nums[i])
            counter += min(i_count, nums.count(k-nums[i]))
            i += i_count

        counter += floor(nums.count(k/2)/2)

        return counter
