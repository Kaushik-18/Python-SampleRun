''' Given a non-empty 2D array grid of 0's and 1's, 
an island is a group of 1's (representing land) 
connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.
Find the maximum area of an island in the given 2D array.
 (If there is no island, the maximum area is 0.) '''

def maxAreaIsland(grid) :
    max_area = 0 
    seen = set()
    stack =[]
    delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for row, _ in enumerate(grid) :
        for column, column_val in enumerate(grid[0]) :
            area = 0
            if (row, column) not in seen and column_val == 1 :
                seen.add((row, column))
                stack.append((row,column))
                while stack :
                    (rs, cs) = stack.pop()
                    area += 1
                    for val in delta :
                        r_test ,c_test = rs + val[0] , cs + val[1]
                        if 0 < r_test < len(grid) and 0 < c_test < len(grid[0])\
                            and grid[r_test][c_test] == 1 and (r_test, c_test) not in seen :
                            seen.add(r_test, c_test)
                            stack.append(r_test, c_test)
                        
            max_area =  max(max_area, area)
    return max_area                   

'''find number of unique islands ,considering only translation , not rotation'''
def distinctIslands(grid):
    stack = []
    all_island_sets = set()
    seen =[]
    delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for row, _ in enumerate(grid):
        for column, column_val in enumerate(grid[0]):
            if (row, column) not in seen and column_val == 1 :
                island_set = []
                stack.append((row, column))
                seen.append((row, column))
                while stack :
                    (r, c) = stack.pop()
                    for vs in delta :
                        r_test, c_test = r + vs[0], c + vs[1]
                        if (0 < r_test < len(grid) and 0 < c < len(grid[0]) and
                                grid[r_test][c_test] == 1 and
                                (r_test, c_test) not in seen):
                            island_set.append((r_test - r ), (c_test - c))
                            seen.append((r_test, c_test))
                            stack.append((r_test, c_test))
                all_island_sets.add(tuple(island_set))            
    return len(all_island_sets)            

                        
             


        










                





            



