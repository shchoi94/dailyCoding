if __name__ == '__main__':
    from math import gcd
    from copy import deepcopy

    def init_star_arr():
        star_arr = []
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
        begin_arr = deepcopy(star_arr)
        return star_arr, begin_arr


    def update_vel(xyz, v_xyz):
        global star_arr
        for i in range(0, 4):
            n = star_arr[i][xyz]
            for j in range(0, 4):
                if i != j:
                    if star_arr[j][xyz] > n:
                        star_arr[i][v_xyz] += 1
                    elif star_arr[j][xyz] < n:
                        star_arr[i][v_xyz] += -1


    def update_pos(xyz, v_xyz):
        global star_arr
        for i in range(0, 4):
            star_arr[i][xyz] += star_arr[i][v_xyz]


    def is_comeback(xyz, v_xyz):
        global star_arr, begin_arr
        for i in range(0, 4):
            if star_arr[i][xyz] != begin_arr[i][xyz] or star_arr[i][v_xyz] != begin_arr[i][v_xyz]:
                return 0
            if i == 3:
                return 1


    def get_count(xyz, v_xyz):
        c = 0
        while True:
            update_vel(xyz, v_xyz)
            update_pos(xyz, v_xyz)
            c += 1
            if is_comeback(xyz, v_xyz) == 1:
                break
        return c


    star_arr, begin_arr = init_star_arr()
    xc = get_count("x", "v.x")
    print(xc)
    star_arr, begin_arr = init_star_arr()
    yc = get_count("y", "v.y")
    print(yc)
    star_arr, begin_arr = init_star_arr()
    zc = get_count("z", "v.z")
    print(zc)
    temp = (xc * yc // gcd(xc, yc))
    result = temp * zc // gcd(temp, zc)
    print(result)
