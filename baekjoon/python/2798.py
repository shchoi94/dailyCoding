if __name__ == '__main__':

    def find_answer(_card_list):
        answer = 0
        global n, m
        card1, card2, card3 = -1, -1, -1
        # select card1
        for i in range(n - 2):
            card1 = _card_list[i]
            # select card2
            for j in range(i + 1, n - 1):
                card2 = _card_list[j]
                # select card3
                for k in range(j + 1, n):
                    card3 = _card_list[k]
                    # m에 가까운 값을 answer에 저장
                    if answer < card1 + card2 + card3 <= m:
                        answer = card1 + card2 + card3
                    # m이랑 같으면 바로 반환
                    if answer == m:
                        return answer
                    # 모든 경우의 수 탐색 시 종료
                    if i == n - 3:
                        return answer


    n, m = map(int, input().split())
    card_list = list(map(int, input().split()))
    print(find_answer(card_list))
