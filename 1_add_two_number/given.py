class Solution:
    def twoSum(self, nums:list[int], target:int) -> list[int]:
        numToIndex = {}
        for i, num in enumerate(nums):
            if (target-num) in numToIndex:
                return numToIndex[target - num], i
            numToIndex[num] = i


nums = [2, 7, 11, 15]
target = 9

solution = Solution()
print("Output:", solution.twoSum(nums, target))