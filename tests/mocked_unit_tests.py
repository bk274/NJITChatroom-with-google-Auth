'''
    mocked_unit_tests.py
    
    This file tests app.py, responses.py
'''

from app import *
from responses import response
import json
import unittest.mock as mock
import unittest
import sys
sys.path.append("..")


KEY_INPUT = "input"
KEY_METHOD = "method"
KEY_EXPECTED = "expected"


class MockedAPIResponse:

    def __init__(self, text):
        self.status_code = 200
        self.text = text

    def json(self):
        return json.loads(self.text)

# ---------------------------------------------------------------------------------------------------------------------------------------------


class MockedMessageResultProxy:

    def __init__(self, id, message, stamp, from_name, from_avatar):
        self.message = 200
        self.id = id
        self.message = message
        self.stamp = stamp
        self.from_name = from_name
        self.from_avatar = from_avatar

# ---------------------------------------------------------------------------------------------------------------------------------------------


class MockedTestCase(unittest.TestCase):

    def setUp(self):
        self.success_msg_translate_params = {
            KEY_INPUT: "!!funtranslate Good morning",
            KEY_EXPECTED: "Bitchin' morning",
            KEY_METHOD: self.mocked_requests_translate
        }

        self.success_msg_covid_params = {
            KEY_INPUT: "!!covid",
            KEY_EXPECTED: "Recovered in USA: 3406656",
            KEY_METHOD: self.mocked_requests_covid
        }

        self.success_messages_params = [
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

        self.success_signin_test_params = {
            KEY_INPUT: {
                KEY_ID: 123
            },
            KEY_EXPECTED: {
                MESSAGES: self.success_messages_params,
                USERS: 1
            }
        }

        self.success_logout_test_params = {
            KEY_INPUT: {
                KEY_ID: 123
            },
            KEY_EXPECTED: {
                MESSAGES: self.success_messages_params,
                USERS: 0
            }
        }

        self.success_error_msg_params = {
            KEY_INPUT: {
                "message": "!!Mocked Test",
                "name": "Tester",
                "avatar": "https://lh6.googleusercontent.com/-p2w6xZQhv2w/AAAAAAAAAAI/AAAAAAAAAAA/AMZuucleAz4IFlrQgajzDOOHtv9RULFesw/s96-c/photo.jpg"
            },

            KEY_EXPECTED: {
                KEY_HUMAN_MESSAGE: [1, "!!Mocked Test", "Tester", "https://lh6.googleusercontent.com/-p2w6xZQhv2w/AAAAAAAAAAI/AAAAAAAAAAA/AMZuucleAz4IFlrQgajzDOOHtv9RULFesw/s96-c/photo.jpg"],
                KEY_BOT_MESSAGE: [1, "command not recognized"]
            }
        }

        self.failure_about_msg_params = {
            KEY_INPUT: {
                "message": "!!about",
                "name": "Tester",
                "avatar": "https://lh6.googleusercontent.com/-p2w6xZQhv2w/AAAAAAAAAAI/AAAAAAAAAAA/AMZuucleAz4IFlrQgajzDOOHtv9RULFesw/s96-c/photo.jpg"
            },

            KEY_EXPECTED: {
                KEY_HUMAN_MESSAGE: [3, "Message Error", "Tester", "https://lh6.googleusercontent.com/-p2w6xZQhv2w/AAAAAAAAAAI/AAAAAAAAAAA/AMZuucleAz4IFlrQgajzDOOHtv9RULFesw/s96-c/photo.jpg"],
                KEY_BOT_MESSAGE: [3, "It's not bot message"]
            }
        }

        self.failure_help_msg_params = {
            KEY_INPUT: {
                "message": "!!help",
                "name": "Tester",
                "avatar": "https://lh6.googleusercontent.com/-p2w6xZQhv2w/AAAAAAAAAAI/AAAAAAAAAAA/AMZuucleAz4IFlrQgajzDOOHtv9RULFesw/s96-c/photo.jpg"
            },

            KEY_EXPECTED: {
                KEY_HUMAN_MESSAGE: [2, "!!help", "Tester", "https://lh6.googleusercontent.com/-p2w6xZQhv2w/AAAAAAAAAAI/AAAAAAAAAAA/AMZuucleAz4IFlrQgajzDOOHtv9RULFesw/s96-c/photo.jpg"],
                KEY_BOT_MESSAGE: [2, "Error Occurred"]
            }
        }

        self.success_color_msg_params = {
            KEY_INPUT: {
                "message": "!!Whats my favorite color",
                "name": "Tester",
                "avatar": "https://lh6.googleusercontent.com/-p2w6xZQhv2w/AAAAAAAAAAI/AAAAAAAAAAA/AMZuucleAz4IFlrQgajzDOOHtv9RULFesw/s96-c/photo.jpg"
            },

            KEY_EXPECTED: {
                KEY_HUMAN_MESSAGE: [4, "!!Whats my favorite color", "Tester", "https://lh6.googleusercontent.com/-p2w6xZQhv2w/AAAAAAAAAAI/AAAAAAAAAAA/AMZuucleAz4IFlrQgajzDOOHtv9RULFesw/s96-c/photo.jpg"],
                KEY_BOT_MESSAGE: [4, "BLue"]
            }
        }

        self.failure_date_msg_params = {
            KEY_INPUT: {
                "message": "!!date",
                "name": "Tester",
                "avatar": "https://lh6.googleusercontent.com/-p2w6xZQhv2w/AAAAAAAAAAI/AAAAAAAAAAA/AMZuucleAz4IFlrQgajzDOOHtv9RULFesw/s96-c/photo.jpg"
            },

            KEY_EXPECTED: {
                KEY_HUMAN_MESSAGE: [5, "!!date", "Tester", "https://lh6.googleusercontent.com/-p2w6xZQhv2w/AAAAAAAAAAI/AAAAAAAAAAA/AMZuucleAz4IFlrQgajzDOOHtv9RULFesw/s96-c/photo.jpg"],
                KEY_BOT_MESSAGE: [5, "2020/10/23"]
            }
        }

        self.success_normal_msg_params = {
            KEY_INPUT: {
                "message": "Nice to meet you",
                "name": "Tester",
                "avatar": "https://lh6.googleusercontent.com/-p2w6xZQhv2w/AAAAAAAAAAI/AAAAAAAAAAA/AMZuucleAz4IFlrQgajzDOOHtv9RULFesw/s96-c/photo.jpg"
            },

            KEY_EXPECTED: [6, "Nice to meet you", "Tester", "https://lh6.googleusercontent.com/-p2w6xZQhv2w/AAAAAAAAAAI/AAAAAAAAAAA/AMZuucleAz4IFlrQgajzDOOHtv9RULFesw/s96-c/photo.jpg"]
        }

    # ---------------------------------------------------------------------------------------------------------------------------------------------

    def mocked_requests_translate(self, url, headers):
        return MockedAPIResponse("""{"contents": {"translated": "Bitchin' morning"}}""")

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

    def mocked_requests_covid(self, url, headers, params):
        return MockedAPIResponse("""{"data": {"recovered":3406656}}""")

    # ---------------------------------------------------------------------------------------------------------------------------------------------

    def test_translate_msg_success(self):
        test = self.success_msg_translate_params

        with mock.patch('requests.get', test[KEY_METHOD]):
            result = response(test[KEY_INPUT])

        expected = test[KEY_EXPECTED]

        self.assertEqual(result, expected)

    # ---------------------------------------------------------------------------------------------------------------------------------------------

    def test_covid_msg_success(self):
        test = self.success_msg_covid_params

        with mock.patch('requests.get', test[KEY_METHOD]):
            result = response(test[KEY_INPUT])

        expected = test[KEY_EXPECTED]

        self.assertEqual(result, expected)

    # ---------------------------------------------------------------------------------------------------------------------------------------------

    def test_user_login_success(self):
        test = self.success_signin_test_params

        with mock.patch("app.db.session.execute", self.mocked_session_execute):
            result = on_user_signin(test[KEY_INPUT])

        self.assertEqual(result, test[KEY_EXPECTED])

    # ---------------------------------------------------------------------------------------------------------------------------------------------

    def test_user_logout_success(self):
        test = self.success_logout_test_params

        with mock.patch("app.db.session.execute", self.mocked_session_execute):
            result = on_user_logout(test[KEY_INPUT])

        self.assertEqual(result, test[KEY_EXPECTED])

    # ---------------------------------------------------------------------------------------------------------------------------------------------

    @mock.patch('app.db.session')
    def test_error_message_success(self, mock_session):
        mock_session.execute.return_value.fetchone.return_value = [1]
        test = self.success_error_msg_params
        
        socketio_mock = mock.MagicMock()
        with mock.patch('app.socketio', socketio_mock):
            result = on_new_message(test[KEY_INPUT])
            socketio_mock.emit.assert_called_once()

        self.assertEqual(result[KEY_HUMAN_MESSAGE], test[KEY_EXPECTED][KEY_HUMAN_MESSAGE])
        self.assertEqual(result[KEY_BOT_MESSAGE], test[KEY_EXPECTED][KEY_BOT_MESSAGE])

    # ---------------------------------------------------------------------------------------------------------------------------------------------

    @mock.patch('app.db.session')
    def test_help_message_failure(self, mock_session):
        mock_session.execute.return_value.fetchone.return_value = [2]
        test = self.failure_help_msg_params
        
        result = on_new_message(test[KEY_INPUT])

        socketio_mock = mock.MagicMock()
        with mock.patch('app.socketio', socketio_mock):
            socketio_mock.emit("ChatRoom", {
                MESSAGES: [["!!Unmocked Test", "Tester"]],
                USERS: 1
            })
            socketio_mock.emit.assert_called_once_with("ChatRoom", {
                MESSAGES: [["!!Unmocked Test", "Tester"]],
                USERS: 1
            })

        self.assertEqual(result[KEY_HUMAN_MESSAGE], test[KEY_EXPECTED][KEY_HUMAN_MESSAGE])
        self.assertNotEqual(result[KEY_BOT_MESSAGE], test[KEY_EXPECTED][KEY_BOT_MESSAGE])

    # ---------------------------------------------------------------------------------------------------------------------------------------------

    @mock.patch('app.db.session')
    def test_about_message_failure(self, mock_session):
        mock_session.execute.return_value.fetchone.return_value = [3]
        test = self.failure_about_msg_params
        
        result = on_new_message(test[KEY_INPUT])

        self.assertNotEqual(result[KEY_HUMAN_MESSAGE], test[KEY_EXPECTED][KEY_HUMAN_MESSAGE])
        self.assertNotEqual(result[KEY_BOT_MESSAGE], test[KEY_EXPECTED][KEY_BOT_MESSAGE])

    # ---------------------------------------------------------------------------------------------------------------------------------------------

    @mock.patch('app.db.session')
    def test_color_message_success(self, mock_session):
        mock_session.execute.return_value.fetchone.return_value = [4]
        test = self.success_color_msg_params
        
        result = on_new_message(test[KEY_INPUT])

        self.assertEqual(result[KEY_HUMAN_MESSAGE], test[KEY_EXPECTED][KEY_HUMAN_MESSAGE])
        self.assertEqual(result[KEY_BOT_MESSAGE], test[KEY_EXPECTED][KEY_BOT_MESSAGE])

    # ---------------------------------------------------------------------------------------------------------------------------------------------

    @mock.patch('app.db.session')
    def test_date_message_failure(self, mock_session):
        mock_session.execute.return_value.fetchone.return_value = [5]
        test = self.failure_date_msg_params
        
        result = on_new_message(test[KEY_INPUT])

        self.assertEqual(result[KEY_HUMAN_MESSAGE], test[KEY_EXPECTED][KEY_HUMAN_MESSAGE])
        self.assertNotEqual(result[KEY_BOT_MESSAGE], test[KEY_EXPECTED][KEY_BOT_MESSAGE])

    @mock.patch('app.db.session')
    def test_normal_message_success(self, mock_session):
        mock_session.execute.return_value.fetchone.return_value = [6]
        test = self.success_normal_msg_params
        
        result = on_new_message(test[KEY_INPUT])

        self.assertEqual(result, test[KEY_EXPECTED])

if __name__ == '__main__':
    unittest.main()
