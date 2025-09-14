class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        rad = []
        dir = []

        for i, c in enumerate(senate):
            if c == 'R':
                rad.append(i)
            else:
                dir.append(i)
        
        while rad and dir:
            r = rad.pop(0)
            d = dir.pop(0)
            if r < d:
                rad.append(n+r)
            else:
                dir.append(n+d)
        if rad:
            return 'Radiant'
        else:
            return 'Dire'
# 20, 7-34
