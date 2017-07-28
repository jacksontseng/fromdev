import sys
import unittest

from basketball import home_or_away, team_colors, player_points, player_stats, shoe_size, big_shoe_stealer

class TestHomeAway(unittest.TestCase):
    def test_home_or_away(self):
        self.assertEqual(home_or_away('Brooklyn Nets'), 'home')

class TestTeamColors(unittest.TestCase):
    def test_team_colors(self):
        self.assertEqual(team_colors('Brooklyn Nets'), 'Black and White')

class TestPlayerPoints(unittest.TestCase):
    def test_player_points(self):
        self.assertEqual(player_points('Charlotte Hornets'), 'Jeff Adrien - 10 pts, Bismak Biyombo - 12 pts, DeSagna Diop - 24 pts, Ben Gordon - 33 pts, Brendan Haywood - 6 pts.')

class TestPlayerStats(unittest.TestCase):
    def test_player_stats(self):
        self.assertEqual(player_stats("Charlotte Hornets", "Ben Gordon"), 'Name: Ben Gordon\nSlam_dunks: 0\nNumber: 8\nPoints: 33\nShoe: 15\nSteals: 1')

class TestShoeSize(unittest.TestCase):
    def test_shoe_size(self):
        self.assertEqual(shoe_size("Charlotte Hornets", "DeSagna Diop"), 14)

class TestBigShoeSteals(unittest.TestCase):
    def test_big_shoe_stealer(self):
        self.assertEqual(big_shoe_stealer('Brooklyn Nets'), 3)

if __name__ == '__main__':
    unittest.main()
