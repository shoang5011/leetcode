# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

class Solution:

    # bfs
    # def numIslands(self, grid): 
    #     # visited = set()
    #     m,n = len(grid),len(grid[0])
    #     numisland = 0

    #     def bfs(i,j): 
    #         q = []
    #         q.append((i,j))           
    #         while q: 
    #             i,j = q.pop(0)
    #             neighbors = [[i+1,j],[i-1,j],[i,j-1],[i,j+1]]
    #             for r,c in neighbors: 
    #                 if r in range(m) and c in range(n) and grid[r][c] =='1' : #and (r,c) not in visited
    #                     # visited.add((r,c))
    #                     grid[r][c] = '0'
    #                     q.append((r,c))

    #     q = []
    #     q.append((0,0))
    #     for i in range(m): 
    #         for j in range(n): 
    #             if grid[i][j] == '1' :
    #             # and (i,j) not in visited: 
    #                 numisland += 1
    #                 grid[i][j] = '0'
    #                 bfs(i,j)
                    
    #     return numisland

    
    # dfs
    def numIslands(self, grid):
        m,n = len(grid),len(grid[0])
        numisland = 0
        def dfs(i,j): 
            if i not in range(m) or j not in range(n) or grid[i][j] == '0'  : 
                return 

            grid[i][j] = '0'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        for i in range(m): 
            for j in range(n): 
                if grid[i][j] == '1' :
                # and (i,j) not in visited: 
                    numisland += 1
                    dfs(i,j)

        return numisland







inp =  [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
solution = Solution()
res = solution.numIslands(inp)
print(res)