class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins = set()
        loss = set()
        loser = set()
        for i in range(0,len(matches)):
            if matches[i][0] not in loser:
                wins.add(matches[i][0])
            if matches[i][1] not in loser:
                loss.add(matches[i][1])
                loser.add(matches[i][1])
                wins.discard(matches[i][1])
            else:
                loss.discard(matches[i][1])
        wins = list(wins)
        wins.sort()
        loss = list(loss)
        loss.sort()
        return [wins, loss]
        