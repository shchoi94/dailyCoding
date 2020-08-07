if __name__ == '__main__':
    from math import gcd


    class Star:
        len_stars = 0
        arr_stars = []
        cycle_x, cycle_y, cycle_z = 0, 0, 0

        @classmethod
        def update_stars_vel(cls, axis):
            for i in range(0, Star.len_stars):
                for j in range(0, Star.len_stars):
                    if Star.arr_stars[i] != Star.arr_stars[j]:
                        if axis == "x":
                            if Star.arr_stars[i].__pos_x > Star.arr_stars[j].__pos_x:
                                Star.arr_stars[i].__vel_x += -1
                            elif Star.arr_stars[i].__pos_x < Star.arr_stars[j].__pos_x:
                                Star.arr_stars[i].__vel_x += 1
                        elif axis == "y":
                            if Star.arr_stars[i].__pos_y > Star.arr_stars[j].__pos_y:
                                Star.arr_stars[i].__vel_y += -1
                            elif Star.arr_stars[i].__pos_y < Star.arr_stars[j].__pos_y:
                                Star.arr_stars[i].__vel_y += 1
                        elif axis == "z":
                            if Star.arr_stars[i].__pos_z > Star.arr_stars[j].__pos_z:
                                Star.arr_stars[i].__vel_z += -1
                            elif Star.arr_stars[i].__pos_z < Star.arr_stars[j].__pos_z:
                                Star.arr_stars[i].__vel_z += 1

        @classmethod
        def update_stars_pos(cls, axis):
            for i in range(0, Star.len_stars):
                if axis == "x":
                    Star.arr_stars[i].__pos_x += Star.arr_stars[i].__vel_x
                elif axis == "y":
                    Star.arr_stars[i].__pos_y += Star.arr_stars[i].__vel_y
                elif axis == "z":
                    Star.arr_stars[i].__pos_z += Star.arr_stars[i].__vel_z
            if axis == "x":
                Star.cycle_x += 1
            elif axis == "y":
                Star.cycle_y += 1
            elif axis == "z":
                Star.cycle_z += 1

        @classmethod
        def get_cycle(cls, axis):
            while True:
                Star.update_stars_vel(axis)
                Star.update_stars_pos(axis)
                for i in range(0, Star.len_stars):
                    if not Star.arr_stars[i].is_comeback_(axis):
                        break
                    if i == Star.len_stars - 1:
                        if axis == "x":
                            return Star.cycle_x
                        elif axis == "y":
                            return Star.cycle_y
                        elif axis == "z":
                            return Star.cycle_z

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
            Star.len_stars += 1
            Star.arr_stars.append(self)

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
