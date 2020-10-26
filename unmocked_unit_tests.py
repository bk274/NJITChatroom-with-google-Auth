import sys
sys.path.append("..")

import unittest
from responses import chat

KEY_INPUT = "input"
KEY_EXPECTED = "expected"

class UnMockedTestCase(unittest.TestCase):
    
    def setUp(self):
        self.success_test_params = [
            {
                KEY_INPUT: "!!about",
                KEY_EXPECTED: "This a little about me, im a chatbout but also i have a chatroom that communicate with other peopple"
            },
            {
                KEY_INPUT: "!!help",
                KEY_EXPECTED: "The commands i respond to are !! followed by either help,about,date,Whats my favorite color, covid, or funtranslate (your message here)"
            },
            {
                KEY_INPUT: "!!Whats my favorite color",
                KEY_EXPECTED: "BLue"
            },
            {
                KEY_INPUT: "!!hello",
                KEY_EXPECTED: "command not recognized"
            },
            {
                KEY_INPUT: "!!funtranslate Good morning",
                KEY_EXPECTED: " Bitchin' morning"
            },
        ]
        
        self.failure_test_params = [
            {
                KEY_INPUT: "!!Who are you",
                KEY_EXPECTED: "It's me"
            },
            {
                KEY_INPUT: "!!date",
                KEY_EXPECTED: "2020/10/23"
   
            },
        ]

#---------------------------------------------------------------------------------------------------------------------------------------------

    def test_parse_message_success(self):
        chatbot = chat()

        for test in self.success_test_params:
            response = chatbot.response(test[KEY_INPUT])
            expected = test[KEY_EXPECTED]
            
            self.assertEqual(response, expected)
            
            # Alternatively (and preferably), you can do self.assertDictEqual(response, expected)

#---------------------------------------------------------------------------------------------------------------------------------------------
             
    def test_parse_message_failure(self):
        chatbot = chat()
        
        for test in self.failure_test_params:
            response = chatbot.response(test[KEY_INPUT])
            expected = test[KEY_EXPECTED]
            
            # TODO add assertNotEqual cases here instead
            self.assertNotEqual(response, expected)

#---------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
