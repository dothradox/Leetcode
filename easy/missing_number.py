class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # result=len(nums)
        # for i in range(len(nums)):
        #     result += (i-nums[i])
        # return result

        sum = 0
        for i in nums:
            sum += i
        n = len(nums)
        return int((n * (n + 1) / 2) - sum)
