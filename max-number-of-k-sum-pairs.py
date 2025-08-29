class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = 0
        
        i = 0

        checked_values = []

        # try to solve it using count()
        while i < len(nums):
            if nums[i] in checked_values:
                i += 1
                continue
            elif nums[i] == k/2:
                counter += floor(nums.count(k/2)/2)
                checked_values.append(nums[i])
                i += 1
                continue
            counter += min(nums.count(nums[i]), nums.count(k-nums[i]))
            checked_values.append(nums[i])
            checked_values.append(k-nums[i])
            i += 1
        return counter
