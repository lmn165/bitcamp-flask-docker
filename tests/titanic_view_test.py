import unittest

<<<<<<< HEAD
from lecture.titanic.legacy.view import TitanicView
=======
from lecture.titanic.view.titanic_view import TitanicView
>>>>>>> 35435834777e479117f611cc4465f5fe32d2ce9b

class TitanicViewTest(unittest.TestCase):
    mock = TitanicView()

    def test_modeling(self):
        self.mock.modeling()

    # def test_submit(self):
    #     self.mock.submit()

if __name__ == '__main__':
    unittest.main()