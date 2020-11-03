import sys

# sys.setrecursionlimit(100000)


def solve(bo):
    solve.counter += 1
    find = find_empty(bo)
    if not find:
        return bo
    else:
        row, col = find
    for num in range(1, 10):
        if valid(bo, num, (row, col)):
            bo[row][col] = num

            if solve(bo):
                return bo, solve.counter

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # check row
    for i in range(9):
        if bo[pos[0]][i] == num:
            return False

    # check column
    for i in range(9):
        if bo[i][pos[1]] == num:
            return False

    # check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def find_empty(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return (i, j)
    return None


solve.counter = 0
