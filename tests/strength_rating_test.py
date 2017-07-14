import unittest
from client.strength_rating import Strength_rating
class Strenght_rating_test(unittest.TestCase):
    def test_strength_rating(self):
        test_obj=Strength_rating()
        strength=test_obj.calculate_strength('Ford')
