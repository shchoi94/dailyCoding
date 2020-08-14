class Room:
    def __init__(self, val, idx_row, idx_col):
        self.val = val
        self.idx_row = idx_row
        self.idx_col = idx_col


# table is 9x9 list,
# area num is 1 to 9
# 1 2 3
# 4 5 6
# 7 8 9
# 3x3 room 데이터에서 val 값 추출하여 리스트로 변환
def three_by_three_to_list(table, area):
    result = []
    range_col = 3 * (area % 3)
    range_row = 3 * ((area - 1) // 3 + 1)
    if range_col == 0:
        range_col = 9
    for i in range(range_row - 3, range_row):
        for j in range(range_col - 3, range_col):
            result.append(table[i][j].val)
    return result


# room 데이터로 된 하나의 열에서 val 값 추출하여 리스로 변환
def vertical_to_list(table, col):
    result = []
    for i in range(9):
        result.append(table[i][col].val)
    return result


# room데이터로 되어있는 리스트에서 val만 추출해서 재구성
def horizontal_to_list(table, row):
    result = []
    for i in range(9):
        result.append(table[row][i].val)
    return result


# target is list having int value
def check_empty_nbr(target, result):
    for i in range(1, 10):
        if i in target:
            result[i - 1] = False
        else:
            result[i - 1] = True


# idx에 맞는 area 넘버로 치환
def idx_to_area(row_idx, col_idx):
    return (row_idx // 3) * 3 + (col_idx // 3 + 1)


# 0인 갯수 세고, 0인 room을 리스트로 만든다.
def count_zero(table):
    zero_list = []
    count = 0
    for i in range(9):
        for j in range(9):
            if table[i][j].val == 0:
                zero_list.append(table[i][j])
                count += 1
    return count, zero_list


def update_status():
    for i in range(9):
        check_empty_nbr(horizontal_to_list(sudoku_tb, i), horiz_line_tb[i])
        check_empty_nbr(vertical_to_list(sudoku_tb, i), ver_line_tb[i])
        check_empty_nbr(three_by_three_to_list(sudoku_tb, i + 1), area_tb[i])


def solve_sudoku(depth, cur_depth):
    global sudoku_tb, horiz_line_tb, ver_line_tb
    if cur_depth == depth:
        for i in range(9):
            for j in range(9):
                if j == 0:
                    print(sudoku_tb[i][j].val, end="")
                else:
                    print(" %d" % sudoku_tb[i][j].val, end="")
            print("")
        return -1

    update_status()
    flag = 1
    for room in zero_list:
        if room.val == 0:
            for k in range(0, 9):
                if horiz_line_tb[room.idx_row][k] and ver_line_tb[room.idx_col][k] and \
                        area_tb[idx_to_area(room.idx_row, room.idx_col) - 1][k]:
                    room.val = k + 1
                    flag = solve_sudoku(depth, cur_depth + 1)
                    if flag == -1:
                        return -1
                    if flag != -1:
                        room.val = 0
                        update_status()
            if room.val == 0:
                return 1


if __name__ == '__main__':

    sudoku_tb = [0 for _ in range(9)]
    horiz_line_tb = [[True for _ in range(9)] for _ in range(9)]
    ver_line_tb = [[True for _ in range(9)] for _ in range(9)]
    area_tb = [[True for _ in range(9)] for _ in range(9)]
    for _ in range(9):
        sudoku_tb[_] = list(map(int, input().split()))
    for i in range(9):
        for j in range(9):
            sudoku_tb[i][j] = Room(sudoku_tb[i][j], i, j)
    depth, zero_list = count_zero(sudoku_tb)

    solve_sudoku(depth, 0)
