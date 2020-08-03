class WordClass:
    def __init__(self, eff):
        self.eff = eff


n = int(input())
word_arr = []
for i in range(0, n):
    word_arr.append(input())
alpha_arr = []
for i in range(97, 123):
    alpha_arr.append(WordClass(0))


def check_word():
    global i
    count = 0
    for j in range(0, n):
        for k in range(0, len(alpha_arr)):
            alpha_arr[k].eff = 0
        temp = word_arr[j][0]
        for i in range(1, len(word_arr[j])):
            if temp == word_arr[j][i]:
                temp = word_arr[j][i]
            elif temp != word_arr[j][i]:
                if alpha_arr[ord(temp) - 97].eff == 0:
                    alpha_arr[ord(temp) - 97].eff = 1
                elif alpha_arr[ord(temp) - 97].eff == 1:
                    alpha_arr[ord(temp) - 97].eff = -1
                temp = word_arr[j][i]
            if i == len(word_arr[j]) - 1:
                if alpha_arr[ord(word_arr[j][i]) - 97].eff == 0:
                    alpha_arr[ord(word_arr[j][i]) - 97].eff = 1
                elif alpha_arr[ord(word_arr[j][i]) - 97].eff == 1:
                    alpha_arr[ord(word_arr[j][i]) - 97].eff = -1
        is_group_word = 0
        for i in range(97, 123):
            if alpha_arr[i - 97].eff == -1:
                is_group_word = -1
        if is_group_word == 0:
            count += 1
    return count


count_group_word = check_word()
print(count_group_word)
