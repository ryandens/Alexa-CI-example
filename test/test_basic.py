import unittest


class TestBasic(unittest.TestCase):

    def setUp(self):
        pass

    def test_basic_case(self):
        self.assertEqual(5, 5)
