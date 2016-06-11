# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

# grid = [[0, 1, 0, 1, 0, 0, 0],
#         [0, 1, 0, 1, 0, 0, 0],
#         [0, 1, 0, 1, 0, 0, 0],
#         [0, 1, 0, 1, 0, 0, 0],
#         [0, 0, 0, 1, 0, 0, 0]]

init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def search(grid, init, goal, cost):
    delta = [[-1, 0],  # go up
             [0, -1],  # go left
             [1, 0],  # go down
             [0, 1]]  # go right

    cost = 1

    pos = [0, init[0], init[1]]
    opened = [[0, init[0], init[1]]]
    closed = [[0, init[0], init[1]]]

    def isValid(pos, grid, opened, closed):
        if pos[1] > len(grid) - 1:
            return False
        if pos[1] < 0:
            return False
        if pos[2] > len(grid[0]) - 1:
            return False
        if pos[2] < 0:
            return False
        if grid[pos[1]][pos[2]] == 1:
            return False
        for i in range(len(closed)):
            if closed[i][1] == pos[1] and closed[i][2] == pos[2]:
                return False
        for i in range(len(opened)):
            if opened[i][1] == pos[1] and opened[i][2] == pos[2]:
                return False
        return True

    def getSortKey(item):
        return item[0]

    while pos[1] != goal[0] or pos[2] != goal[1]:
        for i in range(len(delta)):
            newPos = [pos[0] + cost, pos[1] + delta[i][0], pos[2] + delta[i][1]]
            if isValid(newPos, grid, opened, closed):
                opened.append(newPos)
        closed.append(pos)
        opened.pop(0)
        opened.sort(key=getSortKey)
        if len(opened) == 0:
            print "fail"
            return "fail"
        pos = opened[0]

    print pos
    return pos


search(grid, init, goal, cost)