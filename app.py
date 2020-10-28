"""
Main Module
"""
from os.path import join, dirname
from datetime import datetime
import os
from dotenv import load_dotenv
import flask
import flask_sqlalchemy
import flask_socketio
from responses import response

MESSAGES_RECEIVED_CHANNEL = 'messages received'
MESSAGES = 'messages'
USERS = 'users'
KEY_ID = "id"

KEY_BOT_MESSAGE = "bot_message"
KEY_HUMAN_MESSAGE = "human_message"

app = flask.Flask(__name__)

#

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")
dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)
sql_user = os.environ['SQL_USER']
sql_pwd = os.environ['SQL_PASSWORD']
dbuser = os.environ['USER']
database_uri = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#

db = flask_sqlalchemy.SQLAlchemy(app)
db.init_app(app)
db.app = app

users = set()

try:
    # pylint: disable=maybe-no-member
    db.session.execute(
        """CREATE TABLE messages (
            id serial PRIMARY KEY,
            message VARCHAR ( 255 ) NOT NULL,
            stamp TIMESTAMP NOT NULL,
            from_name VARCHAR ( 255 ),
            from_avatar VARCHAR ( 255 ));""")
    db.session.commit()
except:# pylint: disable=bare-except
    # pylint: disable=maybe-no-member
    db.session.rollback()

#

def emit_all_messages(channel):
    """Method for send message to client"""
    # pylint: disable=maybe-no-member
    messages = [[db_user.message, str(db_user.stamp), db_user.from_name, db_user.from_avatar]
                for db_user in db.session.execute("SELECT * FROM messages")]

    data = {
        MESSAGES: messages,
        USERS: len(users)
    }

    socketio.emit(channel, data)

    return data

#

@socketio.on('connect')
def on_connect():
    """Method for send message to client at first"""
    return emit_all_messages(MESSAGES_RECEIVED_CHANNEL)

#

@socketio.on('new user input')
def on_user_signin(data = None):
    """Method for notice client that new user enter the room"""
    users.add(data["id"])
    return emit_all_messages(MESSAGES_RECEIVED_CHANNEL)


@socketio.on('new user output')
def on_user_logout(data = None):
    """Method for notice client that new user out the room"""
    users.remove(data["id"])
    return emit_all_messages(MESSAGES_RECEIVED_CHANNEL)

#

@socketio.on('new message input')
def on_new_message(data):
    """Method for process chat text"""
    now = datetime.now()
    new_message = data["message"].replace('\'', '\'\'')
    new_name = data["name"].replace('\'', '\'\'')
    new_avatar = data["avatar"].replace('\'', '\'\'')

    # pylint: disable=maybe-no-member
    [new_id] = db.session.execute("""INSERT INTO messages (message, stamp, from_name, from_avatar)
                        VALUES ('""" +
                        new_message + "','" + str(now) + "', '" + new_name + "', '" + new_avatar +
                        """')
                        RETURNING id""").fetchone()

    db.session.commit()
    message_value = str(new_message)

    if message_value[:2] == '!!':
        now = datetime.now()
        bot_message = response(data["message"]).replace('\'', '\'\'')
        [new_bot_id] = db.session.execute("""INSERT INTO messages (message, stamp, from_name)
                        VALUES ('""" +
                        bot_message + "','" + str(now) + """', 'bot'
                        )
                        RETURNING id""").fetchone()
        db.session.commit()

        emit_all_messages(MESSAGES_RECEIVED_CHANNEL)

        return {
            KEY_HUMAN_MESSAGE: [new_id, new_message, new_name, new_avatar],
            KEY_BOT_MESSAGE: [new_bot_id, bot_message]
        }

    emit_all_messages(MESSAGES_RECEIVED_CHANNEL)

    return [new_id, new_message, new_name, new_avatar]

#

@app.route('/')
def index():
    """Method for routing index page"""
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL)
    return flask.render_template("index.html")

if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=8082,
        debug=True
    )
