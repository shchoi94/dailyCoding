class Room:
    def __init__(self, val, idx_row, idx_col):
        self.val = val
        self.idx_row = idx_row
        self.idx_col = idx_col
        self.cnt_possible = 0


# table is 9x9 list,
# area num is 1 to 9
# 1 2 3
# 4 5 6
# 7 8 9
# 3x3 room 데이터에서 val 값 추출하여 리스트로 변환
def convert_area_to_array(sudoku_table, num_area):
    result = []
    area_col = 3 * (num_area % 3)
    area_row = 3 * ((num_area - 1) // 3 + 1)
    if area_col == 0:
        area_col = 9
    for i in range(area_row - 3, area_row):
        for j in range(area_col - 3, area_col):
            result.append(sudoku_table[i][j].val)
    return result


# room 데이터로 된 하나의 열에서 val 값 추출하여 리스로 변환
def convert_col_to_array(sudoku_table, col):
    result = []
    for i in range(9):
        result.append(sudoku_table[i][col].val)
    return result


# room데이터로 되어있는 리스트에서 val만 추출해서 재구성
def convert_row_to_array(sudoku_table, row):
    result = []
    for i in range(9):
        result.append(sudoku_table[row][i].val)
    return result


# target is list having int value
def check_possible_number(target, result):
    for i in range(1, 10):
        if i in target:
            result[i - 1] = False
        else:
            result[i - 1] = True


# idx에 맞는 area 넘버로 치환
def idx_to_area_number(row_idx, col_idx):
    return (row_idx // 3) * 3 + (col_idx // 3 + 1)


# 0인 갯수 세고, 0인 room을 리스트로 만든다.
def count_zero(sudoku_table):
    zero_list = []
    count = 0
    for i in range(9):
        for j in range(9):
            if sudoku_table[i][j].val == 0:
                zero_list.append(sudoku_table[i][j])
                count += 1
    return count, zero_list


def sort_zero_list():
    global zero_list
    for room in zero_list:
        for k in range(0, 9):
            if horiz_line_tb[room.idx_row][k] and ver_line_tb[room.idx_col][k] and \
                    area_tb[idx_to_area_number(room.idx_row, room.idx_col) - 1][k]:
                room.cnt_possible += 1
    # for room in zero_list:
    #     print(room.cnt_possible,end=" ")
    # print("")
    zero_list=sorted(zero_list, key=lambda a: a.cnt_possible)
    # for room in zero_list:
    #     print(room.cnt_possible,end=" ")
    # print("")


def update_possible_number():
    for i in range(9):
        check_possible_number(convert_row_to_array(sudoku_tb, i), horiz_line_tb[i])
        check_possible_number(convert_col_to_array(sudoku_tb, i), ver_line_tb[i])
        check_possible_number(convert_area_to_array(sudoku_tb, i + 1), area_tb[i])


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

    update_possible_number()
    flag = 1
    for room in zero_list:
        if room.val == 0:
            for k in range(0, 9):
                if horiz_line_tb[room.idx_row][k] and ver_line_tb[room.idx_col][k] and \
                        area_tb[idx_to_area_number(room.idx_row, room.idx_col) - 1][k]:
                    room.val = k + 1
                    flag = solve_sudoku(depth, cur_depth + 1)
                    if flag == -1:
                        return -1
                    if flag != -1:
                        room.val = 0
                        update_possible_number()
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
    update_possible_number()
    sort_zero_list()
    solve_sudoku(depth, 0)
