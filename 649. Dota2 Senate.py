class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)

        rad = [i for i in range (len(senate)) if senate[i] == 'R']
        dir = [i for i in range (len(senate)) if senate[i] == 'D']
        
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
# 16, 19
