class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        k = len(nums) -1 
        answer = [0] * len(nums)
        
        while i <= j:
            if abs(nums[i]) >= abs(nums[j]):
                answer[k] = (nums[i] ** 2)
                i += 1
            else:
                answer[k] = (nums[j] ** 2)
                j -= 1
            k-=1

        return answer
        