if __name__ == '__main__':

    n = int(input())
    person = []
    for i in range(0, n):
        x, y = map(int, input().split())
        # dictionary type list
        person.append({"weight": x,
                       "height": y,
                       "rank": 1})
    for i in range(0, n):
        now_weight = person[i]["weight"]
        now_height = person[i]["height"]
        # 본인 제외 자신보다 몸무게,키 모두 큰 사람이 있으면 순위는 한 단계씩 내려간다.
        for j in range(0, n):
            if j != i:
                if now_weight < person[j]["weight"] and now_height < person[j]["height"]:
                    person[i]["rank"] += 1
    for i in range(0, n):
        print(person[i]["rank"], end=" ")
