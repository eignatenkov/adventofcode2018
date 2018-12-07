from collections import Counter


def count_letters(word):
    result = Counter()
    for letter in word:
        result[letter] += 1
    return result


def calc_checksum(filename):
    twos = 0
    threes = 0
    with open(filename) as f:
        for line in f:
            letter_counts = count_letters(line)
            if 2 in letter_counts.values():
                twos += 1
            if 3 in letter_counts.values():
                threes += 1
    return twos * threes


def check_close_ids(id1, id2):
    found_diff = False
    similar = ''
    for a, b in zip(id1, id2):
        if a == b:
            similar += a
        else:
            if not found_diff:
                found_diff = True
            else:
                return False
    return similar


def find_common(box_ids):
    for i, first_box in enumerate(box_ids):
        for second_box in box_ids[i + 1:]:
            check_result = check_close_ids(first_box, second_box)
            if check_result:
                return check_result


def find_common_from_file(filename):
    with open(filename) as f:
        box_ids = [line for line in f]
    return find_common(box_ids)


if __name__ == "__main__":
    print(calc_checksum("data/day02_input.txt"))
    print(find_common_from_file("data/day02_input.txt"))
