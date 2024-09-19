function countSubIslands(grid1, grid2) {
    const m = grid1.length;
    const n = grid1[0].length;

    // DFS function to explore islands
    function dfs(x, y) {
        // If out of bounds or water cell, return true
        if (x < 0 || x >= m || y < 0 || y >= n || grid2[x][y] === 0) {
            return true;
        }

        // If current cell in grid2 is land but not in grid1, it's not a sub-island
        if (grid1[x][y] === 0) {
            return false;
        }

        // Mark the current cell as visited by setting it to 0
        grid2[x][y] = 0;

        // Initialize result as true, and verify all directions
        let isSubIsland = true;
        isSubIsland = dfs(x + 1, y) && isSubIsland;
        isSubIsland = dfs(x - 1, y) && isSubIsland;
        isSubIsland = dfs(x, y + 1) && isSubIsland;
        isSubIsland = dfs(x, y - 1) && isSubIsland;

        return isSubIsland;
    }

    let count = 0;

    // Loop through all cells in grid2
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            // If we find an unvisited land cell in grid2
            if (grid2[i][j] === 1) {
                // Perform DFS and check if it's a sub-island
                if (dfs(i, j)) {
                    count++;
                }
            }
        }
    }

    return count;
}