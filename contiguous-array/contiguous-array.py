class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        difference = {}
        zeros, ones = 0,0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            else:
                ones += 1
            if ones - zeros not in difference:
                difference[ones - zeros] = i

            if  ones == zeros:
                res = i + 1
            else:
                res = max(res, i - difference[ones-zeros])
        return res
        