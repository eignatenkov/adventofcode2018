class LinkedList:
    def __init__(self, input_dict=None, pointer=None):
        self.ll = dict() if input_dict is None else input_dict
        self.pointer = pointer

    def move_forward(self, n_steps):
        for _ in range(n_steps):
            self.pointer = self.ll[self.pointer][1]

    def move_backward(self, n_steps):
        for _ in range(n_steps):
            self.pointer = self.ll[self.pointer][0]

    def insert_before(self, value):
        prev = self.ll[self.pointer][0]
        self.ll[value] = [self.ll[self.pointer][0], self.pointer]
        self.ll[prev][1] = value
        self.ll[self.pointer][0] = value
        self.pointer = value

    def delete(self):
        prev = self.ll[self.pointer][0]
        next = self.ll[self.pointer][1]
        self.ll.pop(self.pointer)
        self.ll[prev][1] = next
        self.ll[next][0] = prev
        self.pointer = next


def linked_list_game(n_players, n_marbles):
    scores = [0] * n_players
    game_state = LinkedList({0: [0, 0]}, pointer=0)
    for i in range(1, n_marbles + 1):
        if i % 23:
            game_state.move_forward(2)
            game_state.insert_before(i)
        else:
            game_state.move_backward(7)
            scores[(i - 1) % n_players] += i + game_state.pointer
            game_state.delete()
    return scores


print(max(linked_list_game(447, 71510)))
print(max(linked_list_game(447, 71510 * 100)))
