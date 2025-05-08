#to test move file into the largest folder (where main is) dont know why this is but it works. keeping folder to avoid clutter
import unittest
from game.map import GameMap

class TestGameMap(unittest.TestCase):
    def test_valid_position(self):
        gmap = GameMap(size=4)
        self.assertTrue(gmap.is_valid((2, 3)))
        self.assertFalse(gmap.is_valid((4, 4)))
        self.assertFalse(gmap.is_valid((-1, 0)))

    def test_display(self):
        gmap = GameMap(size=2)
        gmap.display((0, 0))

if __name__ == '__main__':
    unittest.main()
