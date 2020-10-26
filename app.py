from os.path import join, dirname
from dotenv import load_dotenv
from datetime import datetime
import os
import flask
import flask_sqlalchemy
import flask_socketio
import responses
import time

MESSAGES_RECEIVED_CHANNEL = 'messages received'

app = flask.Flask(__name__)

#---------------------------------------------------------------------------------------------------------------------------------------------

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")
dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)
sql_user = os.environ['SQL_USER']
sql_pwd = os.environ['SQL_PASSWORD']
dbuser = os.environ['USER']
database_uri = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    
#---------------------------------------------------------------------------------------------------------------------------------------------

db = flask_sqlalchemy.SQLAlchemy(app)
db.init_app(app)
db.app = app
Response = responses.chat()

users = set()

try:
    db.session.execute(
        """CREATE TABLE messages (
            id serial PRIMARY KEY,
            message VARCHAR ( 255 ) NOT NULL,
            stamp TIMESTAMP NOT NULL,
            from_name VARCHAR ( 255 ),
            from_avatar VARCHAR ( 255 ));""")
    db.session.commit()
except:
    print("messages db created")
    
#---------------------------------------------------------------------------------------------------------------------------------------------


def emit_all_messages(channel):
    messages = [[db_user.message, str(db_user.stamp), db_user.from_name, db_user.from_avatar]
                for db_user in db.session.execute("SELECT * FROM messages")]

    
    socketio.emit(channel, {
        'messages': messages,
        'users': len(users)
    })
    
#---------------------------------------------------------------------------------------------------------------------------------------------


@socketio.on('connect')
def on_connect():
    print('Someone connection +++++++')
    socketio.emit('connected', {
        'test': 'Connected'
    })

    emit_all_messages(MESSAGES_RECEIVED_CHANNEL)


@socketio.on('disconnect')
def on_disconnect():
    print('Someone disconnected +++++++')
    
#---------------------------------------------------------------------------------------------------------------------------------------------


@socketio.on('new user input')
def on_user_signin(data):
    print("Got an event for new user input with data:", data)

    users.add(data["id"])
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL)


@socketio.on('new user output')
def on_user_logout(data):
    print("Got an event for new user output with data:", data)

    users.remove(data["id"])
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL)    
    
#---------------------------------------------------------------------------------------------------------------------------------------------

@socketio.on('new message input')
def on_new_message(data):
    print("Got an event for new message input with data:", data)

    now = datetime.now()
    new_message = data["message"].replace('\'', '\'\'')
    new_name = data["name"].replace('\'', '\'\'')
    new_avatar = data["avatar"].replace('\'', '\'\'')

    db.session.execute("INSERT INTO messages (message, stamp, from_name, from_avatar) VALUES ('" +
                       new_message + "','" + str(now) + "', '" + new_name + "', '" + new_avatar + "');")
    db.session.commit()
    message_value = str(new_message)

    if(message_value[:2] == '!!'):
        now = datetime.now()
        response = Response.response(data["message"]).replace('\'', '\'\'')
        db.session.execute("INSERT INTO messages (message, stamp, from_name) VALUES ('" +
                           response + "','" + str(now) + "', 'bot');")
        db.session.commit()
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL)
    
    
    
#---------------------------------------------------------------------------------------------------------------------------------------------


@app.route('/')
def index():
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL)
    return flask.render_template("index.html")



if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8082)),
        debug=True
    )
