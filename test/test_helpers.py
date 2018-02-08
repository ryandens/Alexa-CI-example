import unittest
import importlib

lambda_functions = importlib.import_module('Color_Picker.lambda.custom')


class TestBasic(unittest.TestCase):

    def setUp(self):
        pass

    def test_build_speechlet_response(self):
        response = lambda_functions.helpers.build_speechlet_response('title', 'output', 'reprompt_text', 'should_end_session')

        expected_response = {
            'outputSpeech': {
                'type': 'PlainText',
                'text': 'output'
            },
            'card': {
                'type': 'Simple',
                'title': "SessionSpeechlet - " + 'title',
                'content': "SessionSpeechlet - " + 'output'
            },
            'reprompt': {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': 'reprompt_text'
                }
            },
            'shouldEndSession': 'should_end_session'
        }

        self.assertEqual(response, expected_response)
