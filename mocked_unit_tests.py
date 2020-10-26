'''
    mocked_unit_tests.py
    
    This file tests app.py, responses.py
'''

import sys
sys.path.append("..")

import unittest
import unittest.mock as mock

import json
from responses import chat
from app import on_connect

KEY_INPUT = "input"
KEY_METHOD = "method"
KEY_EXPECTED = "expected"

KEY_MESSAGE_ID = "id"
KEY_MESSAGE_CONTENT = "message"
KEY_MESSAGE_STAMP = "stamp"
KEY_MESSAGE_NAME = "from_name"
KEY_MESSAGE_AVATAR = "from_avatar"

class MockedAPIResponse:

    def __init__(self, text):
        self.status_code = 200
        self.text = text
    
    def json(self):
        return json.loads(self.text)

#---------------------------------------------------------------------------------------------------------------------------------------------

class MockedMessageResultProxy:

    def __init__(self, id, message, stamp, from_name, from_avatar):
        self.message = 200
        self.id = id
        self.message = message
        self.stamp = stamp
        self.from_name = from_name
        self.from_avatar = from_avatar

#---------------------------------------------------------------------------------------------------------------------------------------------

class MockedTestCase(unittest.TestCase):

    def setUp(self):
        self.success_api_test_params = [
            {
                KEY_INPUT: "!!covid",
                KEY_EXPECTED: "Recovered in USA: 3406656",
                KEY_METHOD: self.mocked_requests_covid
            },
            {
                KEY_INPUT: "!!funtranslate Good morning",
                KEY_EXPECTED: "Bitchin' morning",
                KEY_METHOD: self.mocked_requests_translate
            }
        ]

        self.success_db_test_params = [
            [
                "Good morning.",
                "2020-10-25 10:55:22.562775",
                "Talay Chatisut",
                "https://lh5.googleusercontent.com/-Mxzl-1ElVkQ/AAAAAAAAAAI/AAAAAAAAAAA/AMZuuckbSuIKOL_xD6PeIEienyZ-3Yeh2g/s96-c/photo.jpg"
            ],
            [
                "Nice to meet you",
                "2018-11-10 22:32:11.250000",
                "Mathieu Dionne",
                "https://lh6.googleusercontent.com/-p2w6xZQhv2w/AAAAAAAAAAI/AAAAAAAAAAA/AMZuucleAz4IFlrQgajzDOOHtv9RULFesw/s96-c/photo.jpg"
            ]
        ]
        
    #---------------------------------------------------------------------------------------------------------------------------------------------
        
    def mocked_requests_translate(self, url, headers):
        return MockedAPIResponse("""{"contents": {"translated": "Bitchin' morning"}}""")

    def mocked_requests_covid(self, url, headers, params):
        return MockedAPIResponse("""{"data": {"recovered":3406656}}""")

    def test_api_success(self):
        chatbot = chat()
        
        for test_case in self.success_api_test_params:
            with mock.patch('requests.get', test_case[KEY_METHOD]):
                result = chatbot.response(test_case[KEY_INPUT])
            
            expected = test_case[KEY_EXPECTED]
        
            self.assertEqual(result, expected)

    #---------------------------------------------------------------------------------------------------------------------------------------------    

    def mocked_session_execute(self, query):
        return[
            MockedMessageResultProxy(
                1,
                "Good morning.",
                "2020-10-25 10:55:22.562775",
                "Talay Chatisut",
                "https://lh5.googleusercontent.com/-Mxzl-1ElVkQ/AAAAAAAAAAI/AAAAAAAAAAA/AMZuuckbSuIKOL_xD6PeIEienyZ-3Yeh2g/s96-c/photo.jpg"
            ),
            MockedMessageResultProxy(
                2, 
                "Nice to meet you",
                "2018-11-10 22:32:11.250000",
                "Mathieu Dionne",
                "https://lh6.googleusercontent.com/-p2w6xZQhv2w/AAAAAAAAAAI/AAAAAAAAAAA/AMZuucleAz4IFlrQgajzDOOHtv9RULFesw/s96-c/photo.jpg"
            )
        ]

    def test_db_success(self):
        with mock.patch("app.db.session.execute", self.mocked_session_execute):
            result = on_connect()

        self.assertEqual(result, self.success_db_test_params)
    

if __name__ == '__main__':
    unittest.main()
