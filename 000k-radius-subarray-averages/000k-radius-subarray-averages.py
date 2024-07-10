class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefix = [nums[0]]
        if k == 0:
            return nums

        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        
        avgs = [0] * len(nums)

        for i in range(len(nums)):
            if (i-k >= 0 and i+k <= len(nums)-1):
                avgs[i] = (prefix[i+k] - prefix[i-k] + nums[i-k])//(2*k+1)
            else:
                avgs[i] = -1
        return avgs
