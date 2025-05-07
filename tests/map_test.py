from game.map import GameMap

def main():
    game_map = GameMap(size=4)
    player_pos = (2, 1)  #start position
    game_map.display(player_pos)

if __name__ == "__main__":
    main()