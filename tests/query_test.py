import unittest
from queries.query import Query

class query_test(unittest.TestCase):
    def test_query(self):
        test_obj = Query()
        self.assertEqual(test_obj.list_query['Ford'], 8, msg="weight of ford should be 8")