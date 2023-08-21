import unittest
from whiteboard import solution

class MatchTestCase(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(solution(['NORTH','EAST','WEST','SOUTH','WEST','SOUTH','NORTH','WEST']),['WEST','WEST'])
    def test_example_two(self):
        self.assertEqual(solution( ['EAST','NORTH','WEST','SOUTH']),['EAST','NORTH','WEST','SOUTH'])
    def test_North(self):
        self.assertEqual(solution(["NORTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH", "SOUTH", "NORTH","WEST", "EAST"]),['NORTH', 'NORTH'])
    def test_West(self):
        self.assertEqual(solution(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]),['WEST'])

if __name__ == '__main__':
    unittest.main()