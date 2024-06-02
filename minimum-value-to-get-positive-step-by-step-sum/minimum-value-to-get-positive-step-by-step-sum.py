class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        lowest = nums[0]

        for i in range(1,len(nums)):
            sum = prefix[-1] + nums[i]
            prefix.append(sum)
            if sum < lowest:
                lowest = sum
        
        if lowest > 0:
            startValue = 1
        else:
            startValue = 1 - lowest
        
        return startValue
        