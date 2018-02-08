import unittest
import importlib
lambda_functions = importlib.import_module('New_Color_Skill.lambda.custom')


class TestBasic(unittest.TestCase):

    def setUp(self):
        pass

    def test_basic_case(self):
        result = lambda_functions.build_response('a', 'b')
        self.assertIsNotNone(result)
