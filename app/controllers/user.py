from flask import current_app, request

from app.models.user import Users, db


def login():
    data = request.get_json()  # 从请求体里解析 JSON
    nickname = data.get("nickname")
    password = data.get("password")

    if not nickname or not password:
        return {"code": 400, "msg": "nickname or password missing"}

    with current_app.app_context():
        user = Users.query.filter_by(nickname=nickname).first()

        if user is None:
            user = Users(nickname=nickname)
            user.set_password(password)  # 加密密码

            db.session.add(user)
            db.session.commit()
            return {
                "code": 200,
                "msg": "success",
                "data": {"id": user.id, "nickname": user.nickname},
            }

        if user.check_password(password):
            return {
                "code": 200,
                "msg": "login success",
                "data": {"id": user.id, "nickname": user.nickname},
            }
        else:
            return {"code": 401, "msg": "wrong password"}


def get_friends():
    users = Users.query.all()
    return {"code": 200, "msg": "success", "data": [u.to_dict() for u in users]}
