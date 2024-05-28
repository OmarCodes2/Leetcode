class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        current = 0
        zeros = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1

            while zeros>k:
                if nums[current] ==  0:
                    zeros -= 1
                current += 1
            
            ans = max(ans, i - current + 1)
        
        return ans
            



        