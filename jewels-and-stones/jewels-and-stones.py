class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict = {}
        total = 0

        for i in range(len(stones)):
            if stones[i] in dict:
                dict[stones[i]] += 1
            else:
                dict[stones[i]] = 1
        
        for i in range(len(jewels)):
            if jewels[i] in dict:
                total += dict[jewels[i]]
        
        return total