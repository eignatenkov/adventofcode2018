from collections import namedtuple
import numpy as np

Rectangle = namedtuple('Rectangle', ['x_start', 'y_start', 'width', 'height'])


def parse_line(line):
    coords, dimensions = line.split('@')[1].strip().split(':')
    x_start, y_start = map(int, coords.split(','))
    width, height = map(int, dimensions.strip().split('x'))
    return Rectangle(x_start, y_start, width, height)


def count_intersections(filename):
    field = np.zeros((2000, 2000))
    with open(filename) as f:
        for line in f:
            cur_req = parse_line(line)
            field[cur_req.y_start:cur_req.y_start + cur_req.height, cur_req.x_start:cur_req.x_start + cur_req.width] += 1
    return (field > 1).sum()


if __name__ == "__main__":
    print(count_intersections("data/day03_input.txt"))
