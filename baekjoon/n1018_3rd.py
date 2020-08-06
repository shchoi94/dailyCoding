def make_input_table(_row):
    _input_tb = [[] for _ in range(_row)]
    for i in range(0, _row):
        _input_tb[i] = list(input())
    return _input_tb


def make_answer_table():
    _answer_tb1 = [["" for _ in range(8)] for _ in range(8)]
    _answer_tb2 = [["" for _ in range(8)] for _ in range(8)]
    _answer_tb1[0][0] = "W"
    _answer_tb2[0][0] = "B"
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 1:
                _answer_tb1[i][j] = "B"
                _answer_tb2[i][j] = "W"
            elif (i + j) % 2 == 0:
                _answer_tb1[i][j] = "W"
                _answer_tb2[i][j] = "B"
    return _answer_tb1, _answer_tb2


def count_repaint(_input_tb, _answer_tb1, _answer_tb2, _i, _j):
    _count1, _count2 = 0, 0
    for i in range(8):
        for j in range(8):
            if _input_tb[_i + i][_j + j] != _answer_tb1[i][j]:
                _count1 += 1
            if _input_tb[_i + i][_j + j] != _answer_tb2[i][j]:
                _count2 += 1
    if _count1 < _count2:
        return _count1
    else:
        return _count2


def find_min(_count_list):
    _min_count = _count_list[0]
    for val_count in _count_list:
        if val_count < _min_count:
            _min_count = val_count
    return _min_count


def print_table(tb):
    global row, col
    if tb == input_tb:
        print("input_tb=====")
        for i in range(row):
            for j in range(col):
                print(input_tb[i][j], end="")
            print("")
    else:
        print("answer_tb=====")
        for i in range(8):
            for j in range(8):
                print(tb[i][j], end="")
            print("")


if __name__ == '__main__':

    row, col = map(int, input().split())
    input_tb = make_input_table(row)
    count_list = []
    for i in range(row - 7):
        for j in range(col - 7):
            answer_tb1, answer_tb2 = make_answer_table()
            count_list.append(count_repaint(input_tb, answer_tb1, answer_tb2, i, j))
    print(find_min(count_list))
