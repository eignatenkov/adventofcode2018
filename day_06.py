from math import fabs
from collections import Counter
from numpy import argmin, array


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(x={0}, y={1})".format(self.x, self.y)

    def distance(self, another_point):
        return fabs(self.x - another_point.x) + fabs(self.y - another_point.y)


def read_input(filename):
    point_list = []
    with open(filename) as f:
        for line in f:
            x, y = map(int, line.split(','))
            point_list.append(Point(x, y))
    return point_list


def find_closest(point, list_of_points):
    distances = [point.distance(p) for p in list_of_points]
    dist_max = min(distances)
    dist_counter = Counter(distances)
    if dist_counter[dist_max] > 1:
        return None
    else:
        return argmin(distances)


def total_distance(point, list_of_points):
    return sum(point.distance(p) for p in list_of_points)


def markup_plane(coords, additional_range=1):
    markup_counter = Counter()
    x_min = min(c.x for c in coords)
    x_max = max(c.x for c in coords)
    y_min = min(c.y for c in coords)
    y_max = max(c.y for c in coords)
    for x in range(x_min - additional_range, x_max + additional_range):
        for y in range(y_min - additional_range, y_max + additional_range):
            closest_coord = find_closest(Point(x, y), coords)
            if closest_coord is not None:
                markup_counter[closest_coord] += 1
    return markup_counter


def find_close_region(coords, max_dist, additional_range=1):
    n_good_points = 0
    x_min = min(c.x for c in coords)
    x_max = max(c.x for c in coords)
    y_min = min(c.y for c in coords)
    y_max = max(c.y for c in coords)
    for x in range(x_min - additional_range, x_max + additional_range):
        for y in range(y_min - additional_range, y_max + additional_range):
            if total_distance(Point(x, y), coords) < max_dist:
                n_good_points += 1
    return n_good_points


if __name__ == "__main__":
    coords = read_input('data/day06_input.txt')
    min_markup = markup_plane(coords, additional_range=2)
    next_markup = markup_plane(coords, additional_range=5)
    print(max(v for k, v in min_markup.items() if next_markup[k] == v))
    # seems that we are not getting new close points outside of the minimal square
    # covering all coords
    # print(find_close_region(coords, 10000, 5))
    print(find_close_region(coords, 10000, 2))

