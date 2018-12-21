from collections import defaultdict


def read_input(filename):
    dependencies_dict = defaultdict(set)
    with open(filename) as f:
        for line in f:
            dependencies_dict[line[36]].add(line[5])
            if line[5] not in dependencies_dict:
                dependencies_dict[line[5]] = set()
    return dependencies_dict


def duration(letter, shift=60):
    return shift + ord(letter) - 64


def remove_dependency(graph, vertex):
    return {k: v - {vertex} for k, v in graph.items()}


def one_step(graph, workers_dict, n_workers=5, shift=60):
    next_time = min(workers_dict.values()) if workers_dict else 0
    next_to_be_done = [letter for letter, letter_time in workers_dict.items() if
                       letter_time == next_time]
    for done in next_to_be_done:
        workers_dict.pop(done)
        graph = remove_dependency(graph, done)

    independent = sorted([k for k, v in graph.items() if not v])
    for letter in independent:
        if len(workers_dict) < n_workers:
            workers_dict[letter] = next_time + duration(letter, shift)
            graph.pop(letter)
    return graph, workers_dict


if __name__ == "__main__":
    task_input = dict(read_input('data/day07_input.txt'))
    result = ''
    while task_input:
        independent = {k for k, v in task_input.items() if not v}
        next = min(independent)
        result += next
        task_input.pop(next)
        task_input = remove_dependency(task_input, next)
    print(result)
    task_input = dict(read_input('data/day07_input.txt'))
    workers_dict = {}
    while task_input:
        task_input, workers_dict = one_step(task_input, workers_dict)
    print(workers_dict)
