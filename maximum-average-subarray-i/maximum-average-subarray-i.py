class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return nums[0]

        sum = 0
        for i in range(k):
            sum += nums[i]
        
        maxAvg = sum/k

        for i in range(k, len(nums)):
            sum += nums[i] - nums[i-k]
            maxAvg = max(maxAvg, sum/k)
        
        return maxAvg