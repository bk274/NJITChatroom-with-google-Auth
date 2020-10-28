"""
Bot Module
"""
from datetime import datetime
from bot_api import get_result_from_api

def response(text):
    """Mothod for Processing Bot text"""
    result = "command not recognized"
    if text == "!!about":
        result = """This a little about me, im a chatbout but also i have a chatroom
            that communicate with other peopple"""
    elif text == "!!help":
        result = """The commands i respond to are !! followed by either help,about,date,
            Whats my favorite color, covid, or funtranslate (your message here)"""
    elif text == "!!date":
        result = "The date is: " + str(datetime.today())
    elif text == "!!Whats my favorite color":
        result = "BLue"
    elif text == "!!covid" or text.startswith("!!funtranslate"):
        result = get_result_from_api(text)
    return result
