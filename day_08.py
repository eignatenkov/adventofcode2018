def parse_input(filename):
    with open(filename) as f:
        input = list(map(int, f.readline().strip().split(' ')))
    return input


def produce_metadata(tree_input, start_position):
    metadata = []
    n_childs, n_metadata = tree_input[start_position: start_position + 2]
    if n_childs == 0:
        next_position = start_position + 2 + n_metadata
        metadata = tree_input[start_position + 2:next_position]
        return metadata, next_position
    else:
        current_position = start_position + 2
        for i in range(n_childs):
            child_metadata, next_position = produce_metadata(tree_input, current_position)
            metadata.extend(child_metadata)
            current_position = next_position
        metadata.extend(tree_input[current_position: current_position + n_metadata])
        return metadata, current_position + n_metadata


if __name__ == "__main__":
    print(sum(produce_metadata(parse_input("data/day08_input.txt"), 0)[0]))
