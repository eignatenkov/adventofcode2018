from collections import namedtuple
import numpy as np

Rectangle = namedtuple('Rectangle', ['x_start', 'y_start', 'x_end', 'y_end'])


def parse_line(line):
    id, dims = line.split(' @ ')
    id = int(id.strip('#'))
    coords, dimensions = dims.strip().split(':')
    x_start, y_start = map(int, coords.split(','))
    width, height = map(int, dimensions.strip().split('x'))
    return id, Rectangle(x_start, y_start, x_start + width, y_start + height)


def count_intersections(filename):
    field = np.zeros((2000, 2000))
    with open(filename) as f:
        for line in f:
            _, cur_req = parse_line(line)
            field[cur_req.y_start:cur_req.y_end, cur_req.x_start:cur_req.x_end] += 1
    return (field > 1).sum()


def is_point_in_rectangle(x: int, y: int, rectangle: Rectangle) -> bool:
    return rectangle.x_start < x < rectangle.x_end and rectangle.y_start < y < rectangle.y_end


def is_intersection(rectangle_a: Rectangle, rectangle_b: Rectangle) -> bool:
    return (is_point_in_rectangle(rectangle_a.x_start, rectangle_a.y_start, rectangle_b)) or \
           (is_point_in_rectangle(rectangle_a.x_start, rectangle_a.y_end, rectangle_b)) or \
           (is_point_in_rectangle(rectangle_a.x_end, rectangle_a.y_start, rectangle_b)) or \
           (is_point_in_rectangle(rectangle_a.x_end, rectangle_a.y_end, rectangle_b)) or \
           (is_point_in_rectangle(rectangle_b.x_start, rectangle_b.y_start, rectangle_a)) or \
           (is_point_in_rectangle(rectangle_b.x_start, rectangle_b.y_end, rectangle_a)) or \
           (is_point_in_rectangle(rectangle_b.x_end, rectangle_b.y_start, rectangle_a)) or \
           (is_point_in_rectangle(rectangle_b.x_end, rectangle_b.y_end, rectangle_a)) or \
           (rectangle_a == rectangle_b) or \
           (rectangle_a.x_start > rectangle_b.x_start and rectangle_a.x_end < rectangle_b.x_end and
            rectangle_a.y_start < rectangle_b.y_start and rectangle_a.y_end > rectangle_b.y_end) or \
           (rectangle_b.x_start > rectangle_a.x_start and rectangle_b.x_end < rectangle_a.x_end and
            rectangle_b.y_start < rectangle_a.y_start and rectangle_b.y_end > rectangle_a.y_end)


def read_rectangles(filename):
    with open(filename) as f:
        rectangles = [parse_line(line) for line in f]
    return rectangles


def find_non_covered_rectangle(rectangles):
    overlapping_rectangles = set()
    for i, rectangle_a_info in enumerate(rectangles):
        for rectangle_b_info in rectangles[i + 1:]:
            a_id, rectangle_a = rectangle_a_info
            b_id, rectangle_b = rectangle_b_info
            if is_intersection(rectangle_a, rectangle_b):
                overlapping_rectangles.add(a_id)
                overlapping_rectangles.add(b_id)
    return {r_id for (r_id, r) in rectangles} - overlapping_rectangles


if __name__ == "__main__":
    print(count_intersections("data/day03_input.txt"))
    print(find_non_covered_rectangle(read_rectangles("data/day03_input.txt")))
