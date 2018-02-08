import unittest
import importlib

lambda_functions = importlib.import_module('Color_Picker.lambda.custom')


class TestBasic(unittest.TestCase):

    def setUp(self):
        pass

    def test_basic_case(self):
        self.assertEqual(5, 5)
