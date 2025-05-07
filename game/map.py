class GameMap:
    def __init__(self, size=4): #map size
        self.size = size

    def is_valid(self, position): #alows movement
        x, y = position
        return 0 <= x < self.size and 0 <= y < self.size

    def display(self, player_pos):
        for i in range(self.size):
            row = ""
            for j in range(self.size):
                if (i, j) == player_pos:
                    row += "[P]"
                else:
                    row += "[ ]"
            print(row)
        print()
