# game/main.py
from game.map import GameMap
from game.player import Player
from game.wumpus import Wumpus

def main():
    game_map = GameMap()
    player = Player()
    wumpus = Wumpus()

    print("Welcome to Hunt the Wumpus!")
    
    while True:
        game_map.display(player.position)
        move = input("Move (N/S/E/W) or shoot (SN/SS/SE/SW): ").strip().upper()

        if move.startswith("S"):
            if wumpus.shoot(move[1:], player.position, game_map):
                print("You shot the Wumpus! You win!")
                break
            else:
                print("Missed! The Wumpus is coming...")
                if wumpus.move():
                    if player.position == wumpus.position:
                        print("The Wumpus ate you!")
                        break
        else:
            player.move(move, game_map)
            if player.position == wumpus.position:
                print("You ran into the Wumpus! Game over!")
                break

if __name__ == "__main__":
    main()

