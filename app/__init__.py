from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # 数据库实例

socketio = SocketIO(cors_allowed_origins="*")

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # 初始化数据库
    db.init_app(app)

    # 初始化 socketio
    socketio.init_app(app)

    # 注册蓝图
    from .routers import main_bp
    app.register_blueprint(main_bp)

    # 注册 socketio 事件
    from .controllers import chat
    chat.register_events(socketio)

    return app
