import numpy as np
from tqdm import tqdm


def plus_two_index(index, game_size):
    if index < game_size - 1:
        return index + 2
    else:
        return 1


def minus_seven_index(index, game_size):
    return (index - 7) % game_size


def play_the_game(n_players, n_marbles):
    # game_state = np.ones(n_marbles, dtype=int) * -1
    scores = np.zeros(n_players, dtype=int)
    # game_state[0] = 0
    game_state = np.zeros(1, dtype=int)
    current_index = 0
    for i in tqdm(range(1, n_marbles + 1)):
        if i % 23:
            index_to_insert = plus_two_index(current_index, game_state.shape[0])
            game_state = np.insert(game_state, index_to_insert, i)
            # game_state[index_to_insert + 1:game_size + 1] = game_state[index_to_insert:game_size]
            # game_state[index_to_insert] = i
            current_index = index_to_insert
        else:
            index_to_remove = minus_seven_index(current_index, game_state.shape[0])
            scores[(i - 1) % n_players] += i + game_state[index_to_remove]
            game_state = np.delete(game_state, index_to_remove)
            # game_state[index_to_remove:game_size - 1] = game_state[index_to_remove + 1:game_size]
            # game_state[game_size - 1] = -1
            current_index = index_to_remove
    return scores


print(play_the_game(447, 71510).max())
print(play_the_game(447, 71510 * 100).max())