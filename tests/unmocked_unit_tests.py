import sys
sys.path.append("..")

import unittest
from responses import response

import sqlalchemy

KEY_INPUT = "input"
KEY_EXPECTED = "expected"

class UnMockedTestCase(unittest.TestCase):
    
    def setUp(self):
        self.failure_msg_about_params = {
            KEY_INPUT: "!!about ",
            KEY_EXPECTED: "This is not about text"
        }

        self.success_msg_about_params = {
            KEY_INPUT: "!!about",
            KEY_EXPECTED: """This a little about me, im a chatbout but also i have a chatroom
            that communicate with other peopple"""
        }

        self.failure_msg_help_params = {
            KEY_INPUT: "!! help",
            KEY_EXPECTED: "This is not help text"
        }

        self.success_msg_help_params = {
            KEY_INPUT: "!!help",
            KEY_EXPECTED: """The commands i respond to are !! followed by either help,about,date,
            Whats my favorite color, covid, or funtranslate (your message here)"""
        }

        self.success_msg_color_params = {
            KEY_INPUT: "!!Whats my favorite color",
            KEY_EXPECTED: "BLue"
        }

        self.failure_msg_color_params = {
            KEY_INPUT: "!!What's my favorite color",
            KEY_EXPECTED: "You mean: Whats my favorite color"
        }

        self.success_msg_error_params = {
            KEY_INPUT: "!!hello",
            KEY_EXPECTED: "command not recognized"
        }

        self.success_msg_error1_params = {
            KEY_INPUT: "!!d a t e",
            KEY_EXPECTED: "command not recognized"
        }

        self.success_msg_error2_params = {
            KEY_INPUT: "!! about ",
            KEY_EXPECTED: "command not recognized"
        }

        self.failure_msg_date_params = {
            KEY_INPUT: "!!date",
            KEY_EXPECTED: "2020/10/23"
        }

#---------------------------------------------------------------------------------------------------------------------------------------------

    def test_about_message_failure(self):
        test = self.failure_msg_about_params

        result = response(test[KEY_INPUT])
        expected = test[KEY_EXPECTED]
        
        self.assertNotEqual(result, expected)

#---------------------------------------------------------------------------------------------------------------------------------------------

    def test_about_message_success(self):
        test = self.success_msg_about_params

        result = response(test[KEY_INPUT])
        expected = test[KEY_EXPECTED]
        
        self.assertEqual(result, expected)
            
#---------------------------------------------------------------------------------------------------------------------------------------------

    def test_help_message_failure(self):
        test = self.failure_msg_help_params

        result = response(test[KEY_INPUT])
        expected = test[KEY_EXPECTED]
        
        self.assertNotEqual(result, expected)

#---------------------------------------------------------------------------------------------------------------------------------------------

    def test_help_message_success(self):
        test = self.success_msg_help_params

        result = response(test[KEY_INPUT])
        expected = test[KEY_EXPECTED]
        
        self.assertEqual(result, expected)
            
#---------------------------------------------------------------------------------------------------------------------------------------------

    def test_color_message_success(self):
        test = self.success_msg_color_params

        result = response(test[KEY_INPUT])
        expected = test[KEY_EXPECTED]
        
        self.assertEqual(result, expected)

#---------------------------------------------------------------------------------------------------------------------------------------------

    def test_color_message_failure(self):
        test = self.failure_msg_color_params

        result = response(test[KEY_INPUT])
        expected = test[KEY_EXPECTED]
        
        self.assertNotEqual(result, expected)
            
#---------------------------------------------------------------------------------------------------------------------------------------------

    def test_error_message_success(self):
        test = self.success_msg_error_params

        result = response(test[KEY_INPUT])
        expected = test[KEY_EXPECTED]
        
        self.assertEqual(result, expected)

#---------------------------------------------------------------------------------------------------------------------------------------------

    def test_error_message1_success(self):
        test = self.success_msg_error1_params

        result = response(test[KEY_INPUT])
        expected = test[KEY_EXPECTED]
        
        self.assertEqual(result, expected)

#---------------------------------------------------------------------------------------------------------------------------------------------

    def test_error_message2_success(self):
        test = self.success_msg_error2_params

        result = response(test[KEY_INPUT])
        expected = test[KEY_EXPECTED]
        
        self.assertEqual(result, expected)
            
#---------------------------------------------------------------------------------------------------------------------------------------------
             
    def test_date_message_failure(self):
        test = self.failure_msg_date_params
        
        result = response(test[KEY_INPUT])
        expected = test[KEY_EXPECTED]
        
        # TODO add assertNotEqual cases here instead
        self.assertNotEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
