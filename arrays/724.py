class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            total += nums[i]
        if (total - nums[0] == 0):
            return 0
        running_total = 0
        for i in range(len(nums) - 1):
            running_total += nums[i]
            remaining = total - nums[i + 1] - running_total
            print(running_total)
            print(remaining)
            if (running_total == remaining):
                return i + 1
        return -1