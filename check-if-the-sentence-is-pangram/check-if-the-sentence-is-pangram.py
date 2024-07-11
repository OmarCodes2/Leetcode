class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        setA = set(sentence)
        if len(setA) == 26:
            return True
        else:
            return False
        