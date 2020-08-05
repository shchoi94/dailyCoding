if __name__ == '__main__':

    class Room:
        def __init__(self, now_c, answer_c):
            self.now_c = now_c
            self.answer_c = answer_c

        # change color and return count
        def now_to_answer(self, count):
            if self.now_c != self.answer_c:
                self.now_c = self.answer_c
                return count + 1
            else:
                return count


    def print_input_table():
        global row, col, input_table
        for i in range(row):
            for j in range(col):
                print(input_table[i][j], end="")
            print("")


    def set_ans_color(_st_c, _i, _j):
        _ans_color = ""
        if (_i + _j) % 2 == 1 and _st_c == "W":
            _ans_color = "B"
        elif (_i + _j) % 2 == 0 and _st_c == "W":
            _ans_color = "W"
        elif (_i + _j) % 2 == 1 and _st_c == "B":
            _ans_color = "W"
        elif (_i + _j) % 2 == 0 and _st_c == "B":
            _ans_color = "B"
        return _ans_color


    def count_change_color(_st_i, _st_j):
        global input_table
        st_c = input_table[_st_i][_st_j]
        _count = 0
        answer_table = [[] for _ in range(8)]
        for i in range(8):
            for j in range(8):
                ans_color = set_ans_color(st_c, i, j)
                answer_table[i].append(Room(input_table[i + _st_i][j + _st_j], ans_color))
                _count = answer_table[i][j].now_to_answer(_count)
        print("\n시작 인덱스 :", _st_i, _st_j)
        for i in range(8):
            for j in range(8):
                print(answer_table[i][j].now_c, end="")
            print("")
        return _count


    # input
    row, col = map(int, input().split())
    input_table = [[] for _ in range(row)]
    for i in range(0, row):
        input_table[i] = list(input())
    # print_input_table()
    min_count = row * col
    for i in range(0, row - 7):
        for j in range(0, col - 7):
            count = count_change_color(i, j)
            if count < min_count:
                min_count = count
    print(min_count)
