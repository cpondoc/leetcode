class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = [int] * len(nums)
        total = 0
        for i in range(len(sums)):
            total = total + nums[i]
            sums[i] = total
        return sums