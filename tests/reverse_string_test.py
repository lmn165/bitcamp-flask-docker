import unittest
from pprint import pprint

class ReverseStringTest(unittest.TestCase):
    def test_str_to_list(self):
        pprint([i for i in "apple"])

    def test_reverseString(self):
        ls = [i for i in "apple"]
        pprint([ls[i] for i in range(len(ls)-1, -1, -1)])

    def test_list_to_str(self) -> []:
        ls = [i for i in "apple"]
        ls = [ls[i] for i in range(len(ls) - 1, -1, -1)]
        print(''.join([i for i in ls]))


if __name__ == '__main__':
    unittest.main