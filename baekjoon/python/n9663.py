def n_queen(n, cur_level):
    global count
    if n == cur_level:
        count += 1
        # for i in range(n):
        #     for j in range(n):
        #         if level[i][j] != "*":
        #             print("[ ]", end="")
        #         else:
        #             print("[", end="")
        #             print(level[i][j], end="")
        #             print("]", end="")
        #         # break
        #     print("")
        #     if i == n - 1:
        #         print("===================")
        return
    for j in range(n):
        if not level[cur_level][j]:
            # 현재 놓으려는 위치가 기존 퀸들의 위치에 의해서 걸리지 않는다면
            if check_vertical(cur_level, j, "*") == 0 and check_crossline(cur_level, j, "*") == 0:
                level[cur_level][j] = "*"
                check_vertical(cur_level, j, "close")
                check_crossline(cur_level, j, "close")
                n_queen(n, cur_level + 1)
                level[cur_level][j] = True
                check_vertical(cur_level, j, "open")
                check_crossline(cur_level, j, "open")


def check_vertical(cur_i, cur_j, state):
    for i in range(n):
        if state == "open":
            level[i][cur_j] = False
        elif i != cur_i:
            if state == "close":
                level[i][cur_j] = True
            if state == "*":
                if level[i][cur_j] == "*":
                    return -1
    return 0


def check_crossline(cur_i, cur_j, state):
    for i in range(n):
        count_cross = 0
        for j in range(n):
            if count_cross == 2:
                break
            # 절대값 계산
            diff_i = (cur_i - i) if (cur_i - i < 0) else (i - cur_i)
            diff_j = (cur_j - j) if (cur_j - j < 0) else (j - cur_j)
            if diff_i == diff_j:
                count_cross += 1
                if state == "open":
                    level[i][j] = False
                elif diff_i != 0:
                    if state == "close":
                        level[i][j] = True
                    if state == "*":
                        if level[i][j] == "*":
                            return -1
    return 0


if __name__ == '__main__':
    n = int(input())
    level = [[False for col in range(n)] for row in range(n)]
    count = 0
    n_queen(n, 0)
    print(count)
