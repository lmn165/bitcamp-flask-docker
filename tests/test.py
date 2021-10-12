import unittest


class scope_test(unittest.TestCase):
    x= 'global'
    def test(self):
        x = 'block-scope'
        print('*' * 100)
        print(x)
        print(self.x)