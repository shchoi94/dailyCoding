def alpha_to_nbr(ch):
    if 65 <= ord(ch) <= 67:
        return 2
    elif 68 <= ord(ch) <= 70:
        return 3
    elif 71 <= ord(ch) <= 73:
        return 4
    elif 74 <= ord(ch) <= 76:
        return 5
    elif 77 <= ord(ch) <= 79:
        return 6
    elif 80 <= ord(ch) <= 83:
        return 7
    elif 84 <= ord(ch) <= 86:
        return 8
    elif 87 <= ord(ch) <= 90:
        return 9
    else:
        return -1


def nbr_to_sec(num):
    if 1 <= num <= 9:
        return num + 1
    else:
        return -1


word = input()
list_word = []
list_sec = []
total_time = 0
for i in range(0, len(word)):
    list_word.append(word[i])
    list_sec.append(nbr_to_sec(alpha_to_nbr(list_word[i])))
    total_time += list_sec[i]
print(total_time)
