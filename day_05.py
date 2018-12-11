from string import ascii_lowercase
from tqdm import tqdm

def reduce_once(line):
    new_line = ''
    i = 0
    while i < len(line) - 1:
        letter = line[i]
        next_letter = line[i + 1]
        if letter.lower() == next_letter.lower() and letter != next_letter:
            i += 2
        else:
            new_line += letter
            i += 1
        if i == len(line) - 1:
            new_line += line[-1]
            i += 1
    return new_line


def reduce_all(alchemy_line):
    while True:
        current_length = len(alchemy_line)
        alchemy_line = reduce_once(alchemy_line)
        if len(alchemy_line) == current_length:
            return current_length


def remove_polymer(line, polymer):
    new_line = ''
    for letter in line:
        if letter.lower() != polymer:
            new_line += letter
    return new_line


def find_best_with_removal(line):
    new_lengths = []
    for polymer in tqdm(ascii_lowercase):
        test_line = remove_polymer(line, polymer)
        new_lengths.append(reduce_all(test_line))
    return min(new_lengths)


if __name__ == "__main__":
    with open("data/day05_input.txt") as f:
        alchemy_line = f.readline().strip()
    print(reduce_all(alchemy_line))
    print(find_best_with_removal(alchemy_line))
