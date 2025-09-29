from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app, cors_allowed_origins="*")

# 在线用户字典：{nickname: session_id}
online_users = {}

@app.route("/")
def index():
    return render_template("index.html")

# 登录
@socketio.on("login")
def handle_login(data):
    nickname = data["nickname"]
    online_users[nickname] = request.sid
    # 广播用户列表
    emit("user_list", list(online_users.keys()), broadcast=True)

# 发送消息
@socketio.on("send_message")
def handle_message(data):
    sender = data["sender"]
    receiver = data["receiver"]
    msg = data["message"]

    # 如果对方在线，发给对方
    if receiver in online_users:
        emit("receive_message",
            {"sender": sender, "message": msg},
            to=online_users[receiver])

if __name__ == "__main__":
    socketio.run(app, host="127.0.0.1", port=5000, debug=True)
