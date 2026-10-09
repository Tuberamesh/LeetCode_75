#Kadane’s Algorithm
#problem no: 53
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        Max = nums[0]
        sum = nums[0]

        for i in range(1, len(nums)):
            sum = max(nums[i], sum + nums[i])
            Max = max(sum, Max)

        return Max

#LeetCode 283 — Move Zeroes
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        k = []
        l = []

        for i in range(len(nums)):
            if nums[i] == 0:
                k.append(nums[i])
            else:
                l.append(nums[i])

        nums[:] = l + k