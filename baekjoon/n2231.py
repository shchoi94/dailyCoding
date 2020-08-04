if __name__ == '__main__':
    # 생성자 찾기.
    def find_gen(nbr):
        start = 0
        #  생성자는 nbr보다 63이상으로 작을 수 없다.
        if nbr > 63:
            start = nbr - 63
        for i in range(start, nbr):
            temp = i
            # 각 자리수를 구하기 위해 스트링으로 변환 
            str_i = str(i)
            for j in str_i:
                # 각 자리수 인트로 변환후 더하기
                temp += int(j)
            if temp == nbr:
                return i
            if i == nbr - 1 and temp != nbr:
                return 0


    n = int(input())
    print(find_gen(n))
