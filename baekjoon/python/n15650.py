def dfs(ck_list, _m, current_depth):
    if current_depth == _m:
        for i in range(m - 1):
            if print_list[i] > print_list[i + 1]:
                return
        print(" ".join(map(str, print_list)))
        return

    for i in range(len(ck_list)):
        if not check_list[i]:
            check_list[i] = True
            print_list.append(i + 1)
            dfs(ck_list, _m, current_depth + 1)
            check_list[i] = False
            print_list.pop()


if __name__ == '__main__':
    n, m = map(int, input().split())
    check_list = [False] * n
    print_list = []
    dfs(check_list, m, 0)
