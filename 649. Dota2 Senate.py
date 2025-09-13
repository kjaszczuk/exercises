class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = list(senate)
        last_senator = ''
        votes = 0
        i = 0
        while True:
            while i < len(queue):
                if votes == 0 or queue[i] == last_senator:
                    last_senator = queue[i]
                    votes += 1
                    i += 1
                elif votes > 0:
                    del queue[i]
                    votes -= 1
            i = 0
            for j in range (votes):
                if last_senator == 'R' and "D" in queue:
                    del queue[queue.index('D')]
                elif last_senator == 'D' and "R" in queue:
                    del queue[queue.index('R')]
            votes = 0     

            if "R" not in queue:
                return 'Dire'
            if "D" not in queue:
                return 'Radiant' 
# who wins:
    # 2vs3 L
    # 3 vs 5 P
    # 4 vs 7 P

# 8, 52
