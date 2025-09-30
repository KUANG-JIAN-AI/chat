from flask import request
from flask_socketio import emit

# 在线用户 {nickname: session_id}
online_users = {}


def register_events(socketio):
    @socketio.on("login")
    def handle_login(data):
        nickname = data["nickname"]
        online_users[nickname] = request.sid
        # 广播在线用户列表
        emit("user_list", list(online_users.keys()), broadcast=True)

    @socketio.on("send_message")
    def handle_message(data):
        sender = data["sender"]
        receiver = data["receiver"]
        msg = data["message"]

        # 如果对方在线，发给对方
        if receiver in online_users:
            emit(
                "receive_message",
                {"sender": sender, "message": msg},
                to=online_users[receiver],
            )
