import unittest
from web_pages.web_page import Web_page

class web_page_test(unittest.TestCase):
    def test_web_page(self):
        test_obj=Web_page()
        self.assertEqual(test_obj.list_web_page['Ford'], 8, msg="weight of car should be 7")
