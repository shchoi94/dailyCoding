if __name__ == '__main__':
    from math import gcd


    def init_star_arr():
        star_arr = []
        begin_arr = []
        star_arr.append({
            "x": -12,
            "y": -11,
            "z": 14,
            "v.x": 0,
            "v.y": 0,
            "v.z": 0
        })
        star_arr.append({
            "x": 14,
            "y": 6,
            "z": 9,
            "v.x": 0,
            "v.y": 0,
            "v.z": 0
        })
        star_arr.append({
            "x": -6,
            "y": 14,
            "z": -14,
            "v.x": 0,
            "v.y": 0,
            "v.z": 0
        })
        star_arr.append({
            "x": -8,
            "y": 3,
            "z": -14,
            "v.x": 0,
            "v.y": 0,
            "v.z": 0
        })
        begin_arr.append({
            "x": -12,
            "y": -11,
            "z": 14,
            "v.x": 0,
            "v.y": 0,
            "v.z": 0
        })
        begin_arr.append({
            "x": 14,
            "y": 6,
            "z": 9,
            "v.x": 0,
            "v.y": 0,
            "v.z": 0
        })
        begin_arr.append({
            "x": -6,
            "y": 14,
            "z": -14,
            "v.x": 0,
            "v.y": 0,
            "v.z": 0
        })
        begin_arr.append({
            "x": -8,
            "y": 3,
            "z": -14,
            "v.x": 0,
            "v.y": 0,
            "v.z": 0
        })
        return star_arr, begin_arr


    def update_vel():
        global star_arr
        for i in range(0, 4):
            n_x = star_arr[i]["x"]
            n_y = star_arr[i]["y"]
            n_z = star_arr[i]["z"]
            for j in range(0, 4):
                if i != j:
                    if star_arr[j]["x"] > n_x:
                        star_arr[i]["v.x"] += 1
                    elif star_arr[j]["x"] < n_x:
                        star_arr[i]["v.x"] += -1
                    if star_arr[j]["y"] > n_y:
                        star_arr[i]["v.y"] += 1
                    elif star_arr[j]["y"] < n_y:
                        star_arr[i]["v.y"] += -1
                    if star_arr[j]["z"] > n_z:
                        star_arr[i]["v.z"] += 1
                    elif star_arr[j]["z"] < n_z:
                        star_arr[i]["v.z"] += -1


    def update_pos():
        global star_arr
        for i in range(0, 4):
            star_arr[i]["x"] += star_arr[i]["v.x"]
            star_arr[i]["y"] += star_arr[i]["v.y"]
            star_arr[i]["z"] += star_arr[i]["v.z"]


    def xis_comeback():
        global star_arr, begin_arr
        for i in range(0, 4):
            if star_arr[i]["x"] != begin_arr[i]["x"] or star_arr[i]["v.x"] != begin_arr[i]["v.x"]:
                return 0
            if i == 3:
                return 1


    def yis_comeback():
        global star_arr, begin_arr
        for i in range(0, 4):
            if star_arr[i]["y"] != begin_arr[i]["y"] or star_arr[i]["v.y"] != begin_arr[i]["v.y"]:
                return 0
            if i == 3:
                return 1


    def zis_comeback():
        global star_arr, begin_arr
        for i in range(0, 4):
            if star_arr[i]["z"] != begin_arr[i]["z"] or star_arr[i]["v.z"] != begin_arr[i]["v.z"]:
                return 0
            if i == 3:
                return 1


    def get_xcount():
        xc = 0
        while True:
            update_vel()
            update_pos()
            xc += 1
            if xis_comeback() == 1:
                break
        return xc


    def get_ycount():
        yc = 0
        while True:
            update_vel()
            update_pos()
            yc += 1
            if yis_comeback() == 1:
                break
        return yc


    def get_zcount():
        zc = 0
        while True:
            update_vel()
            update_pos()
            zc += 1
            if zis_comeback() == 1:
                break
        return zc


    star_arr, begin_arr = init_star_arr()
    xc = get_xcount()

    star_arr, begin_arr = init_star_arr()
    yc = get_ycount()

    star_arr, begin_arr = init_star_arr()
    zc = get_zcount()

    temp = (xc * yc // gcd(xc, yc))
    result = temp * zc // gcd(temp, zc)
    print(result)
