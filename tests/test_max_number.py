import unittest
import src.max_number as max_number
from src.database import Database


class TestMaxNumber(unittest.TestCase):
    def setUp(self):
        self.data = Database()

    def test_number_123(self):
        number = [1, 2, 3]
        old = max_number.old(number)
        new = max_number.largest_number(number)
        print("\n", old, new)
        assert old == new
    

    def test_number_739812673981276398127638127368217(self):
        l = "739812673981276398127638127368217"
        number = [int(x) for x in l]
        # old = max_number.old(number)
        old = max_number.old_database(number)
        new = max_number.largest_number(number)
        print("\n", old, new)
        # assert old == new

    def test_database_123(self):
        self.data.insert_number(123)
        self.data.insert_number(999)
        assert self.data.select_max_number() == 999
        
    