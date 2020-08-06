def make_input_table(_row):
    _input_tb = [[] for _ in range(_row)]
    for i in range(0, _row):
        _input_tb[i] = list(input())
    return _input_tb


def make_answer_table(ch):
    _answer_tb = [["" for _ in range(8)] for _ in range(8)]
    _answer_tb[0][0] = ch
    for i in range(8):
        for j in range(8):
            if _answer_tb[0][0] == "W":
                if (i + j) % 2 == 1:
                    _answer_tb[i][j] = "B"
                elif (i + j) % 2 == 0:
                    _answer_tb[i][j] = "W"
            elif _answer_tb[0][0] == "B":
                if (i + j) % 2 == 1:
                    _answer_tb[i][j] = "W"
                elif (i + j) % 2 == 0:
                    _answer_tb[i][j] = "B"
    return _answer_tb


def count_repaint(_input_tb, _answer_tb, _i, _j):
    _count = 0
    for i in range(8):
        for j in range(8):
            if _input_tb[_i + i][_j + j] != _answer_tb[i][j]:
                _count += 1
    return _count


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
            answer_tb = make_answer_table(input_tb[i][j])
            count_list.append(count_repaint(input_tb, answer_tb, i, j))
    print(find_min(count_list))
