class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #print(len(grid))
        #print(len(grid[1]))
        perimeter = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if row != 0 and column != 0:
                    if grid[row][column] == 1:
                        if grid[row][column - 1] == 1 and grid[row - 1][column] == 1:
                            pass
                        elif grid[row][column - 1] == 1 or grid[row - 1][column] == 1:
                            perimeter += 2
                        else:
                            perimeter += 4
                elif row == 0 and column == 0:
                    if grid[row][column] == 1:
                        perimeter += 4
                elif row == 0:
                    if grid[row][column] == 1:
                        if grid[row][column - 1] == 1:
                            perimeter += 2
                        else:
                            perimeter += 4
                elif column == 0:
                    if grid[row][column] == 1:
                        if grid[row - 1][column] == 1:
                            perimeter += 2
                        else:
                            perimeter += 4
        return perimeter
