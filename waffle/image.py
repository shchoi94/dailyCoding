if __name__ == '__main__':

    def check_color():
        global a
        # 결과, 출력할 테이블
        result = [[0 for col in range(30)] for row in range(7)]
        for i in range(7):
            for j in range(30):
                for k in range(5):
                    # 투명이면 다음 layer의 [i][j] 확인, 투명이 아니면 결과에 넣고 break
                    if a[k][i][j] != "2":
                        result[i][j] = a[k][i][j]
                        break
        for row in range(7):
            for col in range(30):
                # 가시성을 위해 0을 공백으로
                if result[row][col] == "0":
                    print(" ", end="")
                else:
                    print(result[row][col], end="")
            print("")


    input_list = list(input())
    a = [[[0 for col in range(30)] for row in range(7)] for depth in range(5)]
    index = 0
    for k in range(5):
        for i in range(7):
            for j in range(30):
                a[k][i][j] = input_list[index]
                index += 1
    check_color()
