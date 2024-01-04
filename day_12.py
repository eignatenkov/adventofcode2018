def read_input(filepath):
    initial_state = None
    rules = dict()
    with open(filepath) as f:
        for line in f:
            if line.startswith("initial state"):
                initial_state = line.strip()[15:]
            elif line.strip():
                k, v = line.strip().split(' => ')
                rules[k] = True if v == '#' else False
    return initial_state, rules


def key_from_pos(pos, plants):
    return ''.join('#' if i in plants else '.' for i in range(pos - 2, pos + 3))


def run_generation(plants, rules):
    new_plants = set()
    for i in range(min(plants) - 4, max(plants) + 4):
        key = key_from_pos(i, plants)
        if rules[key]:
            new_plants.add(i)
    return new_plants


def find_loop(plants):
    is_processed = tuple(sorted(plants))
    states = [(is_processed, 0)]
    iter_counter = 0
    while True:
        plants = run_generation(plants, rules)
        iter_counter += 1
        shift = min(plants)
        new_state = tuple(sorted(p - shift for p in plants))
        for i, s in enumerate(states):
            if new_state == s[0]:
                return iter_counter, i, s, shift
        states.append((new_state, shift))


initial_state, rules = read_input('data/day_12.txt')
plants = {i for i, p in enumerate(initial_state) if p == '#'}

for i in range(20):
    plants = run_generation(plants, rules)
print(sum(plants))


plants = {i for i, p in enumerate(initial_state) if p == '#'}
iter_counter, i, s, shift = find_loop(plants)
n_steps = 50000000000
print((n_steps - i + s[1]) * len(s[0]) + sum(s[0]))