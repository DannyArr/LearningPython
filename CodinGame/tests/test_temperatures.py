# https://www.codingame.com/ide/puzzle/temperatures

from context import games
import unittest
from collections import Counter

# Simple test case
class TestTemp(unittest.TestCase):

    def test01(self): #Simple test case
        self.assertEqual(games.temperatures.Attempt1("1 -2 -8 4 5"),1)    

    def test02(self): #Only negative numbers
        self.assertEqual(games.temperatures.Attempt1("-12 -5 -137"),-5)

    def test03(self): #Choose the right temperature
        self.assertEqual(games.temperatures.Attempt1("42 -5 12 21 5 24"),5)

    def test04(self): #Choose the right temperature 2
        self.assertEqual(games.temperatures.Attempt1("42 5 12 21 -5 24"),5)

    def test05(self): #Complex test case
        self.assertEqual(games.temperatures.Attempt1("-5 -4 -2 12 -40 4 2 18 11 5"),2)

    def test06(self): #No temperature
        self.assertEqual(games.temperatures.Attempt1(""),0)


if(__name__ == "__main__"):
    unittest.main()