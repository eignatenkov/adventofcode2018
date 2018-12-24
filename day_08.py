def parse_input(filename):
    with open(filename) as f:
        input = list(map(int, f.readline().strip().split(' ')))
    return input


def produce_metadata(tree_input, start_position=0):
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


def compute_node_value(tree_input, start_position=0):
    n_childs, n_metadata = tree_input[start_position: start_position + 2]
    next_position = start_position + 2 + n_metadata
    if n_childs == 0:
        metadata = tree_input[start_position + 2:next_position]
        return sum(metadata), next_position
    else:
        child_values = []
        current_position = start_position + 2
        for i in range(n_childs):
            child_value, next_position = compute_node_value(tree_input, current_position)
            child_values.append(child_value)
            current_position = next_position
        metadata = tree_input[current_position:current_position + n_metadata]
        node_value = sum(child_values[i - 1] for i in metadata if 0 < i <= len(child_values))
        return node_value, current_position + n_metadata


if __name__ == "__main__":
    task_input = parse_input("data/day08_input.txt")
    print(sum(produce_metadata(task_input)[0]))
    print(compute_node_value(task_input)[0])
