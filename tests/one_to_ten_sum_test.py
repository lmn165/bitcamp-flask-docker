import unittest


class OntToTenSumTest(unittest.TestCase):
    def test_one_to_ten_sum_1(self):
        sum = 0
        for i in range(1, 11):  # basic loop shape
            sum += i
        print(sum)

    def test_one_to_ten_sum_2(self):
        print(sum(i for i in range(1, 11)))

    def test_one_to_ten_sum_3(self):
        print(f'{range(1, 11)}')

if __name__ == '__main__':
    unittest.main