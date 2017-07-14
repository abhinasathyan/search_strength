import unittest
from client.parser import Parser

class TestParser(unittest.TestCase):
    def test_shouldParseCommands(self):
        testObj=Parser()
        parsed=testObj.split("P Ford Car Review")
        self.assertEqual(parsed[0], "p",msg= "should parse p")
        self.assertEqual(parsed[1], "ford",msg= "should parse ford")
        self.assertEqual(parsed[2],"car",msg="should parse car")
        self.assertEqual(parsed[3],"review",msg="should parse review")