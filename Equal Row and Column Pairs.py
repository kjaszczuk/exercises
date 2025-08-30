class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # 1 attempt
        # transposed = [[row[i] for row in grid] for i in range (len(grid))]
        # pairs_count = 0
        # for row1 in grid:
        #     for row2 in transposed:
        #         if row1 == row2:
        #             pairs_count += 1
        # return pairs_count
        # 24%, 35%

        # 2 attempt
        # rows = Counter(tuple(row) for row in grid)
        # transposed = [[row[i] for row in grid] for i in range (len(grid))]
        # cols = Counter(tuple(row) for row in transposed)
        # pairs_count = 0
        # for row in rows:
        #     if row in cols:
        #         pairs_count += rows[row]*cols[row]
        # return pairs_count
        # 65%, 19%; 69, 19

        # 3 attempt
        n = len(grid)
        rows = Counter(tuple(row) for row in grid)
        pairs_count = 0
        for i in range (n):
            col = tuple(grid[j][i] for j in range (n))
            pairs_count += rows[col]
        return pairs_count
        # 77%, 19%; 60, 35; 56, 12
