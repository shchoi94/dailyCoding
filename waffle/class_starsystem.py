if __name__ == '__main__':
    from math import gcd


    class Star:
        how_many_star = 0
        list_star = []
        cycle_x, cycle_y, cycle_z = 0, 0, 0

        # 가속도를 계산하여 각 행성의 속도정보를 업데이트한다. return 안함.
        @classmethod
        def update_stars_vel(cls, axis):
            for i in range(0, Star.how_many_star):
                for j in range(0, Star.how_many_star):
                    # 속도 계산 시 행성 자기 자신 제외한 나머지와 위치 비교
                    if Star.list_star[i] != Star.list_star[j]:
                        if axis == "x":
                            if Star.list_star[i].__pos_x > Star.list_star[j].__pos_x:
                                Star.list_star[i].__vel_x += -1
                            elif Star.list_star[i].__pos_x < Star.list_star[j].__pos_x:
                                Star.list_star[i].__vel_x += 1
                        elif axis == "y":
                            if Star.list_star[i].__pos_y > Star.list_star[j].__pos_y:
                                Star.list_star[i].__vel_y += -1
                            elif Star.list_star[i].__pos_y < Star.list_star[j].__pos_y:
                                Star.list_star[i].__vel_y += 1
                        elif axis == "z":
                            if Star.list_star[i].__pos_z > Star.list_star[j].__pos_z:
                                Star.list_star[i].__vel_z += -1
                            elif Star.list_star[i].__pos_z < Star.list_star[j].__pos_z:
                                Star.list_star[i].__vel_z += 1

        # 업데이트 된 속도 정보로 해당하는 만큼 위치를 이동시키고 주기를 재기 위해 카운트한다. return 안함.
        @classmethod
        def update_stars_pos(cls, axis):
            for i in range(0, Star.how_many_star):
                if axis == "x":
                    Star.list_star[i].__pos_x += Star.list_star[i].__vel_x
                elif axis == "y":
                    Star.list_star[i].__pos_y += Star.list_star[i].__vel_y
                elif axis == "z":
                    Star.list_star[i].__pos_z += Star.list_star[i].__vel_z
            if axis == "x":
                Star.cycle_x += 1
            elif axis == "y":
                Star.cycle_y += 1
            elif axis == "z":
                Star.cycle_z += 1

        # 주기를 계산한다. return axis_cycle
        @classmethod
        def get_cycle(cls, axis):
            while True:
                Star.update_stars_vel(axis)
                Star.update_stars_pos(axis)
                for i in range(0, Star.how_many_star):
                    if not Star.list_star[i].is_comeback_(axis):
                        break
                    if i == Star.how_many_star - 1:
                        if axis == "x":
                            return Star.cycle_x
                        elif axis == "y":
                            return Star.cycle_y
                        elif axis == "z":
                            return Star.cycle_z

        # 인스턴스 생성 초기화 함수.
        def __init__(self, x_i, y_i, z_i, vx_i, vy_i, vz_i):
            self.__pos_x = x_i
            self.__pos_y = y_i
            self.__pos_z = z_i
            self.__vel_x = vx_i
            self.__vel_y = vy_i
            self.__vel_z = vz_i
            self.__ini_pos_x = x_i
            self.__ini_pos_y = y_i
            self.__ini_pos_z = z_i
            self.__ini_vel_x = vx_i
            self.__ini_vel_y = vy_i
            self.__ini_vel_z = vz_i
            Star.how_many_star += 1
            Star.list_star.append(self)

        # 행성 하나가 초기 위치와 속도로 돌아왔는지 체크 return boolean
        def is_comeback_(self, axis):
            if axis == "x":
                if self.__pos_x == self.__ini_pos_x and self.__vel_x == self.__ini_vel_x:
                    return True
            elif axis == "y":
                if self.__pos_y == self.__ini_pos_y and self.__vel_y == self.__ini_vel_y:
                    return True
            elif axis == "z":
                if self.__pos_z == self.__ini_pos_z and self.__vel_z == self.__ini_vel_z:
                    return True
            return False


    Star(-12, -11, 14, 0, 0, 0)
    Star(14, 6, 9, 0, 0, 0)
    Star(-6, 14, -14, 0, 0, 0)
    Star(-8, 3, -14, 0, 0, 0)
    xc = Star.get_cycle("x")
    yc = Star.get_cycle("y")
    zc = Star.get_cycle("z")

    print(xc)
    print(yc)
    print(zc)
    temp = (xc * yc // gcd(xc, yc))
    result = temp * zc // gcd(temp, zc)
    print(result)
