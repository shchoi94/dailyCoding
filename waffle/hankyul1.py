import re
from math import gcd
import time


def get_cycle(string: str):
    num_regex = re.compile('-?\d+')
    numbers = num_regex.findall(string)
    x = []
    y = []
    z = []
    planets = [x, y, z]
    for index, number in enumerate(numbers):
        planets[index % 3].append([int(index / 3), int(number), 0])
    x_cycle = axis_cycle(x)
    y_cycle = axis_cycle(y)
    z_cycle = axis_cycle(z)
    xy_cycle = lcm(x_cycle, y_cycle)
    xyz_cycle = lcm(xy_cycle, z_cycle)
    print(xyz_cycle)


def lcm(a, b):
    return a * b // gcd(a, b)


def axis_cycle(coordinates):
    # coordinate = [number, position, velocity]
    original = [coordinate.copy() for coordinate in coordinates]
    cycle = 0
    last_index = len(coordinates) - 1
    while True:
        coordinates = sorted(coordinates, key=lambda coo: coo[1], reverse=True)
        cycle_check = True
        before = coordinates[last_index][1] + 1
        coordinate_before = [0, 0, 0]
        duplicated = 1
        acceleration = 0
        for index, coordinate in enumerate(coordinates):
            if before != coordinate[1]:
                if duplicated > 1:
                    for k in range(index - duplicated, index):
                        coordinates[k][2] += acceleration
                    duplicated = 1
                else:
                    coordinate_before[2] += acceleration
                acceleration = 2 * index - last_index
            else:
                acceleration += 1
                duplicated += 1
            before = coordinate[1]
            coordinate_before = coordinate
        if duplicated > 1:
            for k in range(last_index + 1 - duplicated, last_index + 1):
                coordinates[k][2] += acceleration
        else:
            coordinate_before[2] += acceleration
        for coordinate in coordinates:
            coordinate[1] += coordinate[2]
            original_coordinate = original[coordinate[0]]
            cycle_check = cycle_check & (coordinate[1] == original_coordinate[1]) & (
                    coordinate[2] == original_coordinate[2])
        cycle += 1
        if cycle_check:
            return cycle


if __name__ == '__main__':
    start = time.time()
    get_cycle("<x=-12, y=-11, z= 14><x= 14, y=  6, z=  9><x= -6, y= 14, z=-14><x= -8, y=  3, z=-14>")
    print("time :", time.time() - start)


# import re
# from math import gcd
# import time
# import numpy as np
# def get_cycle(string: str):
#     num_regex = re.compile('-?\d+')
#     numbers = num_regex.findall(string)
#     x = []
#     y = []
#     z = []
#     planets = [x, y, z]
#     for index, number in enumerate(numbers):
#         planets[index % 3].append(int(number))
#     x_cycle = axis_cycle(x)
#     y_cycle = axis_cycle(y)
#     z_cycle = axis_cycle(z)
#     xy_cycle = lcm(x_cycle, y_cycle)
#     xyz_cycle = lcm(xy_cycle, z_cycle)
#     print(xyz_cycle)
# def lcm(a, b):
#     return a * b // gcd(a, b)
# def axis_cycle(coordinates):
#     coordinates_np = np.array(coordinates)
#     original = np.array(coordinates)
#     cycle = 0
#     velocity_orig = np.zeros(4, dtype=int)
#     velocity = np.zeros(4, dtype=int)
#     while True:
#         acc = np.array(
#             [len(coordinates_np[coordinates_np > coordinates_np[i]]) - len(
#                 coordinates_np[coordinates_np < coordinates_np[i]]) for i in
#              range(len(coordinates))])
#         velocity += acc
#         coordinates_np += velocity
#         cycle += 1
#         if np.array_equal(coordinates_np, original) and np.array_equal(velocity, velocity_orig):
#             return cycle
# if __name__ == '__main__':
#     start = time.time()
#     get_cycle("<x=  1, y=-11, z= -8><x=  8, y= -7, z=  0><x= 11, y= -7, z= 10><x= -6, y= -2, z=  8>")
#     print("time :", time.time() - start)