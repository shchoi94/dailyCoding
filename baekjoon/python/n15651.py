def dfs(_num_list, _print_list, _m, current_depth):
    if _m == current_depth:
        print(" ".join(_print_list))
        return
    for i in range(len(_num_list)):
        # if not _num_list[i]:
        #     _num_list[i] = True
        _print_list.append(str(i + 1))
        dfs(_num_list, _print_list, _m, current_depth + 1)
        _print_list.pop()
        # _num_list[i] = False


if __name__ == '__main__':
    N, M = map(int, input().split())
    # M is depth
    num_list = [0] * N
    print_list = []
    dfs(num_list, print_list, M, 0)
