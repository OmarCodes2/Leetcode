class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = {}
        for char in text:
            if char in countText:
                countText[char] += 1
            else:
                countText[char] = 1
        balloon = "balloon"
        countBalloon = {}
        for char in balloon:
            if char in countBalloon:
                countBalloon[char] += 1
            else:
                countBalloon[char] = 1
        res = float('inf')
        for char in countBalloon:
            if char in countText:
                res = min(res, countText[char] // countBalloon[char])
            else:
                return 0

        return res
