class Player:
    def __init__(self):
        self.position = (0, 0)

    def move(self, direction, game_map):
        delta = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}
        if direction in delta:
            new_pos = (self.position[0] + delta[direction][0], self.position[1] + delta[direction][1])
            if game_map.is_valid(new_pos):
                self.position = new_pos
