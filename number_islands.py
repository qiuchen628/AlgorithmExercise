# number of islands
def numIslands(grid) -> int:

    row, col = len(grid), len(grid[0])
    visit = set()
    count = 0

    def dfs(r, c):
        if(r < row and r >= 0 and c < col and c >= 0 and grid[r][c] == '1' and (r, c) not in visit):
            visit.add((r, c))
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)

    for i in range(row):
        for j in range(col):
            if grid[i][j] == '1' and (i, j) not in visit:
                dfs(i, j)
                count += 1

    return count


grid_islands = [['1', '1', '1'], ['1', '0', '0'], ['0', '1', '0']]

num_islands = numIslands(grid_islands)

print(num_islands)