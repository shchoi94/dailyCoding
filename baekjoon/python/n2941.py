def find_croatian(str):
    if str.find('c=') != -1:
        return str.replace('c=', ' ', 1)
    elif str.find('c-') != -1:
        return str.replace('c-', ' ', 1)
    elif str.find('dz=') != -1:
        return str.replace('dz=', ' ', 1)
    elif str.find('d-') != -1:
        return str.replace('d-', ' ', 1)
    elif str.find('lj') != -1:
        return str.replace('lj', ' ', 1)
    elif str.find('nj') != -1:
        return str.replace('nj', ' ', 1)
    elif str.find('s=') != -1:
        return str.replace('s=', ' ', 1)
    elif str.find('z=') != -1:
        return str.replace('z=', ' ', 1)
    else:
        return "0" + str


str = input()
count = 0
while True:
    if str.find("0") != -1:
        str = str.replace(" ", "")
        count += len(str) - 1
        print(count)
        break
    else:
        str = find_croatian(str)
        if str.find("0") == -1:
            count += 1
