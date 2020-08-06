if __name__ == '__main__':

    n = int(input())
    a = []
    for _ in range(n):
        a.append(int(input()))

    # insert sort
    # for i in range(1, n):
    #     temp=a[i]
    #     for j in range(i - 1, -1, -1):
    #         if temp < a[j]:
    #             a[j+1] = a[j]
    #             a[j]=temp
    #         else:
    #             a[j+1] = temp
    #             break

    # bubble sort
    for i in range(n - 1, -1, -1):
        for j in range(0, i):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp

    for i in a:
        print(i)
