if __name__ == '__main__':

    n = int(input())

    num = 665
    count = 0
    while True:
        if count == n:
            break
        num += 1
        str_num = str(num)
        if '666' in str_num:
            count += 1

    print(num)
