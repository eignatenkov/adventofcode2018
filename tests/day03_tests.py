from day_03 import Rectangle, is_intersection


def test_intersections():
    rec_a = Rectangle(1, 1, 4, 5)
    assert is_intersection(rec_a, Rectangle(2, 2, 3, 3))
    assert is_intersection(rec_a, rec_a)
    assert is_intersection(Rectangle(2, 2, 3, 3), rec_a)
    assert not is_intersection(rec_a, Rectangle(4, 5, 6, 7))
    assert is_intersection(rec_a, Rectangle(0, 0, 100, 100))
    assert is_intersection(Rectangle(0, 0, 100, 100), rec_a)
    assert is_intersection(Rectangle(x_start=454, y_start=116, x_end=468, y_end=145),
                           Rectangle(x_start=450, y_start=117, x_end=477, y_end=133))
