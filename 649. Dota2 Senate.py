from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        rad = deque()
        dir = deque()

        for i, c in enumerate(senate):
            if c == 'R':
                rad.append(i)
            else:
                dir.append(i)
        
        while rad and dir:
            r = rad.popleft()
            d = dir.popleft()
            if r < d:
                rad.append(n+r)
            else:
                dir.append(n+d)
        return 'Radiant' if rad else 'Dire'
# 69-97; 7-84
