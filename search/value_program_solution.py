# ----------
# User Instructions:
#
# Create a function compute_value() which returns
# a grid of values. Value is defined as the minimum
# number of moves required to get from a cell to the
# goal.
#
# If it is impossible to reach the goal from a cell
# you should assign that cell a value of 99.

# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

goal = [len(grid) - 1, len(grid[0]) - 1]

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']

cost = 1  # the cost associated with moving from a cell to an adjacent one.


# ----------------------------------------
# insert code below
# ----------------------------------------

def compute_value(grid, goal, cost):
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    value[goal[0]][goal[1]] = 0

    boundary = [[goal[0], goal[1]]]
    while len(boundary) > 0:
        newBoundary = []
        for i in range(len(boundary)):
            row = boundary[i][0]
            col = boundary[i][1]
            if row - 1 >= 0:
                if grid[row - 1][col] != 1 and value[row - 1][col] == 99:
                    value[row - 1][col] = value[row][col] + cost
                    newBoundary.append([row - 1, col])
            if row + 1 < len(grid):
                if grid[row + 1][col] != 1 and value[row + 1][col] == 99:
                    value[row + 1][col] = value[row][col] + cost
                    newBoundary.append([row + 1, col])
            if col - 1 >= 0:
                if grid[row][col - 1] != 1 and value[row][col - 1] == 99:
                    value[row][col - 1] = value[row][col] + cost
                    newBoundary.append([row, col - 1])
            if col + 1 < len(grid[0]):
                if grid[row][col + 1] != 1 and value[row][col + 1] == 99:
                    value[row][col + 1] = value[row][col] + cost
                    newBoundary.append([row, col + 1])
        boundary = []
        for i in newBoundary:
            boundary.append(i)

    for i in range(len(value)):
        print value[i]

    return value  # make sure your function returns a grid of values as demonstrated in the previous video.


compute_value(grid, goal, cost)