import random

rows = 5
cols = 5

grid = [[random.randint(1, 9) for j in range(cols)] for i in range(rows)]

grid[1][2] = -1
grid[2][2] = -1
grid[3][1] = -1

print("Walking Time Grid:")
for row in grid:
    print(row)

dp = [[9999 for j in range(cols)] for i in range(rows)]

dp[0][0] = grid[0][0]

for i in range(rows):
    for j in range(cols):

        if grid[i][j] == -1:
            continue

        if i == 0 and j == 0:
            continue

        if i > 0 and dp[i-1][j] != 9999:
            dp[i][j] = min(dp[i][j], dp[i-1][j] + grid[i][j])

        if j > 0 and dp[i][j-1] != 9999:
            dp[i][j] = min(dp[i][j], dp[i][j-1] + grid[i][j])

print("\nDP Table:")
for row in dp:
    print(row)

if dp[rows-1][cols-1] == 9999:
    print("\nDestination cannot be reached.")
else:
    print("\nMinimum Walking Time:", dp[rows-1][cols-1])
    print("Destination Index:", (rows-1, cols-1))
