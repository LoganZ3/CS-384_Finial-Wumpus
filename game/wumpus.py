import random

class Wumpus:
    def __init__(self, size=4):
        self.size = size
        self.position = self._random_position()

    def _random_position(self):
        return (random.randint(0, self.size - 1), random.randint(0, self.size - 1))

    def move(self):
        old_position = self.position
        while True:
            new_position = self._random_position()
            if new_position != old_position:
                self.position = new_position
                break
        return True

    def shoot(self, direction, player_pos, game_map):
        deltas = {
            'N': (-1, 0), 'S': (1, 0),
            'E': (0, 1), 'W': (0, -1)
        }
        if direction not in deltas:
            return False

        dx, dy = deltas[direction]
        pos = player_pos

        while game_map.is_valid(pos):
            if pos == self.position:
                return True
            pos = (pos[0] + dx, pos[1] + dy)
        return False
