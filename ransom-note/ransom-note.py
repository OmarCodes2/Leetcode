class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        for i in range(len(magazine)):
            if magazine[i] in dict:
                dict[magazine[i]] += 1
            else:
                dict[magazine[i]] = 1
        
        for i in ransomNote:
            if i in dict and dict[i] != 0:
                dict[i] -= 1
            else:
                return False
        
        return True
        