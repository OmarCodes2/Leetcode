class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        occurence = {}
        largest = -1
        for i in nums:
            if i not in occurence:
                occurence[i] = 1
            else:
                occurence[i] += 1
        
        for key, value in occurence.items():
            if value == 1 and key > largest:
                largest = key
        return largest