from collections import defaultdict


def read_input(filename):
    dependencies_dict = defaultdict(set)
    with open(filename) as f:
        for line in f:
            dependencies_dict[line[36]].add(line[5])
            if line[5] not in dependencies_dict:
                dependencies_dict[line[5]] = set()
    return dependencies_dict


if __name__ == "__main__":
    print(read_input('data/day07_input.txt'))
