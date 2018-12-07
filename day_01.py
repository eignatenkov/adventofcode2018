def sum_up(filename):
    total = 0

    with open(filename) as f:
        for line in f:
            total += int(line)
    return total


def first_twice(filename):
    seen_freqs = {0}
    cur_freq = 0
    while True:
        with open(filename) as f:
            for line in f:
                cur_freq += int(line)
                if cur_freq in seen_freqs:
                    return cur_freq
                else:
                    seen_freqs.add(cur_freq)


if __name__ == "__main__":
    print(sum_up('data/day01_input.txt'))
    print(first_twice('data/day01_input.txt'))
