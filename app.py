from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('chat.html')

@socketio.on('message')
def handleMessage(data):
    print(f"{data['user']} said: {data['msg']}")
    emit('message', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
